# Вариант 1
my_list = [7, 2, 9, 4]
my_list.reverse()
print(my_list)
# вывод: [4, 9, 2, 7]

# Вариант 2
my_list = [7, 2, 9, 4]
size = len(my_list)
for i in range(size):
    my_list.append(my_list[(size-1)-i])
print(my_list)
# вывод: [7, 2, 9, 4, 4, 9, 2, 7]
