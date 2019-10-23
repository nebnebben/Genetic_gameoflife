import numpy as np

def neighbours(matrix, x, y):
    sum = 0
    # No of neighbours
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            sum += matrix[i, j]
    # Counts up no. of neighbours, not counting itself, 0-8
    if matrix[x, y] == 1:
        sum -= 1
#    print("The sum is {} at i{} j{}".format(sum, x, y))
    return sum

def updatecell(n, alive):
    # How to update the current cell
    # Depending on neighbours and if alive/dead
    if alive:
        if n < 2:
            return 0
        elif n > 3:
            return 0
        else:
            return 1
    else:
        if n == 3:
            return 1
        else:
            return 0


def updatematrix(matrix, gridsize):
    newmatrix = np.zeros((gridsize+2, gridsize+2))
    # Makes a new matrix equal to the old one
    # Nested for loop only applies to middle values of matrix, ignoring edges
    for x in range(1, gridsize+1):
        for y in range(1, gridsize+1):
            n = neighbours(matrix, x, y)
            # No of live neighbouring cells
            if matrix[x, y] == 1:
                newmatrix[x, y] = updatecell(n, True)
            else:
                newmatrix[x, y] = updatecell(n, False)
            # Updates new matrix
    # print("This is the new matrix", newmatrix)
    return newmatrix


def simulate(pop, pop_num, iterations, gridsize):
    # print("The pop is ", pop)
    newpop = np.copy(pop)
    # To get around python's parameter passing peculiarities
    for x in range(pop_num):
        # print("This is the pop thing before", pop[x])
        for i in range(iterations):
            # print(i)
            # print("it {} Before: {}".format(i, pop[x]))
            newpop[x] = updatematrix(newpop[x], gridsize)
            # print("it {} After: {}".format(i, pop[x]))
    return newpop


# Need new matrix