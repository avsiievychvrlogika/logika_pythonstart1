from turtle import *

speed(0)
screen = getscreen()
screen.bgcolor("black")

def go_xy(t, x, y):
    t.pu()
    t.goto(x,y)
    t.pd()

def draw_line(t, x1, y1, x2, y2, cl="green"):
    t.color(cl)
    go_xy(t, x1, y1)
    t.goto(x2, y2)

def draw_rect(t, x, y, w, h, fill=None):
    go_xy(t, x, y)
    if fill:
        t.color(fill)
        t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    if fill:
        t.end_fill()

def create_pen():
    pen = Turtle()
    pen.color("blue")
    pen.speed(0)
    pen.shape("circle")
    
    def on_key_left():
        ...

    def on_key_right():
        ...

    def on_key_up():
        pen.seth(90)
        pen.fd(10)

    def on_key_down():
        ...
       
    def set_red():
        pen.color("red")

    def set_green():
        pen.color("green")

    def set_blue():
        pen.color("blue")
    def set_white():
        pen.color("white")

    pen.set_red = set_red
    pen.set_green = set_green
    pen.set_blue = set_blue
    pen.set_white = set_white

    pen.on_key_left = on_key_left
    pen.on_key_right = on_key_right
    pen.on_key_up = on_key_up
    pen.on_key_down = on_key_down

    return pen

def create_label(x,y, cl, text):
    t = Turtle()
    go_xy(t, x, y)
    t.color(cl)
    t.write(text, font=("Arial", 16, "normal"))
    t.hideturtle()
    return t

def create_button(x,y, cl, shape = "square"):
    t = Turtle()
    t.shape(shape)
    go_xy(t, x, y)
    t.color(cl)
    return t

def create_indicator(x,y, active):
    t = Turtle()
    t.speed(0)
    t.shape("circle")
    go_xy(t, x, y)

    def set_active(active):
        ...

    t.active = set_active
    t.active(active)

    return t
   
def create_field():
    draw_rect(getpen(), -200, 120, 400, 320, "white")

create_field()
draw_rect(getpen(),-200, 200, 400, 70, "green")
pen = create_pen()

def on_screen_click(x, y):
    if y>120:
        return
    go_xy(pen,x,y)

def on_drag(x, y):
    if y>120:
        return
    pen.goto(x,y)
    

btn_width_up = create_button(100, 180, "red")
btn_width_down = create_button(100, 150, "blue")
btn_clear = create_button(-80, 165, "orange")
width_label = create_label(130, 150, "black", f"W: {pen.width()}")

def on_width_up(x, y):
    ...

def on_width_down(x, y):
    ...

def on_clear(x, y):
    pen.clear()

btn_clear.onclick(on_clear)
btn_width_up.onclick(on_width_up)
btn_width_down.onclick(on_width_down)

fill_label = create_label(-50, 150, "white", f"Заливка:")
clear_label = create_label(-190, 150, "white", f"Очистити:")
fill_indicator = create_indicator(50, 165, False)

def on_begin_fill():
    ...

def on_end_fill():
    ...

#screen.onkey(pen.on_key_left, "")
#screen.onkey(pen.on_key_right, "")
#screen.onkey(pen.on_key_up, "")
#screen.onkey(pen.on_key_down, "")

screen.onkey(pen.set_red, "r")
screen.onkey(pen.set_green, "g")
screen.onkey(pen.set_blue, "b")

screen.onkey(pen.set_white, "w")
#screen.onkey(pen.clear, "")
#screen.onkey(on_begin_fill, "")
#screen.onkey(on_end_fill, "")

#dragscreen.onclick(on_screen_click)
pen.ondrag(on_drag)
screen.onclick(on_screen_click)
screen.listen()

done()