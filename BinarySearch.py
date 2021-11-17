import numpy as np
def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -2

availableList = [int(x) for x in input("Enter available no:").split()]
array = np.array(availableList)
searchList = [int(x) for x in input("Enter to search:").split()]

resultList = []
for x in searchList:
    resultList.append(binarySearch(array, x, 0, len(array)-1)+1)

for x in resultList:
    print(x, end=' ')
