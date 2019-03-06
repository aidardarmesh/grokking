# определяем базовый случай
# [ ] -> 0 базовый
# [1] -> 1 рекурсивный

def count(list):
    if list == []:
        return 0

    return 1 + count(list[1:])

print(count([1, 22, 3, 45, 3, 4, 5, 8]))