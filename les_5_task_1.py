# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Company = namedtuple('Company', ['name', 'profit'])
companies = set()

num_comp = int(input("Количество предприятий: "))
tot_profit = 0
for i in range(1, num_comp + 1):
    profit = 0
    name = input(f'\nНазвание {i}-го предприятия : ')
    for j in range(4):
        profit += float(input(f'Прибыль за {j + 1}-й квартал: '))
    comp = Company(name=name, profit=profit)
    companies.add(comp)
    tot_profit += profit
average = tot_profit / num_comp
print(f'\nСредняя прибыль предприятия за год- {average:.2f}')

print(f'\nПредприятия с прибылью выше среднего:')
for comp in companies:
    if comp.profit > average:
        print(f'{comp.name} (прибыль за год - {comp.profit})')
print(f'\nПредприятя с прибылью ниже среднего:')
for comp in companies:
    if comp.profit < average:
        print(f'{comp.name} (прибыль за год - {comp.profit})')
