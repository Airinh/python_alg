# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.

import random


m = 16
list_1 = [random.randrange(0, 100) for _ in range(2 * m + 1)]
print(list_1)


def median_square(array):
    for i in range(len(array)):
        smaller = bigger = 0
        equal = - 1
        for j in range(len(array)):
            if array[i] < array[j]:
                smaller += 1
            elif array[i] > array[j]:
                bigger += 1
            else:
                equal += 1
        if smaller == bigger or smaller == equal + bigger or bigger == equal + smaller or abs(bigger - smaller) < equal and equal > 1:
            return array[i]


print(f'медина = {median_square(list_1)}')
