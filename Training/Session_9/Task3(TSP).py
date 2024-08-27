import random

# Parameters
CITIES = 10  # Number of cities
POPULATION_SIZE = 100
GENERATIONS = 1000
MUTATION_RATE = 0.01

# Sample coordinates for cities
city_coords = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(CITIES)]

# Function to calculate the distance between two cities
def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5

# Function to calculate the total distance of a tour
def total_distance(tour):
    return sum(distance(city_coords[tour[i]], city_coords[tour[i-1]]) for i in range(len(tour)))

# Create a random individual (tour)
def individual():
    return random.sample(range(CITIES), CITIES)

# Create a population of random individuals
def population(count):
    return [individual() for _ in range(count)]

# Calculate fitness as the inverse of the total distance
def fitness(individual):
    return 1 / total_distance(individual)

# Tournament selection
def tournament_selection(pop, tournament_size):
    selected = random.sample(pop, tournament_size)
    return min(selected, key=lambda x: x[0])

# Ordered crossover (OX)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(CITIES), 2))
    child = [None] * CITIES
    child[start:end] = parent1[start:end]
    for city in parent2:
        if city not in child:
            for i in range(CITIES):
                if child[i] is None:
                    child[i] = city
                    break
    return child

# Mutation by swapping two cities
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(CITIES), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

# Genetic Algorithm
def genetic_algorithm():
    pop = population(POPULATION_SIZE)
    pop = [(fitness(ind), ind) for ind in pop]
    generation = 0
    
    while generation < GENERATIONS:
        pop = sorted(pop, key=lambda x: x[0], reverse=True)
        
        if generation % 100 == 0:
            print(f"Generation {generation}, Best Fitness: {pop[0][0]:.4f}, Distance: {1/pop[0][0]:.2f}")
        
        new_generation = pop[:int(POPULATION_SIZE * 0.1)]  # Elitism: keep the top 10%
        desired_length = POPULATION_SIZE - len(new_generation)
        
        while len(new_generation) < POPULATION_SIZE:
            parent1 = tournament_selection(pop, 3)
            parent2 = tournament_selection(pop, 3)
            child = crossover(parent1[1], parent2[1])
            child = mutate(child, MUTATION_RATE)
            new_generation.append((fitness(child), child))
        
        pop = new_generation
        generation += 1
    
    best_individual = max(pop, key=lambda x: x[0])
    print(f"Best solution found in Generation {generation}")
    print(f"Tour: {best_individual[1]}")
    print(f"Distance: {1/best_individual[0]:.2f}")

# Run the Genetic Algorithm
genetic_algorithm()
