import math
import random

class SimulatedAnnealing():
    
    def __init__(self, fitness_function, neighborhood_function, initial_temperature, cooling_rate, max_iterations, final_temperature, initial_solution):
        self.fitness_function = fitness_function
        self.neighborhood_function = neighborhood_function
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.max_iterations = max_iterations
        self.final_temperature = final_temperature
        self.current_solution = initial_solution
        self.best_solution = initial_solution
        
    def run(self):
        current_temperature = self.initial_temperature
        for i in range(self.max_iterations):
            if current_temperature < self.final_temperature:
                break
            neighbor_solution = self.neighborhood_function(self.current_solution)
            delta = self.fitness_function(neighbor_solution) - self.fitness_function(self.current_solution)
            if delta < 0:
                self.current_solution = neighbor_solution
                if self.fitness_function(self.current_solution) < self.fitness_function(self.best_solution):
                    self.best_solution = self.current_solution
            else:
                probability = math.exp(-delta/current_temperature)
                if random.random() < probability:
                    self.current_solution = neighbor_solution
            current_temperature *= self.cooling_rate
    
        return self.best_solution
