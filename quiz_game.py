"""Небольшой квиз по кино"""


def new_game():

    gusses = []
    correct_gusses = 0
    question_num = 1

    for key in questions:
        print("``````````````````")
        print(key)
        for i in answers[question_num-1]:
            print(i)
        guss = input("Выберете ответ:").upper()
        while guss not in ["A", "B", "C", "D"]:
            guss = input("Нет такого ответа\nВыберете ответ снова:").upper()

        gusses.append(guss)

        correct_gusses = check_answer(questions.get(key), guss)
        question_num += 1

    display_score(correct_gusses, gusses)


def check_answer(answer, guss):

    if answer == guss:
        print("Верно!")
        return 1
    else:
        print("Не верный ответ!")
        return 0


def display_score(correct_guesses, guesses):
    print("``````````````````")
    print("Результат")
    print("``````````````````")

    print("Верные ответы: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Ваши ответы:   ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int(correct_guesses/len(questions)*100)
    print("Ваш счет: ", score, "%")


def play_again():
    res = input("Вы хотите ответить снова? (yes/no): ").upper()
    if res == "YES":
        return True
    else:
        return False


questions = {
    "1. За какое время перед нами проходят двадцать четыре кадра кинопленки?": "B",
    "2. Назовите имя режиссера-постановщика фильма «Звездные войны»?": "A",
    "3. Каким был первый цветной фильм ужасов?": "D",
    "4. Какой цвет присутствует почти в каждом кадре «Сияния»?": "B",
    "5. В каком фильме мы видим старшеклассницу (Дрю Бэрримор),\n которая получает все более угрожающие телефонные звонки?": "C"
}

answers = [
    ["А. За 3 секунды", "B. За 1 секунду", "C. За 5 секунд", "D. За 10 секунд"],
    ["А. Джордж Лукас", "B. Робби Райан", "C. Джек Кардифф", "D. Федон Папамайкл"],
    ["А. Злобный санта", "B. Тайна музея восковых фигур",
        "C. Дом дьявола", "D. Проклятие Франкенштейна"],
    ["А. Желеный", "B. Красный", "C. Желтый", "D. Синий"],
    ["А. Ядовитый плющ ", "B. Безумная любовь", "C. Орать", "D. Зеркало"]
]

new_game()
while play_again():
    new_game()
