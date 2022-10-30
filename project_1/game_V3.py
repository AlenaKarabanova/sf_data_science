"""Игра угадай число.
Компьютер сам загадывает и угадывает число. Максимальное количество попыток 20
"""
from this import s
from turtle import right
import numpy as np
def random_predict(number:int=1) -> int:
    """Угадываем число через алгоритм

    Args:
        number(int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left_n = 1
    right_n = 101
    while True:
        count += 1
        predict_number = (left_n + right_n)//2#предполагаемое число
        if predict_number > number:
            right_n = predict_number
        elif predict_number < number: 
            left_n = predict_number
        else:
            break#конец игры, выход из цикла
    return(count)
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101,size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) #Находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
print(f'Количество попыток:{random_predict()}')

# RUN

if __name__ == '__main__':
    score_game(random_predict)
