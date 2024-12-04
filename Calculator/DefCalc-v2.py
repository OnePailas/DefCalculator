chs1 = float(input('Введите первое число: '))
chs2 = float(input('Введите второе число: '))
print(f'Результат сложения: {chs1 + chs2} \nРезультат вычитания: {chs1 - chs2} \nРезультат умножения: {chs1 * chs2}') 
if chs2 == 0:
    chs2 = float(input('Введите еще раз второе число: '))
    print(f'Результат деления: {chs1 / chs2}')
else:
    print(f'Результат деления: {chs1 / chs2}')