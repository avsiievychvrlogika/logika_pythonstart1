"""Сума кубиків більше 7 чи менше"""
import random

def dice_battle():
    guess = input("Сума буде більше 7 чи менше? (пиши 'більше' або 'менше'): ").lower()
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    print("Кубики:", d1, d2, "Сума:", total)
    if (total > 7 and guess == "більше") or (total < 7 and guess == "менше"):
        print("Вгадав!")
    else:
        print("Програв!")

#dice_battle()

"""Рандомне число більше або нижче за 50"""
import random

def high_low():
    guess = input("Число буде вище чи нижче за 50? ").lower()
    num = random.randint(1, 100)
    print("Число:", num)
    if (num > 50 and guess == "вище") or (num < 50 and guess == "нижче"):
        print("Вгадав!")
    else:
        print("Не вгадав.")

#high_low()

"""Число парне чи непарне"""
import random

def even_or_odd():
    guess = input("Вгадай: парне чи непарне? ").lower()
    number = random.randint(1, 100)
    print("Число:", number)
    if (number % 2 == 0 and guess == "парне") or (number % 2 == 1 and guess == "непарне"):
        print("Правильно! Ти виграв.")
    else:
        print("Програш.")

#even_or_odd()

"""Ставка з рандомним множником"""
import random

def random_multiplier():
    print("Ставка множиться на випадкове число від 0 до 5")
    bet = int(input("Введи ставку: "))
    multiplier = random.randint(0, 5)
    print("Випав множник:", multiplier)
    print("Виграш:", bet * multiplier)

#random_multiplier()

""" орел чи решка"""

def coin_toss():
    
    print("\n--- ГРА: МОНЕТКА ---")
    guess = input("Орел чи решка? ").lower()
    result = random.choice(["орел", "решка"])
    print("Випало:", result)
    if guess == result:
        print("Вгадав")
    else:
        print("не вгадав")
#coin_toss()
"""слоти"""
def choice(s1,s2,s3,s4):
    a=random.randint(1,4)
    if a==1:
        return s1
    elif a==2:
        return s2
    elif a==3:
        return s3
    elif a==4:
        return s4

def slot_machine():
    print("\n--- ГРА: СЛОТ МАШИНА ---")
    symbol1 = "🍒"
    symbol2="7"
    symbol3="⭐"
    symbol4="🍋"
    roll1=choice(symbol1,symbol2,symbol3,symbol4)
    roll2=choice(symbol1,symbol2,symbol3,symbol4)
    roll3=choice(symbol1,symbol2,symbol3,symbol4)
    print("Барабан:", roll1,roll2,roll3)
    
    if roll1 == roll2 == roll3:
        print("джекпот")
    elif roll1 == roll2 or roll2 == roll3 or roll1 == roll3:
        print("маленький виграш")
    else:
        print("нічого")
#slot_machine()
        
"""Рулетка"""

def roulette():

    print("\n--- ГРА: РУЛЕТКА ---")

    a=input("Рулетка по кольору чи числу(введи слово колір або число)").lower()
    if a=="колір":
        b=input("Червоне чи чорне чи зелене(введи слово)").lower()
        c=random.randint(1,3)
        col="червоне"
        if c==1:
            col="червоне"
        elif c==2:
            col="чорне"
        elif c==3:
            col="зелене"
        print(f"Комп'ютер загадав {col}")
        if b==col:
            print("Виграш")
        else:
            print("Програш")
    elif a=="число":
        b=int(input("Введи число"))
        c=random.randint(0,36)
        print(f"Комп'ютер загадав {c}")
        if c==b:
            print("Ви виграли")
        else:
            print("Ви програли")
roulette()
            
