def create_t(x, y, sh, col):
    t = Turtle()
    t.speed(0)
    t.pu()
    t.color(col)
    t.shape(sh)
    t.setheading(270)
    t.goto(x, y)
    return t

def create_lbl(x, y, col,txt):
    l = create_t(x, y,"turtle", col)
    l.ht()
    l.count = -1

    def update(txt):
        l.count += 1
        l.clear()
        l.write(f"{txt} : {l.count}", font = ("Arial", 16))
    l.update = update


    def write_end(txt):
        l.goto(0,0)
        l.write(txt, font = ("Arial", 40))
        return True
    l.write_end = write_end


    l.update(txt)
    return l



screen.bgcolor("black")
pole = create_t(-150, 150, "turtle", "white")
pole.ht()
pole.begin_fill()
for _ in range(4):
    pole.fd(300)
    pole.lt(90)
pole.end_fill()