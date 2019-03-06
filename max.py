# [ ] -> None
# [1] -> 1, базовый
# [1, 2] -> 2, базовый
# [1, 2, 3] -> 3, рекурсивный

def maxInList(list):
    if len(list) == 2:
        return max(list[0], list[1])

    return max(list[0], maxInList(list[1:]))

print(maxInList([4, 1, 67, 23, 100]))