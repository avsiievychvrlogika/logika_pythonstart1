# Якщо потрібно побудувати корабель, як в завданні:
# x1, y1, x2, y2, name, is_right

# рівень 1
data_1_1 = (-80, -120,  -200, 0, "Сідней", True)
data_1_2 = (-80, 120,  0, 0, "Берлін", False)
data_1_3 = (80, 120,  0, 0, "Рим", False)
data_1_4 = (80, -120,  0, 0, "Київ", False)

# рівень 2
data_2_1 = (-80, 120,  0, 0, "Атлантичний", False)
data_2_2 = (200, 0, 120, -120, "Китайський", True)
data_2_3 = (80, 120,  0, 0, "Індійський", False)
data_2_4 = (80, -120,  0, 0, "Тихий", False)

# рівень 3
data_3_1 = (-200, 120, 0, 0, "Python", False)
data_3_2 = (100, 120, 0, 0, "C++", False)
data_3_3 = (0, 0, 0, 200, "Mouse", True)
data_3_4 = (0, -120, 0, 0, "JavaAcript", False)

# рівень 4
data_4_1 = (-80, 120, 0, 0, "Cat",  False)
data_4_2 = (80, 120, 0, 0, "Dog",  False)
data_4_3 = (0, -120, 0, 0, "Mouse", False)
data_4_4 = (0, 200, 160, 40, "Shark", True)

# рівень 5
data_5_1 = (120, -120, -80, -120, "Head", True)
data_5_2 = (-120, -120, 0, 0, "CPU", False)
data_5_3 = (0, 0, 0, 0, "SSD",  False)
data_5_4 = (150, -0, 0, 0, "RAM",  False)

# рівень 6
data_6_1 = (-80, 120, 0, 0, "Red", False)
data_6_2 = (-120, 40, 0 , 200, "Brawl", True)
data_6_3 = (80, 120, 0, 0, "Green", False)
data_6_4 = (100, 0, 0, 0, "Blue", False)

# рівень 7
data_7_1 = (-80, 120, 0, 0, "Train", False)
data_7_2 = (80, 120, 0, 0, "Car",  False)
data_7_3 = (-200, 0, 200, 0, "Seat", True)
data_7_4 = (120, 0, 0, 0, "Rocket", False)

# рівень 8
data_8_1 = (-80, 120, 0, 0, "One", False)
data_8_2 = (80, 120, 0, 0, "Two",  False)
data_8_3 = (80, -120, 0, 0, "Three",  False)
data_8_4 = (160, 40, -120, 40, "Minus", True)

from turtle import *
from time import sleep



screen = getscreen()
screen.bgcolor("white")
hideturtle()
pu()
goto(-200, 150)


def info(text, col, bg):
    screen.bgcolor(bg)
    color(col)
    write(text, font=("Arial", 28, "normal"))
    sleep(1)
    clear()
    screen.bgcolor("white")



class Player(Turtle):
    # TYPE: статична властивість — лічильник помилок усіх гравців
    errors = 0

    def __init__(self, x, y, game):
        super().__init__(shape="square")
        self.color("green")
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.game = game

        screen.onkey(self.__move_left, "Left")
        screen.onkey(self.__move_right, "Right")
        screen.onkey(self.__move_up, "Up")
        screen.onkey(self.__move_down, "Down")

    def __move_left(self):
        self.setheading(180)
        self.forward(10)
        self.check_collision()

    def __move_right(self):
        self.setheading(0)
        self.forward(10)
        self.check_collision()

    def __move_up(self):
        self.setheading(90)
        self.forward(10)
        self.check_collision()

    def __move_down(self):
        self.setheading(-90)
        self.forward(10)
        self.check_collision()

    def check_collision(self):
        
        end_level = False
        for robot in self.game.level.robots:
            if self.distance(robot.pos()) < 20 and robot.isvisible():
                robot.clear()
                robot.hideturtle()
                if robot.is_right:
                    end_level = True
                    robot.pendown()
                    robot.move()
                    break
                else:
                    # TYPE: збільшуємо статичне поле класу Player
                    Player.errors += 1

        if end_level:
            for robot in self.game.level.robots:
                if not robot.is_right:
                    robot.clear()
                    robot.hideturtle()
            self.game.next_level()


class Robot(Turtle):

    def __init__(self, x1, y1, x2, y2, col, text, is_right=False):
        super().__init__(shape="classic")
        self.hideturtle()
        self.speed(0)
        self.color(col)
        self.penup()
        self.goto(x1, y1)
        self.showturtle()
        self.write(text, font=("Arial", 16, "normal"))
        self.is_right = is_right
        self.__command_x = x2
        self.__command_y = y2



    def move(self):
        if self.is_right:
            self.goto(self.__command_x, self.__command_y)


class Level:
    # TYPE: статична (класова) властивість із доступними кольорами
    colorsList = ("red", "blue", "orange", "green")

    def __init__(self):
        self.robots = []

    def add_robot(self, x1, y1, x2, y2, text, is_right):
        # TYPE: беремо колір зі статичної властивості класу
        col = Level.colorsList[len(self.robots)]
        r = Robot(x1, y1, x2, y2, col, text, is_right)
        self.robots.append(r)


class Game:
    LEVEL_DATA = [
        [data_1_1, data_1_2, data_1_3, data_1_4],
        [data_2_1, data_2_2, data_2_3, data_2_4],
        [data_3_1, data_3_2, data_3_3, data_3_4],
        [data_4_1, data_4_2, data_4_3, data_4_4],
        [data_5_1, data_5_2, data_5_3, data_5_4],
        [data_6_1, data_6_2, data_6_3, data_6_4],
        [data_7_1, data_7_2, data_7_3, data_7_4],
        [data_8_1, data_8_2, data_8_3, data_8_4],
    ]

    def __init__(self):
        self.currentLevel = 0
        self.create_level_from_data(self.currentLevel)
        self.player = Player(0, 0, self)

    def create_level_from_data(self, index):
        level = Level()
        for (x1, y1, x2, y2, text, is_right) in Game.LEVEL_DATA[index]:
            level.add_robot(x1, y1, x2, y2, text, is_right)
        self.level = level

    def next_level(self):
        # TYPE: перемикаємо рівень і показуємо інформацію
        self.currentLevel += 1
        info(f"Рівень {self.currentLevel} пройдено!", "green", "orange")

        if self.currentLevel >= len(Game.LEVEL_DATA):
            info("Перемога!", "white", "green")
            info(f"Помилок: {Player.errors} шт!", "white", "green")
        else:
            self.create_level_from_data(self.currentLevel)


# Запуск гри
info("Знайдіть унікальні слова!", "white", "green")
screen.listen()
game = Game()
done()