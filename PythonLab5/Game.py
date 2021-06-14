from random import randint
import time

score1 = 0
score2 = 0


def inputName():
    gamer1 = input('Введите имя 1-го играющего: ')
    gamer2 = input('Введите имя 2-го играющего: ')
    return (gamer1, gamer2)


def startGame(gamer1, gamer2):
    # Моделирование бросания кубика первого игрока
    sum1 = 0
    for i in range(5):
        print('Кубик бросает', gamer1)
        time.sleep(1)
        n1 = randint(1, 6)
        print('Выпало: ', n1)
        sum1 += n1

    # Моделирование бросания кубика первого игрока
    print('________')
    sum2 = 0
    for i in range(5):
        print('Кубик бросает', gamer2)
        time.sleep(1)
        n2 = randint(1, 6)
        print('Выпало: ', n2)
        sum2 += n2

    print(getWinner(sum1, sum2, gamer1, gamer2))


def getWinner(score1, score2, gamer1, gamer2):
    print('_______')
    if score1 > score2:
        return ('Выиграл {0}, кол-во очков: {1}'.format(gamer1, score1))
    elif score1 < score2:
        return ('Выиграл {0}, кол-во очков: {1}'.format(gamer2, score2))
    else:
        return 'Ничья!'
