# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11

print('Задание 1')

number = input('Введите число ')
if float(number) < 0:
    number = float(number) * (-1)
summ = 0
for n in number:
    if n != '.':
        summ += int(n)
print(f'Сумма цифр введенного числа = {summ}')
