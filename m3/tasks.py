""" Вікторина з одним повтором """

def question(q, right_answer):
    a=input(q).lower()
    if a==right_answer.lower():
        print("Вірно!")
    else:
        print("Не вірно!")
    

question("Столиця України? ", "Київ")
question("Найшвидша тварина у світі? ", "Гепард")

"""Вікторина з безліччю повторів"""

def question2(q, right_answer):
  a=""
  while a.lower()!=right_answer.lower():
      a=input(q)
      if a.lower()!=right_answer.lower():
          print("Не вірно!")
  print("Вірно!")
  


question2("Столиця України? ", "Київ")
question2("Найшвидша тварина у світі? ", "Гепард")

"""Гральна кістка 1 - 6"""
from random import randint
# ваш код
def dice():
    a=randint(1,6)
    print("Я загадав число")
    b=0
    while b!=a:
        b=int(input("Вгадай число 1 - 6"))
        if a!=b:
            print("Не вгадав")
    print("Вгадав")
dice()

"""Камінь ножиці папір"""
from random import randint
# ваш код
def text(choice):
    if choice == 1:
        return  "камінь"
    elif choice == 2:
        return "ножиці"
    else:
        return "папір"

def paper_rock_scissors():
    computer_choice = random.randint(1, 3)

    print("Оберіть (введіть число):")
    print("1 - камінь, 2 - ножиці, 3 - папір")
    user_choice = int(input("Ваш вибір: "))

    user_choice_name=text(user_choice)
    computer_choice_name=text(computer_choice)

    print(f"Ви обрали: {user_choice_name}")
    print(f"Комп’ютер обрав: {computer_choice_name}")

    if user_choice == computer_choice:
        print("Нічия!")
    elif ((user_choice == 1 and computer_choice == 2) or
            (user_choice == 2 and computer_choice == 3) or
            (user_choice == 3 and computer_choice == 1)):
        print("Ви перемогли!")
    else:
        print("Комп’ютер переміг!")
paper_rock_scissors()

"""Вгадування числа від 1 до 100 більше менше"""
from random import randint
from time import time
# ваш код
def guess_number():
    start=time()
    a=randint(1,100)
    print("Я загадав число від 1 до 100")
    b=0
    k=0
    while b!=a:
        b=int(input("Ваша відповідь"))
        if b>a:
            print("Ваше число більше!")
        if b<a:
            print("Ваше число менше!")
        k=k+1    
    finish=time()    
    print(f"Ви вгадали за {k} спроб/и і {finish-start:.1f} секунд!")
guess_number()

