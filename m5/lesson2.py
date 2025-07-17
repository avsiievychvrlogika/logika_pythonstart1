def create_t(x, y, h, col):
    t = Turtle()
    t.color(col)
    t.shape("turtle")
    t.setheading(h)
    t.pu()
    t.goto(x, y)
    t.pd()
    return t