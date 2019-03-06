# [1] -> если item = 1, элемент найден, базовый случай
# [2] -> но item также 1, элемента в массиве нет

def binSearchRec(list, item):
    low  = 0
    high = len(list)-1
    mid  = (low + high) // 2

    print("low: ", low, "mid: ", mid, "high: ", high)

    if item == list[mid]:
        return mid
    elif item < list[mid]:
        return binSearchRec(list[:mid], item)
    elif item > list[mid]:
        return binSearchRec(list[mid+1:], item) + (mid + 1)

list = [1, 3, 5, 7, 9, 14, 17]

print(binSearchRec(list, 14))