# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random


def sort_bubble(array):
    for i in range(len(array) - 1):
        test = 1
        for j in range(len(array) - 1 - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                test = 0
        if test:
            break
    return array


list_1 = [random.randrange(-100, 100) for _ in range(21)]
print(list_1)

print(sort_bubble(list_1))

