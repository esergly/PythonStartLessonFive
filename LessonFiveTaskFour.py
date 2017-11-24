my_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
count = 0
i = 0
j = 0
for element in my_list:
    print(element)
for i in range(4):
    for j in range(4):
        count = count + my_list[i][j]
print('Сумма всех элементов списка списков равна ' + str(count))
