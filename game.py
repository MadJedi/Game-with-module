#Простейшая игра, демонстрация импорта модуля игры
import gamemodule, random

print("Вас приветствует самая простая игра на свете!!!\n")

again = None
while again != "n":
    players = []
    num = gamemodule.ask_number(question = "Сколько будет игроков? (2-5): ", low = 2, \
                           high = 5)
    for i in range(num):
        name = input("Имя игрока: ")
        score = random.randrange(100) + 1
        player = gamemodule.Player(name, score)
        players.append(player)

    print("\Результаты игры:")
    for player in players:
        print(player)

    again = gamemodule.ask_yes_no("\nЖелаете сыграть ещё раз? (y/n): ")

input("\n\nНажмите Enter чтобы выйти.")
