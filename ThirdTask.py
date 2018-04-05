import random
from collections import Counter

"""
   Implement random dice roll without using `random` python module.
   The only one source which you can use for random numbers is the `flip` function.
   Should return dice face number (1 to 6)
"""


def flip():
    return random.randint(0, 1)



'''Solution of the Third task'''
def dice_roll():

     probably_combination = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (0, 0, 0)]  #  создадим 6 возможных(любых) комбинаций из цифр (1.0) подрозумевая, что
                                                                                                #  индексами массива будут наши числа от 1 до 6
     rand_number = (flip(),flip(),flip())                                                       #  генерируем кортеж возможной комбинации чисел
                                                                                                #
     if  rand_number in probably_combination:                                                   #  проверяем ее наличие в списке наших вариантов, если True то
         return probably_combination.index(rand_number)+1                                       #  возвращаем индекс массива +1, потому что индексирование идет с нуля
     else:                                                                                      #
        return dice_roll()                                                                      #  если False, то повторяем процедуру во избежание получения пустых значений
                                                                                                #  в случае когда  rand_number не входит в наш список возможных значний

print(dice_roll())  # should return from 1 to 6
#thousand_rolls = Counter([dice_roll() for _ in range(1000)])