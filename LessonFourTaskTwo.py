import random

my_list = []
new_list = []

for i in range(4):
    my_list.append(random.randint(1, 100))
print(my_list)

new_list = my_list + new_list

for element in my_list:
    new_list.append(element * 2)
print(new_list)
