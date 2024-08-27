import random
from random import randint

TARGET = 200
MIN = 0
MAX = 100
LENGTH=5
# Create suggested solution according to length value and min & max


def individual( ):
    return [randint(MIN, MAX) for x in range(LENGTH)] #chromosome [length=5]


def population(count): #100
    return [individual() for x in range(count)]


def fitness(individual):
    total = sum(individual)
    return abs(TARGET-total)


def mutation(parents, mutate):
    mutation_length = int(len(parents)*mutate)
    for _ in range(mutation_length):
        individual = random.choice(parents)
        pos_to_mutate = randint(0, LENGTH-1)
        individual[1][pos_to_mutate] = randint(MIN, MAX)
        x = fitness(individual[1])
        individual[0] = x
    return parents


def crossover(parents, desired_length):
    parents_length = len(parents)
    children = []
    while len(children) < desired_length:
        indxmale = randint(0, parents_length-1)  # =>10
        indxfemale = randint(0, parents_length-1)  # => 12
        if indxmale != indxfemale:
            male = parents[indxmale]  # =>  [12, [1,2,3,4,5]]
            female = parents[indxfemale]  # [13, [2,3,4,5,6]]
            half = round(len(male[1]) / 2)  # =>2
            child = male[1][:half] + female[1][half:]
           # [1,2]+[4,5,6]=[1,2,4,5,6]
            children.append([fitness(child), child])
    return children


def TournamentSelection(population, desired_length, tournament_size):
    new_offspring = []
    for _ in range(desired_length):
        candidates = [random.choice(population) for _ in range(tournament_size)]
        new_offspring.append(min(candidates, key=lambda ind: ind[0]))
    return new_offspring


def GeneticAlgorithm(pop, target, retain=0.2, mutate=0.01):
    generation = 0
    found = False
    population = [[fitness(x), x] for x in pop]
    while(not found):
        population = sorted(population, key=lambda x: x[0])
        if population[0][0] == 0:
            found=True
            break
        # population = [ x[1] for x in sorted(population)]
        retrain_length = int(len(population)*retain)
        # elitism
        new_generation= population[:retrain_length] #10
        desired_length=len(population)-retrain_length #90

        selectionParents=TournamentSelection(population,desired_length, 3) #90

        # crossover parents to create children
        # desired_length = len(population) - len(new_generation)
        new_generation.extend(crossover(selectionParents,desired_length)) #100

        # mutate some individuals
        new_generation=mutation(new_generation,mutate)
        
        population = new_generation
        population = sorted(population, key=lambda x: x[0])
        print("\n Generation "+str(generation) +"\n"+ "Best Individual " +str (population[0][1]) + " fitness " +str(population[0][0])+"\n"\
            + "Median Individual " +str(population[50][1]) + " fitness " +str(population[50][0])+"\n"\
               + "Worst Individual " +str(population[99][1]) + " fitness " +str(population[99][0])+"\n" )
        # print("Generation: {}\tIndividual: {}\tFitness: {}".\
        #     format(generation,
		# 	"".join(str(population[0][1])),
		# 	str(population[0][0])))
        generation += 1
       

        
    print("In Generation: {}\tString: {}\tFitness: {}".\
			format(generation,
			"".join(str(population[0][1])),
			str(population[0][0])))

GeneticAlgorithm(population(100), 200)
# GeneticAlgorithm(pop=population,target=200,retain=0.01) #default parameter

# attributes Target, sizepop, Min, Max

# def fitness(individual):
    # sum=sum(indiviual[1])
    # return abs(Target-sum)

# def Indiviual(LengthChromosome, Min,Max):
   #    indi =[random.ranint(min=0,max=100)   for lengthchromosome] ==>(1)

# def CreateInitPop(sizePop, LengthChromosome, Min,Max):   ==>(2)
     #  [ Indiviual(LengthChromosome, Min,Max) for_ in sizepop  ]

# Population=CreateInitPop(sizePop, LengthChromosome, Min,Max)

# Population= [[fitness(item), item]   for item in  Population] ==> (3)

# def GeneticAlgorithm(Population, target): (4)
    #   sort
    # if found:
        # print 
        # return
    # while(true):                      ====>(4.1)
        # elitism=0.2
        # selection (tournament selection)  ====>(4.2)
        # crossover                         ====>(4.3)
        # mutation                          ====>(4.5)
        # sort
        # if (item[0][0] = 0) 
            # generation+=1
            # break                         ====>(4.5)