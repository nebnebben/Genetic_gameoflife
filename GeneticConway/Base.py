import numpy as np
import geneticalgorithm as ga
import conwaysgame as game

pop_num = 9
best_num = 1
rest_num = int(pop_num - best_num)

gridsize = 8
gen_num = 200
iterations = 30

bestsofar = 0  # highest fitness found so far

general_pop = np.random.randint(2, size=(pop_num, gridsize, gridsize))
# create mask to make sure outside values = 0?
general_pop = np.pad(general_pop, pad_width=((0, 0), (1, 1), (1, 1)), mode='constant', constant_values=0)
# Adds '0's to the sides of each matrix
# Makes conway's game of life easier to use

for gen in range(gen_num):
    print("Gen {}".format(gen))
    current_pop = game.simulate(general_pop, pop_num, iterations, gridsize)
    # print("current pop is ", current_pop)
    prob, genfit = ga.fitness(current_pop, pop_num)
    # Works out fitnesses of each individual
    # And probability of all selecting an individual
    fitness_indices = np.argsort(genfit)[::-1][:best_num]
    #Returns the indices of what the sorted would be and gets the last ones
    #e.g the biggest
    if sorted(genfit)[-1] > bestsofar:
        bestsofar = sorted(genfit)[-1]
        print(bestsofar)
        print(general_pop[fitness_indices[0]])
    # Gets the best individuals in a generation
    # Where the number of individuals selected is best_num
    new_pop = []
    # New population
    for i in fitness_indices:
        new_pop.append(general_pop[i])
        if gen % 10 == 0:
            print(general_pop[i])
            print(genfit)
#    print("New pop is, ", new_pop)
    # Keep the most successful elements of the last generation in the new one
    offspring = ga.crossover(general_pop, prob, rest_num, gridsize)
    # Uses parents to get offspring
    offspring = ga.mutate(offspring, rest_num)
    # Mutates the offspring
    for i in range(rest_num):
        #Not equal to aprent
        new_pop.append(offspring[i])
    # print("New pop is, ", new_pop)
    # Adds this offspring to the new population
    # print("General pop is:", general_pop)
    general_pop = np.array(new_pop)

print(general_pop)
print("and after")
current_pop = game.simulate(general_pop, pop_num, iterations, gridsize)
print(current_pop)
# print(general_pop[:, 1:-1, 1:-1])
# Gets the new middle values of the matrix, ignores 0 edges
prob, genfit = ga.fitness2(current_pop, pop_num)
print(genfit)


# Weird error out of bounds thing