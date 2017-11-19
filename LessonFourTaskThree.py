import random

salary = []

for i in range(12):
    salary.append(random.randint(7500, 15000))
print(salary)

average = 0
for element in salary:
    average = average + element
print(average / len(salary))
