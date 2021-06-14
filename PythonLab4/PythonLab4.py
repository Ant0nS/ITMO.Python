from random import randint
import time

#Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего: ')
igrok2 = input('Введите имя 2-го играющего: ')
score1 = 0
score2 = 0


#Моделирование бросания кубика первым играющим
for i in range(5):
    print('Кубик бросает ', igrok1)
    time.sleep(1)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    score1 +=n1

#Моделирование бросания кубика вторым играющим
for i in range(5):
    print('Кубик бросает ', igrok2)
    time.sleep(1)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    score2 += n2

#Определение результата (3 возможных варианта)
if score1 > score2:
    print('Выиграл', igrok1, ' с количеством очков', score1, ' против ', igrok2, ' c ', score2, ' очков.')
elif score1 < score2:
    print('Выиграл', igrok2, ' с количеством очков', score2, ' против ', igrok1, ' c ', score1, ' очков.')
else:
    print('Ничья')
