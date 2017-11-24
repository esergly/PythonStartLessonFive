grad = int(input('На 90,180 или 270 градусов повернуть исходную матрицу? Введите значение: \n'))
my_list = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6]]
print('Исходная матрица: ')
for element in my_list:
    print(element)
repeat = 0
if grad == 90:
   repeat = 1
if grad == 180:
   repeat = 2
if grad == 270:
   repeat = 3
if repeat == 0:
   print('К сожалению поворот возможен только на 90, 180 или 270 градусов.')

# Переводим значения столбцов в строчки
else:
    print('Матрица повёрнута по часовой стрелке на ' + str(grad) + ' градусов: ')
    i = 0
    j = 0
    k = 0
    x = 0
    size = len(my_list)

    for i in range(repeat):
        for i in range(size):
            for j in range(size):
                a = my_list[j][i]
                my_list.append(a)

# Удаляем исходные исходные списки
        for k in range(size):
            n = 0
            del (my_list[n])

# Собираем новые списки по срезам
        for x in range(size):
            my_list[x] = my_list[x:x+size]
            my_list[x].reverse()
            for i in range(size-1):
                i = x+1
                del (my_list[i])

    for element in my_list:
        print(element)
