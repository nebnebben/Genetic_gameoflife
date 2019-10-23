import numpy as np


def fitness(pop, pop_num):
    genfit = []
    # stores fitnesses of all the individuals
    for c in range(pop_num):
        # calculates the fitness and stores it for each individual
        genfit.append((pop[c] == 1).sum())
#        print(genfit)

    square = lambda i: i*i
    vector_square = np.vectorize(square)
    genfit = vector_square(genfit)
    # Squares fitnesses to emphasise difference between successful/unsuccessful solutions
    total = np.sum(genfit)
    prob = genfit/total
    # May not always add up to 1, rounding error?
    # also, np.choice gives error is value is 0?
    # prob gets relative strength of solutions to use as probabilities
    return prob, genfit

def fitness2(pop, pop_num):
    genfit = []
    # stores fitnesses of all the individuals
    # print(pop)
    for c in range(pop_num):
        # calculates the fitness and stores it for each individual
        genfit.append((pop[c] == 1).sum())
        print(pop[c])
        print(genfit)

    square = lambda i: i*i
    vector_square = np.vectorize(square)
    genfit = vector_square(genfit)
    # Squares fitnesses to emphasise difference between successful/unsuccessful solutions
    total = np.sum(genfit)
    prob = genfit/total
    # May not always add up to 1, rounding error?
    # also, np.choice gives error is value is 0?
    # prob gets relative strength of solutions to use as probabilities
    return prob, genfit

def crossover(pop, prob, parentnum, gridsize):
    children = []
    # Change pop -- errors!!
    # where the children are stored
    for c in range(int(parentnum/2)):
        index = np.random.choice(pop.shape[0], size=2, replace=True, p=prob)
        # gets random indexes from population probabilistically
        # Replace equals true so that in the edge case where only there is only one non-zero probability it
        # doesn't crash
        parent1 = pop[index[0]]
        # sets the parent with that index
        parent2 = pop[index[1]]
        cross_dimensions = np.random.randint(low=1, high=gridsize, size=2)
        # ab[2:4,2:4] = bc[2:4,2:4]
        # means ab = ab, swapped with rows + columns 2-3 of bc
        # Gets how much of each parent will be crossed over
        # Up to the size-1, so that it's not just every co-ordinate being switched


        xstart = np.random.randint(gridsize-cross_dimensions[0]+1) + 1
        # Where x part of the grid is starting to be swapped
        xend = xstart + cross_dimensions[0]
        ystart = np.random.randint(gridsize-cross_dimensions[0]+1) + 1
        # The same but for the y
        yend = ystart + cross_dimensions[0]


        child1 = parent1
        child2 = parent2
        # Defaults with the same value as parent
        child1[xstart:xend, ystart:yend] = parent2[xstart:xend, ystart:yend]
        child2[xstart:xend, ystart:yend] = parent1[xstart:xend, ystart:yend]
        # Children are different their parent, with different sub-matrix of another individual swapped in
        children.append(child1)
        children.append(child2)
    children = np.array(children)
    # print(children)
    return children


def probflip(val):
    prob = np.random.uniform(0, 1, 1) < 0.05
    # Gets random number between 0 and 1
    # Sets true or false depending on whether its under a certain value
    # Likelihood of flipping a bit
    if prob:
        if val == 0:
            val = 1
        else:
            val = 0
    return val


def mutate(pop, rest_num):
    prob = np.vectorize(probflip)
    # prob applies probflip function to each element in the array
    for i in range(rest_num):
        # for each element in the array
        pop[i][1:-1,1:-1] = prob(pop[i][1:-1,1:-1])
        # Mutate each element with a small probability
    return pop
