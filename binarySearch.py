# дан массив чисел
data = [1, 3, 5, 7, 9, 10, 11, 24, 17, 20]
#       0  1  2  3  4  5   6   7   8   9

# написать бинарный поиск нахождения позиции элемента в листе
# если в листе нет, вернуть null
# input : list, item
# output: position (null)

# бинарный поиск работает следующим образом:
# вычисляем общую длину листа, low = 0, high = len(list)
# -> находим mid индекс (high - low) // 2
# сравниваем item с list[mid]
# если item равен list[mid], возвращаем mid
# если item < list[mid], присваиваем high = mid - 1
# если item > list[mid], присваиваем low = mid + 1
# <- возврат с новыми значениями low и high, пока low != high

def lowMidHigh(low, mid, high):
    print("low:", low, "mid", mid, "high:", high, "\n")

def binarySearch(list, item):
    low  = 0
    high = len(list) - 1

    while (low <= high):
        mid = (high + low) // 2

        lowMidHigh(low, mid, high)

        if  (item == list[mid]):
            return mid
        elif (item < list[mid]):
            high = mid - 1
        else:
            low = mid + 1

    return None

print(binarySearch(data, 11))