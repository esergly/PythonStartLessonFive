grad = int(input('На 90,180 или 270 градусов повернуть исходную матрицу? Введите значение: '))
my_list = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6]]
print('Исходная матрица: ')
for element in my_list:
    print(element)
i = 0
repeat = 0
if grad == 90:
   repeat = 1
if grad == 180:
   repeat = 2
if grad == 270:
   repeat = 3
if repeat == 0:
   print('К сожалению поворот возможен только на 90, 180 или 270 градусов.')

# Вариант с красивой логикой переворота
else:
   print('Матрица повёрнута по часовой стрелке на ' + str(grad) + ' градусов: ')
   for i in range(repeat):
       my_list = tuple(zip(*my_list[::-1]))
for element in my_list:
    print(element)

'''
That's a clever bit. Here's the breakdown:

[::-1] - makes a shallow copy of the original list in reverse order. Could also use reversed() which would produce a reverse iterator over the list rather than actually copying the list (more memory efficient).
* - makes each sublist in the original list a separate argument to zip() (i.e., unpacks the list)
zip() - takes one item from each argument and makes a list (well, a tuple) from those, and repeats until all the sublists are exhausted. This is where the transposition actually happens.

So assuming you have this:
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]

You first get this (shallow, reversed copy):
[ [7, 8, 9],
  [4, 5, 6],
  [1, 2, 3] ]

Next each of the sublists is passed as an argument to zip:
zip([7, 8, 9], [4, 5, 6], [1, 2, 3])
zip() repeatedly consumes one item from the beginning of each of its arguments and makes a tuple from it, until there are no more items, resulting in:

[(7, 4, 1), 
 (8, 5, 2), 
 (9, 6, 3)]  

To answer question about rotating it in the other direction, 
it's pretty straightforward: you just need to reverse both the sequences 
that go into zip and the result. The first can be achieved 
by removing the [::-1] and the second can be achieved by 
throwing a reversed() around the whole thing. Since reversed() 
returns an iterator over the list, we will need to put 
list() around that to convert it. So:

rotated = list(reversed(zip(*original)))  
'''
