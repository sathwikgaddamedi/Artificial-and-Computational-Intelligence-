import math
import random

def rastrigin_function(x):
    """ Rastrigin function: a non-convex function used for testing optimization algorithms """
    A = 10
    return A + x**2 - A * math.cos(2 * math.pi * x)

def simulated_annealing(objective_function, x_start, temp_start, temp_min, cooling_rate, max_iterations):
    """ Simulated Annealing algorithm for function optimization """
    x_current = x_start
    best_x = x_current
    best_eval = objective_function(x_current)
    
    temp = temp_start  # Initial temperature
    for i in range(max_iterations):
        if temp < temp_min:
            break
        
        # Generate a new candidate solution
        x_new = x_current + random.uniform(-1, 1)
        new_eval = objective_function(x_new)

        # Accept new solution based on probability
        delta = new_eval - best_eval
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temp):
            x_current = x_new
            if new_eval < best_eval:
                best_x, best_eval = x_new, new_eval
        
        # Cool down
        temp *= cooling_rate

    return best_x, best_eval

# Parameters
x_start = random.uniform(-5.12, 5.12)  # Initial point
temp_start = 100.0  # Starting temperature
temp_min = 0.01  # Minimum temperature
cooling_rate = 0.99  # Cooling factor
max_iterations = 1000  # Maximum iterations

# Run Simulated Annealing
best_solution, best_value = simulated_annealing(rastrigin_function, x_start, temp_start, temp_min, cooling_rate, max_iterations)

# Output results
print(f"Best solution found: x = {best_solution:.5f}, f(x) = {best_value:.5f}")
