import pygame
import time
from random import randint
pygame.init()

BACK = (102, 255, 204)  
width = 450
height = 450
mw = pygame.display.set_mode((width, height))
mw.fill(BACK)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = BACK
        if color:
            self.fill_color = color
    
    def color(self, new_color):
        self.fill_color = new_color
    
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10, color=None):
        super().__init__(x, y, width, height, color=color)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (width, height))
    
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Paddle(Area):
    def __init__(self, x, y, color=(255, 255, 255)):
        super().__init__(x, y, 20, 80, color=color)  
        self.speed = 5
    
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        if self.rect.bottom < height:
            self.rect.y += self.speed
    
    def draw(self):
        self.fill()

class Ball(Area):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20, color=(255, 255, 255))  
        self.speed_x = 4
        self.speed_y = 3
        self.base_speed = 4
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
    def bounce_y(self):
        self.speed_y *= -1
    
    def bounce_x(self):
        self.speed_x *= -1
        
        if self.speed_x > 0:
            self.speed_x += 0.2
        else:
            self.speed_x -= 0.2
    
    def reset(self):
        self.rect.x = 240  
        self.rect.y = 240
        
        if randint(0, 1):
            self.speed_x = self.base_speed
        else:
            self.speed_x = -self.base_speed
        
        if randint(0, 1):
            self.speed_y = 3
        else:
            self.speed_y = -3
    
    def draw(self):
        
        pygame.draw.ellipse(mw, self.fill_color, self.rect)


game = True
clock = pygame.time.Clock()

paddle_a = Paddle(30, height/2 - 40, (255, 100, 100))  
paddle_b = Paddle(width - 50, height/2 - 40, (100, 100, 255))  

ball = Ball(width/2, height/2)

score_a = 0
score_b = 0

move_up_a = False
move_down_a = False
move_up_b = False
move_down_b = False

score_label_a = Label(120, 10, 60, 40, BACK)
score_label_b = Label(320, 10, 60, 40, BACK)

while game:
    mw.fill(BACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up_a = True
            elif event.key == pygame.K_s:
                move_down_a = True
            elif event.key == pygame.K_UP:
                move_up_b = True
            elif event.key == pygame.K_DOWN:
                move_down_b = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up_a = False
            elif event.key == pygame.K_s:
                move_down_a = False
            elif event.key == pygame.K_UP:
                move_up_b = False
            elif event.key == pygame.K_DOWN:
                move_down_b = False
    
    if move_up_a:
        paddle_a.move_up()
    if move_down_a:
        paddle_a.move_down()
    if move_up_b:
        paddle_b.move_up()
    if move_down_b:
        paddle_b.move_down()
    
    ball.move()
    
    if ball.rect.top <= 0 or ball.rect.bottom >= height:
        ball.bounce_y()
    
    if ball.colliderect(paddle_a.rect) and ball.speed_x < 0:
        ball.bounce_x()
    
    if ball.colliderect(paddle_b.rect) and ball.speed_x > 0:
        ball.bounce_x()
    
    if ball.rect.left <= 0:
        score_b += 1
        ball.reset()
        time.sleep(0.5)  
    
    if ball.rect.right >= width:
        score_a += 1
        ball.reset()
        time.sleep(0.5)  
    
    if score_a >= 5:
        win_label = Label(150, 200, 200, 100, BACK)
        win_label.set_text("Player A Wins!", 30, (255, 0, 0))
        win_label.draw()
        pygame.display.update()
        time.sleep(2)
        game = False
        continue
    
    if score_b >= 5:
        win_label = Label(150, 200, 200, 100, BACK)
        win_label.set_text("Player B Wins!", 30, (0, 0, 255))
        win_label.draw()
        pygame.display.update()
        time.sleep(2)
        game = False
        continue
    
    paddle_a.draw()
    paddle_b.draw()
    ball.draw()
    
    score_label_a.set_text(str(score_a), 50, (255, 0, 0))
    score_label_a.draw()
    
    score_label_b.set_text(str(score_b), 50, (0, 0, 255))
    score_label_b.draw()
    
    for y in range(0, 500, 20):
        pygame.draw.rect(mw, (255, 255, 255), (248, y, 4, 10))
    
    border_color = (0, 0, 0)
    border_thickness = 2
    pygame.draw.rect(mw, border_color, (0, 0, width, height), border_thickness)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()