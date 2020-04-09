# Used for random number generation for the list.
import random
import math
import time

# Constant value for the size of the list.
sizeOfList = pow(10, 6)

# Constant value for the size of the numbers in the list.
listRange = pow(100, 15)

# generateList ... Returns a sorted list of n elements.
def generateList(n):
    values = []
    for val in range(0, n):
        values.append(random.randint(0, listRange))

    values.sort()
    return values

# binarySearch ... Search list values for target using a the binary search algorithm.
def binarySearch(values, target):
    floorBounds = 0
    roofBounds = sizeOfList - 1    
    targetIndex = -1

    while (floorBounds < roofBounds):
        middleIndex = math.floor((floorBounds + roofBounds) * .5)

        if values[middleIndex] < target:
            floorBounds = middleIndex + 1

        elif values[middleIndex] > target:
            roofBounds = middleIndex - 1

        else:
            targetIndex = middleIndex
            return targetIndex

    return targetIndex
    

def main():
    values = generateList(sizeOfList)

    # Target value.
    targetValue = random.randint(0, sizeOfList - 1)
    targetValue = values[targetValue]

    pastTime = time.time()
    index = binarySearch(values, targetValue)
    currentTime = time.time()

    print("Target Value: " + str(targetValue))
    print("Index: " + str(index))
    print("Value at Index: " + str(values[index]))
    print("Size of List: " + str(sizeOfList))

    print("Completion Time: " + str(currentTime - pastTime) + "(s)")

# Run the application.
if __name__ == '__main__':
    main()