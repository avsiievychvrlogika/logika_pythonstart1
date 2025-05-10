import time, random
# вгадай число
def guess_number():
    print("Вгадай число від 1 до 100")
    number = random.randint(1, 100)
    attempts = 0
    game = True
    while game:
        answer = int(input("Ваше число: "))
        attempts += 1
        if answer < number:
            print("Моє число більше!")
        elif answer > number:
            print("Моє число менше!")
        else:
            game = False

    print(f"Вітаємо!")
    print(f"Використано {attempts} спроб!")

# гральні кості

def dice():
    print("Вгадай число, що випало (від 1 до 6)")
    while True:
        number = random.randint(1, 6)
        answer = int(input("Ваша відповідь: "))
        if number == answer:
            break
        else:
            print("Не вгадали, спробуйте ще! ")

    print(f"Вітаємо! Гру пройдено!")

# дата та час
def time_part():
    print("Час зараз: ")
    print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime()))


while True:
    print("1 - Гральні кості: ")
    print("2 - Вгадай число: ")
    print("3 - Дата та час: ")
    variant = input("Введіть тип опитування (1 - 3): ")
    if variant == "1":
        dice()
    elif variant == "2":
        guess_number()
    elif variant == "3":
        time_part()

    q = input("Чи бажаєте ви вийти? (y = True): ")
    if q.lower() == "y":
        break