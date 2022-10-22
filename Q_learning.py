from lib import *
from sampler import *
from agents import *
from emulator import *
from simulators import *
from visualizer import *
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

class SupplyChainEnvironment:
    def __init__(self, initial_inventory, demand_estimates, lead_times, holding_cost, backorder_cost):
        self.initial_inventory = initial_inventory
        self.current_inventory = initial_inventory.copy()
        self.demand_estimates = demand_estimates
        self.lead_times = lead_times
        self.holding_cost = holding_cost
        self.backorder_cost = backorder_cost
        self.time_step = 0

    def reset(self):
        self.current_inventory = self.initial_inventory.copy()
        self.time_step = 0

    def get_state(self):
        return np.concatenate([self.current_inventory, self.lead_times])

    def get_possible_actions(self):
        return np.arange(0, 101, 10)

    def take_action(self, action):
        order_quantity = action
        lead_time = self.lead_times[self.time_step]
        demand = np.random.normal(self.demand_estimates[self.time_step], 5)  
        demand = max(demand, 0)  

        on_hand_inventory = max(self.current_inventory - demand, 0)

        holding_cost = self.holding_cost * max(on_hand_inventory, 0)
        backorder_cost = self.backorder_cost * max(demand - self.current_inventory, 0)
        total_cost = holding_cost + backorder_cost

        self.current_inventory = on_hand_inventory + order_quantity

        self.time_step += 1

        return total_cost

    def get_reward(self):
        return -self.take_action(0)


def get_model(model_type, env, learning_rate, fld_load):
	print_t = False
	print ("\t\t\t |--------- ****** optimization process for  storage capacity and cost-efficiency ****** --------|")
	exploration_init = 1.

	if model_type == 'MLP':
		m = 16
		layers = 5
		hidden_size = [m]*layers
		model = QModelMLP(env.state_shape, env.n_action)
		model.build_model(hidden_size, learning_rate=learning_rate, activation='tanh')
	
	elif model_type == 'conv':
		m = 16
		layers = 2
		filter_num = [m]*layers
		filter_size = [3] * len(filter_num)
		use_pool = None
		dilation = None
		dense_units = [48,24]
		model = QModelConv(env.state_shape, env.n_action)
		model.build_model(filter_num, filter_size, dense_units, learning_rate, 
			dilation=dilation, use_pool=use_pool)

	elif model_type == 'RNN':

		m = 32
		layers = 3
		hidden_size = [m]*layers
		dense_units = [m,m]
		model = QModelGRU(env.state_shape, env.n_action)
		model.build_model(hidden_size, dense_units, learning_rate=learning_rate)
		print_t = True

	elif model_type == 'ConvRNN':
	
		m = 8
		conv_n_hidden = [m,m]
		RNN_n_hidden = [m,m]
		dense_units = [m,m]
		model = QModelConvGRU(env.state_shape, env.n_action)
		model.build_model(conv_n_hidden, RNN_n_hidden, dense_units, learning_rate=learning_rate)
		print_t = True

	elif model_type == 'pretrained':
		agent.model = load_model(fld_load, learning_rate)

	else:
		raise ValueError
		
	return model, print_t


def main():

	print ("\t\t\t ****** Define state, action, and reward functions using demand estimates, lead times, and supply chain costs ******")
	model_type = 'conv'; exploration_init = 1.; fld_load = None
	n_episode_training = 1
	n_episode_testing = 1
	open_cost = 3.3
	db_type = 'PairSamplerDB'; db = 'randjump_100,1(10, 30)[]_'; Sampler = PairSampler
	batch_size = 8
	learning_rate = 1e-4
	discount_factor = 0.8
	exploration_decay = 0.99
	exploration_min = 0.01
	window_state = 40

	fld = os.path.join('..','data',db_type,db+'A')
	sampler = Sampler('load', fld=fld)
	env = Market(sampler, window_state, open_cost)
	model, print_t = get_model(model_type, env, learning_rate, fld_load)
	model.model.summary()

	agent = Agent(model, discount_factor=discount_factor, batch_size=batch_size)
	visualizer = Visualizer(env.action_labels)

	fld_save = os.path.join(OUTPUT_FLD, sampler.title, model.model_name, 
		str((env.window_state, sampler.window_episode, agent.batch_size, learning_rate,
			agent.discount_factor, exploration_decay, env.open_cost)))
	
	print('='*20)
	print(fld_save)
	print('='*20)

	simulator = Simulator(agent, env, visualizer=visualizer, fld_save=fld_save)
	simulator.train(n_episode_training, save_per_episode=1, exploration_decay=exploration_decay, 
		exploration_min=exploration_min, print_t=print_t, exploration_init=exploration_init)

	simulator.test(n_episode_testing, save_per_episode=1, subfld='in-sample testing')

if __name__ == '__main__':
	main()
