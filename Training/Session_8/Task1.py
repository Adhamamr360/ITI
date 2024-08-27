import random

class Individual:
    def __init__(self, solution, fitness):
        self.solution = solution
        self.fitness = fitness

    def print_items(self):
        print("The solution is " + str(self.solution) + " and the fitness is " + str(self.fitness))

    def __repr__(self):
        return f"Individual(solution={self.solution}, fitness={self.fitness})"


class Population:
    def __init__(self, individuals):
        self.individuals = individuals

    def rank_selection(self, num_parents):
        sorted_population = sorted(self.individuals, key=lambda x: x.fitness, reverse=True)
        total_rank = sum(i + 1 for i in range(len(sorted_population)))
        probabilities = [(i + 1) / total_rank for i in range(len(sorted_population))]
        selected_parents = random.choices(sorted_population, weights=probabilities, k=num_parents)
        return selected_parents

    def tournament_selection(self, tournament_size, num_parents):
        selected_parents = []
        while len(selected_parents) < num_parents:
            tournament = random.sample(self.individuals, tournament_size)
            winner = max(tournament, key=lambda x: x.fitness)
            selected_parents.append(winner)
        return selected_parents

    def roulette_wheel_selection(self, num_parents):
        fitness_values = [ind.fitness for ind in self.individuals]
        total_fitness = sum(fitness_values)
        probabilities = [fitness / total_fitness for fitness in fitness_values]
        selected_parents = random.choices(self.individuals, weights=probabilities, k=num_parents)
        return selected_parents

    def __repr__(self):
        return f"Population(individuals={self.individuals})"


if __name__ == "__main__":
    individuals = [
        Individual("Solution1", 10),
        Individual("Solution2", 5),
        Individual("Solution3", 15),
        Individual("Solution4", 8)
    ]
    
    population = Population(individuals)
    
    # Using ranking selection
    parents_rank = population.rank_selection(2)
    print("Ranking Selection:")
    for parent in parents_rank:
        print(parent)
    
    # Using tournament selection
    parents_tournament = population.tournament_selection(2, 2)
    print("\nTournament Selection:")
    for parent in parents_tournament:
        print(parent)
    
    # Using roulette wheel selection
    parents_roulette = population.roulette_wheel_selection(2)
    print("\nRoulette Wheel Selection:")
    for parent in parents_roulette:
        print(parent)
