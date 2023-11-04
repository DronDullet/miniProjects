# Игра "камень", "ножницы", "бумага"
import random

choise_list = ["камень", "ножницы", "бумага"]

computer = random.choice(choise_list)
player = input('Сделай выбор из "камень", "ножницы", "бумага": ').lower()
while player not in choise_list:
    print("Этого в списке нет, сделай правильный выбор!")
    player = input('Сделай выбор из "камень", "ножницы", "бумага": ').lower()
    print(player)


if player == computer:
    print("Компьютер выбрал:", computer)
    print("Ты выбрал :", player)
    print("Ничья!")
elif player == "камень":
    if computer == "ножницы":
        print("Компьютер выбрал:", computer)
        print("Ты выбрал :", player)
        print("Вы выиграли!")
    elif computer == "бумага":
        print("Компьютер выбрал:", computer)
        print("Ты выбрал :", player)
        print("Вы проиграли!")

elif player == "ножницы":
    if computer == "бумага":
        print("Компьютер выбрал:", computer)
        print("Ты выбрал :", player)
        print("Вы выиграли!")
    elif computer == "камень":
        print("Компьютер выбрал:", computer)
        print("Ты выбрал :", player)
        print("Вы проиграли!")

elif player == "бумага":
    if computer == "камень":
        print("Компьютер выбрал:", computer)
        print("Ты выбрал :", player)
        print("Вы выиграли!")
    elif computer == "ножницы":
        print("Компьютер выбрал:", computer)
        print("Ты выбрал :", player)
        print("Вы проиграли!")
