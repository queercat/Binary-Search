# Used for random number generation for the list.
import random
import math
import time

# Constant value for the size of the list.
sizeOfList = pow(10, 1)

# Constant value for the size of the numbers in the list.
listRange = pow(100, 2)

# generateList ... Returns a sorted list of n elements.
def generateList(n):
    values = []
    for val in range(0, n):
        values.append(random.randint(0, listRange))

    values.sort()
    return values

# binarySearch ... Search list values for target using a the binary search algorithm.
def binarySearch(values, target, debug=False):
    floorBounds = 0
    roofBounds = sizeOfList - 1   

    if (debug):
        print("Target Value: " + str(target))

    while (floorBounds <= roofBounds):
        middleIndex = math.floor((floorBounds + roofBounds) / 2)

        if (debug):
            print("Middle Index: " + str(middleIndex))
            print("Value: " + str(values[middleIndex]))

        if values[middleIndex] < target:
            floorBounds = middleIndex + 1

            if (debug):
                print("Less than target!")

        elif values[middleIndex] > target:
            roofBounds = middleIndex - 1

            if (debug):
                print("Greater than target!")

        elif values[middleIndex] == target:
            return middleIndex

    return -1
    

def main():
    values = generateList(sizeOfList)

    # Target value.
    targetValue = random.randint(0, sizeOfList - 1)
    targetValue = values[targetValue]

    pastTime = time.time()
    index = binarySearch(values, targetValue)
    currentTime = time.time()

    if index == -1:
        print(values)
        binarySearch(values, targetValue, True)

    print("Target Value: " + str(targetValue))
    print("Index: " + str(index))
    print("Value at Index: " + str(values[index]))
    print("Size of List: " + str(sizeOfList))

    print("Completion Time: " + str(currentTime - pastTime) + "(s)")

# Run the application.
if __name__ == '__main__':
    main()