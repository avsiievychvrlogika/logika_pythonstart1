#функція draw_petal
def draw_petal(col, radius):
    color(col)
    begin_fill()
    circle(radius, 60)  # Півколо
    left(120)  # Поворот для іншої сторони
    circle(radius, 60)  # Півколо
    end_fill()
#функція draw_stem
def draw_stem():
    start(x_start,y_start)
    setheading(90)
    color("green")
    width(20)
    # перша частина ствобувра
    fd(50)
    #розвернути вліво та малювати листочок
    setheading(135)
    draw_petal("green",100)
    #розвернути вправо та малювати листочок
    setheading(25)
    draw_petal("green",65)
    # друга частина стовбура
    setheading(90)
    fd(150)
#функція draw_petals
def draw_petals():    
    # Малювання квітки
    width(20)
    k = starting_angle
    for i in range(7):
        start(x_start,y_start+200)
        setheading(k)
        draw_petal(colors[i], r)
        k += starting_angle
#функція draw_down_petal
def draw_down_petal(col):
    draw_flower()
    xd = randint(x_start-50,x_start+50)
    start(xd,y_start)
    h = randint(180,360)
    setheading(h)
    width(20)
    draw_petal(col, r)
    
def draw_flower():
    draw_stem()
    draw_petals()
#функція write_ask
def write_ask(word):
    start(-170, 100)
    setheading(0)
    width(4)
    color("black")
    for w in word:
        fd(30)
        penup()
        fd(15)
        pendown()
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