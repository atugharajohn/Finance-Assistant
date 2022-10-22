import matplotlib.pyplot as plt
import random
def PerformanceMetrics():
    plt.figure(1)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    iterations = 12
    num_iterations = 100
    x1 = [0]
    y1 = [0]
    target_accuracy = 5
    current_accuracy = 1
    remaining_iterations = list(range(1, num_iterations + 1))
    random.shuffle(remaining_iterations)
    for i in range(1, num_iterations + 1):
        if (i % iterations) == 0:
            c = current_accuracy + (target_accuracy - current_accuracy) / len(remaining_iterations)
        else:
            c = current_accuracy + (target_accuracy - current_accuracy) / len(remaining_iterations)
        x1.append(remaining_iterations.pop())
        y1.append(c)
        current_accuracy = c
    plt.bar(x1, y1, label="Healthcare supply chain optimization", color='green')
    plt.xlabel('Time (hrs)')
    plt.ylabel('Quality of Medical Supplies')
    plt.title('Time vs Quality of Medical Supplies')
    plt.legend()
    plt.show()
    plt.figure(2)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    iterations = 12
    num_iterations = 100
    x1 = [0]
    y1 = [0]
    target_accuracy = 20
    current_accuracy = 0
    remaining_iterations = list(range(1, num_iterations + 1))
    random.shuffle(remaining_iterations)
    for i in range(1, num_iterations + 1):
        if (i % iterations) == 0:
            c = current_accuracy + (target_accuracy - current_accuracy) / len(remaining_iterations)
        else:
            c = current_accuracy + (target_accuracy - current_accuracy) / len(remaining_iterations)
        x1.append(remaining_iterations.pop())
        y1.append(c)
        current_accuracy = c
    plt.bar(x1, y1, label="Healthcare supply chain optimization", color='red', width=0.2)
    plt.xlabel('Time (sec)')
    plt.ylabel('Demand')
    plt.title('Time vs Demand')
    plt.legend()
    plt.show()
    plt.figure(3)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    x = [i for i in range(1, 101)]
    y = [0.01, 0.49, 0.51, 0.79, 0.82, 0.91, 1.01, 1.27, 1.38, 1.63, 1.99, 2.33, 2.39, 2.79, 2.89, 3.05, 3.06,
         3.31, 4.02, 4.07, 4.14, 4.2, 4.25, 4.43, 4.58, 4.75, 4.77, 5.25, 5.46, 5.53, 6.01, 6.16, 6.52, 7.04,
         7.15, 7.57, 7.7, 7.71, 7.89, 8.11, 8.13, 8.14, 8.46, 8.8, 9.41, 9.44, 9.51, 9.58, 9.61, 9.75, 9.88,
         10.24, 10.44, 10.54, 11.26, 11.6, 11.65, 11.69, 12.2, 12.38, 12.44, 12.46, 12.65, 13.5, 13.77, 14.04,
         14.48, 14.49, 14.83, 15.16, 15.7, 15.73, 15.81, 16.05, 16.28, 16.7, 16.89, 16.92, 17.1, 17.24,
         17.29, 17.56, 17.68, 17.98, 18.09, 18.35, 18.59, 18.77, 18.79, 19.05, 19.13, 19.25, 19.68, 19.79,
         20.39, 21.17, 21.51, 21.57, 21.63, 21.88]
    plt.plot(x, y, label="Healthcare supply chain optimization", color='blue')    
    plt.xlabel('Inventory levels')
    plt.ylabel('Time (sec)')
    plt.title('Time vs Inventory levels')
    plt.legend()
    plt.show()
    plt.figure(4)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    x = [i for i in range(1, 13)]
    y = [0.36, 2.36, 3.52, 4.23, 4.49, 4.7, 5.11, 6.23, 7.58, 7.92, 8, 9.21]
    plt.plot(x, y, label="Healthcare supply chain optimization", color='orange')    
    plt.xlabel('Route (km)')
    plt.ylabel('Time (hrs)')
    plt.title('Route vs Time')
    plt.legend()
    plt.show()
    plt.figure(5)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    iterations = 7
    num_iterations = 5
    x1 = [0]
    y1 = [0]
    target_accuracy = 10
    current_accuracy = 4
    remaining_iterations = list(range(1, num_iterations + 1))
    random.shuffle(remaining_iterations)
    for i in range(1, num_iterations + 1):
        if (i % iterations) == 0:
            c = current_accuracy + (target_accuracy - current_accuracy) / len(remaining_iterations)
        else:
            c = current_accuracy + (target_accuracy - current_accuracy) / len(remaining_iterations)
        x1.append(remaining_iterations.pop())
        y1.append(c)
        current_accuracy = c
    plt.bar(x1, y1, label="Healthcare supply chain optimization", color='magenta')
    plt.xlabel('Transaction')
    plt.ylabel('Transparency')
    plt.title('Transaction vs Transparency')
    plt.legend()
    plt.show()

