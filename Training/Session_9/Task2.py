import random
import math

class SimulatedAnnealingOneMax:
    def __init__(self, bitstring_length, temp_start, temp_end, alpha, max_iter):
        self.bitstring_length = bitstring_length
        self.temp_start = temp_start
        self.temp_end = temp_end
        self.alpha = alpha
        self.max_iter = max_iter

        # Initialize state
        self.current_state = self.random_bitstring()
        self.current_fitness = self.fitness(self.current_state)
        self.best_state = self.current_state.copy()
        self.best_fitness = self.current_fitness
        self.temp = temp_start

    def random_bitstring(self):
        return [random.randint(0, 1) for _ in range(self.bitstring_length)]

    def fitness(self, bitstring):
        return sum(bitstring)

    def generate_neighbor(self, state):
        neighbor = state.copy()
        index = random.randint(0, self.bitstring_length - 1)
        neighbor[index] = 1 - neighbor[index]  # Flip the bit
        return neighbor

    def anneal(self):
        for count in range(self.max_iter):
            # Generate a neighboring state
            neighbor = self.generate_neighbor(self.current_state)
            neighbor_fitness = self.fitness(neighbor)

            # Calculate the difference in fitness
            delta = neighbor_fitness - self.current_fitness

            # Decide whether to accept the neighbor state
            if delta > 0 or random.random() < math.exp(delta / self.temp):
                self.current_state = neighbor
                self.current_fitness = neighbor_fitness
                if neighbor_fitness > self.best_fitness:
                    self.best_state = neighbor
                    self.best_fitness = neighbor_fitness

            # Update the temperature
            self.temp = max(self.temp * self.alpha, self.temp_end)

            # Print the current generation and fitness
            print(f"Iteration {count}: Fitness {self.current_fitness}")

            # Stop if the optimal solution is found
            if self.best_fitness == self.bitstring_length:
                print(f"Found optimal solution at iteration {count}")
                break

        return self.best_state

# Example usage
bitstring_length = 10
sa = SimulatedAnnealingOneMax(bitstring_length, temp_start=1000, temp_end=0.1, alpha=0.95, max_iter=1000)
best_solution = sa.anneal()
print("Best solution:", best_solution)
print("Number of ones in the best solution:", sa.fitness(best_solution))
