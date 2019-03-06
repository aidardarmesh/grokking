def findSmallestIndex(arr):
    smallest      = arr[0]
    smallestIndex = 0
    lenArr        = len(arr)

    for i in range(1, lenArr):
        if (arr[i] < smallest):
            smallest      = arr[i]
            smallestIndex = i

    return smallestIndex

def selectionSort(arr):
    newArr = []
    lenArr = len(arr)

    for i in range(0, lenArr):
        smallestIndex = findSmallestIndex(arr)
        newArr.append(arr.pop(smallestIndex))

    return newArr

print(selectionSort([5, 2, 7, 3, 9, 10]))