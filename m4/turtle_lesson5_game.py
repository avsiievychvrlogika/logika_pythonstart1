#підключи усі необхідін молулі
from art import *
from guess_word import *
from random import *
# Список кольорів пелюсток
colors = ["#c0392b", "#8e44ad", "#2471a3", "#138d75", "#f1c40f","#e74c3c","#5dade2"]

# координати квітки
x_start,y_start = 400,-150
# координати завдання
x_ask,y_ask = -170,100
# координати для відображення невірних літер
x_wrong, y_wrong = -170, 50

# радіус пелюстки та листочків
r = 95
# стартовий кут для пелюсток квітки
starting_angle = 360/7

# лічильники вірних та невірних слів
count_right = 0
count_wrong = 0


speed(0)
# список слів для гри
words = ["привіт","пока","прощавай"]
# випадкове слово для старту гри
word = choice(words)

# малюємо квітку 
draw_flower()
# малюємо завдання
write_ask(word)

# ігровий цикл
while True:
    letter = input("Введіть літеру:")
    if letter in word:
        c = write_right(letter)
        count_right += c
    else:
        start(x_wrong,y_wrong)
        x_wrong += 45
        write_wrong(letter)
        count_wrong += 1
        col = colors[count_wrong-1]
        colors[count_wrong-1] = "white"
        draw_down_petal(col)

    if count_wrong == 7:
        end_game("red","Ти програв :(")
        break
    if count_right == len(word):
        end_game("blue","Ти виграв!")
        break



