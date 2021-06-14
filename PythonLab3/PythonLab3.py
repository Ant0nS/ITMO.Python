import math
import numpy
import random as ran
import statistics as stat
#print(help(math))
#print(dir(math))

list = []
i = 0
while i < 10:
    k = ran.randint(1,100)
    list.append(k)
    i += 1
print(list)
print("Сумма цифр: ", math.fsum(list))
print("Среднее: ", stat.mean(list))
print("Медиана: ", stat.median(list))
print("Стандартное отклонение: ", stat.stdev(list))



print("Случайное целое число в промежутке от 1 до 100: ", ran.randint(1,100))
