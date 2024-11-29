def calc():
    chislo1 = float(input('Введите первое число: '))
    chislo2 = float(input('Введите второе число: '))
    print()
    result = chislo1 + chislo2
    print(f'Результат сложения: {result}')
    result = chislo1 - chislo2 
    print(f'Результат вычитания: {result}')
    result = chislo1 * chislo2
    print(f'Результат умножения: {result}')
    if chislo2 != 0:
        result = chislo1 % chislo2
        print(f'Результат деления: {result}')
    else:
        print()
        print('На ноль делить нельзя')
        chislo2 = float(input('Введите второе число: '))
        result = chislo1 % chislo2
        print()
        print(f'Результат деления: {result}')
calc()