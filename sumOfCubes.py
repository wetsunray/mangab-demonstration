"""create a function that returns the set of all integers that can be expressed
as the sum of three cubes less than the argument given in the function"""
import math
import itertools

def combiner(numCombs):
    finalList = []
    sumsList = []
    for c in itertools.combinations(numCombs[0], numCombs[1]):
        sums = sum(c)
        if sums not in sumsList:
            sumsList.append(sums)
            finalList.append([sums, c])
    return(sorted(finalList))

def cubesList(maxNumber):
    rtnList = []
    for i in range(1, maxNumber+1):#This part makes it so that it includes the max num
                                   #and also does not include the number 0
        rtnList.append(i**3)
    return rtnList

def maxValue(number):
    maxValue =  math.floor(number ** (1.0/3.0))
    return maxValue


def numCombs(cubesList):
    pool = []
    length = len(cubesList)
    for i in range(3):
        for i in range(len(cubesList)):
            pool.append(cubesList[i])
    return (pool, 3)

def sumOfCubes(number):
    maxValue2 = maxValue(number)
    cubesList2 = cubesList(maxValue2)
    numCombs2 = numCombs(cubesList2)
    combiner2 = combiner(numCombs2)
    solutions = []
    for i in combiner2:
        if i[0] <= number:
            solutions.append(i)
    print("there were", len(solutions), "solutions found.")
    print("The following numbers can be expressed as a sum of three cubes >= 1")
    print("Those solutions were:")
    for index in solutions:
        print(index[0], ", which is formed by these three cubes:", index[1])
    
        


def main():
    """
    print("maxValue(10) is")
    print(maxValue(10))
    print("cubesList(maxValue(10)) is")
    print(cubesList(maxValue(10)))
    print("numCombs(cubesList(maxValue(10))) is")
    print(numCombs(cubesList(maxValue(10))))
    print("combiner(numCombs(cubesList(maxValue(10)))) is")
    print(combiner(numCombs(cubesList(maxValue(10)))))"""
    sumOfCubes(1000)
if __name__ == "__main__":
    main()
