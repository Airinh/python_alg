import timeit
import cProfile

HOLE = 0


def prime_number_1(d):
    size = d ** 2 + 3
    array = [i for i in range(size)]
    array[1] = HOLE
    for i in range(2, size):
        if array[i] != HOLE:
            j = i ** 2
            while j < size:
                array[j] = HOLE
                j += i
    res = [i for i in array if i != HOLE]
    return res[d - 1]


def prime_number_2(d):
    k = 1
    num = 2
    while k < d:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            k += 1
    return num


print('\nТест prime_number_1:')
print(timeit.timeit('prime_number_1(5)', number=1000, globals=globals()))   # 0.009339
print(timeit.timeit('prime_number_1(50)', number=1000, globals=globals()))  # 0.7781855
print(timeit.timeit('prime_number_1(100)', number=1000, globals=globals())) # 2.9829236
cProfile.run('prime_number_1(100)')

print('\nТест prime_number_2:')
print(timeit.timeit('prime_number_2(5)', number=1000, globals=globals()))   # 0.004108499999999626
print(timeit.timeit('prime_number_2(50)', number=1000, globals=globals()))  # 0.2894543000000005
print(timeit.timeit('prime_number_2(100)', number=1000, globals=globals())) # 1.2305558000000003
cProfile.run('prime_number_2(100)')

# Вывод: Получилось, что алгоритм с Решетом Эратосфена работает медленнее,
# делает больше операций и они больше по длительности.