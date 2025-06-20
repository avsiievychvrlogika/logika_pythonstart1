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