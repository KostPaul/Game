import random
import codecs, sys
from sys import exit


def start():
    print("""
    Ты находишься в комнате с четырьмя дверьми.
    На первой двери табличка с надписью "Алгебра".
    На в торой с надписью "Геометрия".
    На третей "Статистика".
    На четвёртой "Выход", но дверь закрыта.
    Что бы открыть последнию дверь, нужно пройти все предыдущие.
    С какой начнёшь?
    """)
    x = int(input('> '))

    if x == 1:
        algebra()
    elif x == 2:
        geometry()
    elif x == 3:
        statistics()
    elif x == 4:
        if room4 == True:
            room4()
        else:
            print('Дверь заперта. Осмотри предыдущие комнаты!')
    else:
        start()

def algebra():
    print('Тебе предстоит решить задачу, что бы выйти!')
    x = random.randint(1,3)
    if x == 1:
        print('Корень из 225?')
        z = int(input('> '))
        if z == 15:
            print('Верно!')
            key_algebra = True
            return key_algebra
            start()
        else:
            print('Нет!')
            algebra()
    elif x == 2:
        print('7 в кубе?')
        z = int(input('> '))
        if z == 343:
            print('Верно!')
            key_algebra = True
            return key_algebra
            start()
        else:
            print('Нет!')
            algebra()
    else:
        print("""47 * 9 = x
        """)
        z = int(input('> '))
        if z == 423:
            print('Верно!')
            key_algebra = True
            return key_algebra
            start()
        else:
            print('Нет!')
            algebra()

def geometry():
    pass
def statistics():
    pass
def room4():
    pass

key_algebra = None
key_geometry = None
key_statistics = None
key_room4 = key_algebra and key_geometry and key_statistics

start()

print(key_algebra)
