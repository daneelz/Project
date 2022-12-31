vopros = ["Вы хотите начать игру?", "Вы играли раньше в нее?"]
sp = [0, 0]
for i in range(len(vopros)):
    while True:
        print(f"Укажите ответ на вопрос: {vopros[i]}")
        user_input = input().lower
        if user_input == "да":
            sp[i] = user_input
            break
        elif user_input == "нет":
            print("Нам очень жаль(")
            break
        else:
            print("Некоректный ввод")

ob = 30
user_name = input("Как вас зовут? ")
print("У вас всего 30 очков для создания своей характеристике")

health = int(input("\nВведите ваше здоровье (от 1 до 30 и не забудь оставить очки еще на 3 пункта): "))
while health < 1 or health > 30:
    print("У вас не осталось очков, введите число поменьше!")
    health = int(input("Введите верное число: "))
    continue

print(f"У вас осталось очков - {ob - health}")

streight = int(input(f"\nВведите вашу силу (от 1 до {ob - health} и не забудь оставить очки еще на 2 пункта): "))

'''if streight >= 1 and streight <= ob - health:
    print(f"У вас осталось очков - {ob - health - streight}")
elif ob - health - streight <= 0:
    print("У вас закончились очки, перезапустите программу.")
    exit()
else:
    print(f"Неверное число, перезапустите программу.")
    exit()'''

while streight < 1 or streight > ob - health:
    print("У вас не осталось очков, введите число поменьше!")
    streight = int(input("Введите верное число: "))
    continue

print(f"У вас осталось очков - {ob - health - streight}")

intelekt = int(
    input(f"\nВведите ваш интелект (от 1 до {ob - health - streight} и не забудь оставить очки еще на 3 пункта): "))
'''if intelekt >= 1 and intelekt <= ob - health - streight:
    print(f"У вас осталось очков - {ob - health - streight - intelekt}")
elif ob - health - streight - intelekt <= 0:
    print("У вас закончились очки, перезапустите программу.")
    exit()
else:
    print(f"Неверное число, перезапустите программу.")
    exit()'''
while intelekt < 1 or intelekt > ob - health - streight:
    print("У вас не осталось очков, введите число поменьше!")
    intelekt = int(input("Введите верное число: "))
    continue
print(f"У вас осталось очков - {ob - health - streight - intelekt}")

superstreight = int(input(f"\nВведите вашу суперсилу (от 1 до {ob - health - streight - intelekt}): "))
'''if superstreight >= 1 and superstreight <= ob - health - streight:
    print(f"У вас осталось очков - {ob - health - streight - intelekt - superstreight}")
elif ob - health - streight - intelekt - superstreight <= 0:
    print("У вас закончились очки, перезапустите программу.")
    exit()
else:
    print(f"Неверное число, перезапустите программу.")
    exit()'''

while superstreight < 1 or superstreight > ob - health - streight - intelekt:
    print("У вас не осталось очков, введите число поменьше!")
    intelekt = int(input("Введите верное число: "))
    continue

print(f"У вас осталось очков - {ob - health - streight - intelekt - superstreight}")

print(f"\n{user_name}, вы со всем справились! \n"
      f"Вот ваша характеристика:")
print(f"здоровье\tсила\tинтелект\tсуперсила\n"
      f"{health}\t\t\t{streight}\t\t\t{intelekt}\t\t\t{superstreight}")

answer = input("\nПродолжим? Да/Нет: ").lower()
if answer == "да":
    print(f"Ваш герой идет по улице и на него нападают бандиты! (--Какой ужас--)")
    if streight >= 5:
        print(
            f"Ваш герой победил в этой схватке, потому что его сила = {streight}, он пошел домой и хочет включить телевизор!")
        if intelekt >= 7 and intelekt <= 30:
            print(f"Ваш герой включил телевизор, потому что его интелект {intelekt} единиц опыта")
            exit()
        elif intelekt < 7:
            print(
                f"Ваш герой не смог включить телевизор и лег спать без него, потому что его интелект = {intelekt} единиц!\n"
                f"Ваш герой грустный! Игра завершена!")
        exit()
    elif streight < 5:
        print(f"Ваш герой проиграл в этой схватке и попал в больницу, потому что его сила = {streight}")
        answer1 = input(
            "Вы хотите выбраться из больницы? Если не выберетесь, то останетесь здесь навсегда! Ваш ответ да/нет: ").lower()
        if answer1 == "да":
            if health >= 5 and health <= 30:
                print(f"Вы успешно выбрались из больницы, потому что у вашего героя {health} единиц здоровья!")
                answer2 = ("Вы видите женщину на которую напали бандиты! ОХ-НЕТ!!! Вы хотите ей помочь? да/нет: ").lower
                if answer2 == "да":
                    print(f"Вы успешно спасли девушку, потому что ваша суперсила равна {superstreight} единиц!\n"
                          f"Вы успешно окончили игру! Хорошего дня!")
                elif answer2 == "нет":
                    print("Вы не спасли девушку, она скорее всего погибла(((\n"
                          "Игра завершена! До свидания!")
                else:
                    print("Неверный ввод, начните игру заново!")
            if health <= 5:
                print(f"Вы не смогли выбраться из больницы, потому что у вашего героя {health} единиц здоровья!\n"
                      f"Попробуйте начать игру заново!")
                exit()
        elif answer1 == "нет":
            print("Вы не выбрались из больницы( Вы погибли!")
            exit()
elif answer == "нет":
    print("Ну как хотите:( Пока!")
    exit()
else:
    print("Неверный ввод! Начните игру заново!")
