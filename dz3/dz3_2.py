# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] = > [12, 15, 16]
# - [2, 3, 5, 6] = > [12, 15]


lst = input()

if lst == '1':
    lst = [2, 3, 4, 5, 6]
else:
    lst = [2, 3, 5, 6]

temp = (len(lst) + 1) // 2

newlst = []

for i in range(temp):
    newlst.append(lst[i] * lst[-i - 1])
print(newlst)