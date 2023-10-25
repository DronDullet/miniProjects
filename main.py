"""код игры "Угадай число"
игра для двоих игроков, программа загадывает число, а игроки его должны угадать
угадывая по очереди.
1. Длина числа должна задаваться.
2. При не верном ответе должна выдавать больше число или меньше.
"""
# импортируем модуль рандом
import random

print("Добро пожаловть в игру /// 'Угадай число'")
print("ver 0.0")
print("Игра предназначена для двойх игроков.")


# name_player_one = input("Введите имя первого игрока: ")
name_player_one = "Sam"
# name_player_two = input("Введите имя второго игрока: ")
name_player_two = "Din"

# Добавил проверку на не правлиьную длину числа
long_number = int(input("Введите длину числа: "))
if long_number <= 0:
    print("Не верная длина числа!")
    long_number = int(input("Введите  новую длину числа: "))
# генератор числа c регулируемой длиной числа
win_number = random.randint(0, 10**long_number-1)
print(win_number)


'''def win(num_one, num_two):
    if num_one == num_two:
        return True
    else:
        if num_one > num_two:
            return "Число большее =)"
        else:
            return "Число меньше =)"'''


# цикл игры
game = True
step = 1
while game:
    if step == 1:
        print(f"Число угадывает {name_player_one}!")
        number = int(input("И ваше число: "))
        if win_number == number:
            print(f"{name_player_one} вы выйграли!!! угадав число {number}")
            game = False
        else:
            step += 1
    else:
        print(f"Число угадывает {name_player_two}!")
        number = int(input("И ваше число: "))
        if win_number == number:
            print(f"{name_player_two} вы выйграли!!! угадав число {number}")
            game = False
        else:
            step -= 1
