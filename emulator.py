from lib import *

# by Xiang Gao, 2018



def find_ideal(p, just_once):
	if not just_once:
		diff = np.array(p[1:]) - np.array(p[:-1])
		return sum(np.maximum(np.zeros(diff.shape), diff))
	else:
		best = 0.
		i0_best = None
		for i in range(len(p)-1):
			best = max(best, max(p[i+1:]) - p[i])

		return best


class Market:
	"""
	state 			MA of prices, normalized using values at t
					ndarray of shape (window_state, n_instruments * n_MA), i.e., 2D
					which is self.state_shape

	action 			three action
					0:	empty, don't open/close. 
					1:	open a position
					2: 	keep a position
	"""
	
	def reset(self, rand_price=True):
		self.empty = True
		if rand_price:
			prices, self.title = self.sampler.sample()
			price = np.reshape(prices[:,0], prices.shape[0])

			self.prices = prices.copy()
			self.price = price/price[0]*100
			self.t_max = len(self.price) - 1

		self.max_profit = find_ideal(self.price[self.t0:], False)
		self.t = self.t0
		return self.get_state(), self.get_valid_actions()


	def get_state(self, t=None):
		if t is None:
			t = self.t
		state = self.prices[t - self.window_state + 1: t + 1, :].copy()
		for i in range(self.sampler.n_var):
			norm = np.mean(state[:,i])
			state[:,i] = (state[:,i]/norm - 1.)*100	
		return state

	def get_valid_actions(self):
		if self.empty:
			return [0, 1]	# wait, open
		else:
			return [0, 2]	# close, keep


