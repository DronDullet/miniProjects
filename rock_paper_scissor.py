# Игра "камень", "ножницы", "бумага"
import random

choise_list = ["камень", "ножницы", "бумага"]

computer = random.choice(choise_list)
player = input('Сделай выбор из "камень", "ножницы", "бумага": ').lower()
while player not in choise_list:
    print("Этого в списке нет, сделай правильный выбор!")
    player = input('Сделай выбор из "камень", "ножницы", "бумага": ').lower()
    print(player)

print("Компьютер выбрал:", computer)
print("Ты выбрал :", player)
