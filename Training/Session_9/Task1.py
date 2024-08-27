import random
from random import randint

N = 8  # Number of queens
POPULATION_SIZE = 100
TARGET = N * (N - 1) // 2 
LENGTH = N 
MIN = 0
MAX = N - 1

def individual():
    return random.sample(range(N), N)

def population(count):
    return [individual() for _ in range(count)]

def fitness(individual):
    non_attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if abs(individual[i] - individual[j]) != j - i:
                non_attacking_pairs += 1
    return abs(TARGET - non_attacking_pairs)

def TournamentSelection(population, desired_length, tournament_size):
    new_offspring = []
    for _ in range(desired_length):
        candidates = [random.choice(population) for _ in range(tournament_size)]
        new_offspring.append(min(candidates, key=lambda ind: ind[0]))
    return new_offspring

def crossover(parents, desired_length):
    parents_length = len(parents)
    children = []
    while len(children) < desired_length:
        indxmale = randint(0, parents_length-1)
        indxfemale = randint(0, parents_length-1)
        if indxmale != indxfemale:
            male = parents[indxmale]
            female = parents[indxfemale]
            half = round(len(male[1]) / 2)
            child = male[1][:half] + female[1][half:]
            children.append([fitness(child), child])
    return children

def mutation(parents, mutate):
    mutation_length = int(len(parents) * mutate)
    for _ in range(mutation_length):
        individual = random.choice(parents)
        pos_to_mutate = randint(0, LENGTH-1)
        individual[1][pos_to_mutate] = randint(MIN, MAX)
        x = fitness(individual[1])
        individual[0] = x
    return parents

def GeneticAlgorithm(pop, target, retain=0.2, mutate=0.01):
    generation = 0
    found = False
    population = [[fitness(x), x] for x in pop]
    while not found:
        population = sorted(population, key=lambda x: x[0])
        if population[0][0] == 0:
            found = True
            break

        retrain_length = int(len(population) * retain)
        new_generation = population[:retrain_length]
        desired_length = len(population) - retrain_length
        selectionParents = TournamentSelection(population, desired_length, 3)
        new_generation.extend(crossover(selectionParents, desired_length))
        new_generation = mutation(new_generation, mutate)
        
        population = new_generation
        population = sorted(population, key=lambda x: x[0])
        print(f"Generation: {generation}, Best Fitness: {population[0][0]}")
        generation += 1

    print(f"Solution Found in Generation: {generation}")
    print("Board Configuration:")
    print(population[0][1])

GeneticAlgorithm(population(POPULATION_SIZE), TARGET)

