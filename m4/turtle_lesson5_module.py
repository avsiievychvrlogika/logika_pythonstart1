#функція write_right
def write_right(letter):
    start(-170, 105)
    penup()
    color("black")
    setheading(0)
    count = 0
    for w in word:
        if w == letter:
            pendown()
            write(letter,font=("Arial",32))
            penup()
            count += 1
        fd(45)
    return count

#функція write_wrong
def write_wrong(letter):
    color("black")
    write(letter, font=("Arial",28))
    color("red")
    width(2)
    setheading(45)
    fd(30)
    setheading(180)
    penup()
    fd(20)
    setheading(270+45)
    pendown()
    fd(30)
    color("grey")
def end_game(col,txt):
    start(-50,-50)
    color(col)
    write(txt, font=("Arila",50))