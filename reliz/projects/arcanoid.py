import pygame
import time
from random import randint
pygame.init()
BACK = (255,255,255)
height=450
width=450
mw = pygame.display.set_mode((width,height))
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
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Block(Area):
    def __init__(self, x, y, color):
        super().__init__(x, y, 45, 20, color)
        self.active = True
    
    def draw(self):
        if self.active:
            pygame.draw.rect(mw, self.fill_color, self.rect)
            pygame.draw.rect(mw, (0, 0, 0), self.rect, 1)  

class Ball(Area):
    def __init__(self, x, y):
        super().__init__(x, y, 15, 15, (255, 0, 0))  
        self.speed_x = 3
        self.speed_y = 3
    
    def draw(self):
        pygame.draw.circle(mw, self.fill_color, self.rect.center, 7)
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
    def bounce_x(self):
        self.speed_x *= -1
    
    def bounce_y(self):
        self.speed_y *= -1

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x, y, width, height, color=None)
        self.image = pygame.image.load(filename)
    
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Platform(Picture):
    def __init__(self, x, y):
        super().__init__("platform.png", x, y, 100, 30)

def create_level(level_num):
    blocks = []
    colors = [
        (255, 0, 0),    
        (255, 165, 0),  
        (255, 255, 0),  
        (0, 255, 0),    
        (0, 0, 255),    
        (128, 0, 128)   
    ]
    
    if level_num == 1:
        for row in range(6):
            for col in range(8):
                x = 25 + col * 50  
                y = 50 + row * 25  
                color = colors[row % len(colors)]
                block = Block(x, y, color)
                blocks.append(block)
    
    elif level_num == 2:
        for row in range(6):
            blocks_in_row = 8 - row
            start_x = 25 + (row * 25)
            for col in range(blocks_in_row):
                x = start_x + col * 50
                y = 50 + row * 25
                color = colors[row % len(colors)]
                block = Block(x, y, color)
                blocks.append(block)
    
    elif level_num == 3:
        patterns = [
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
        ]
        for row in range(len(patterns)):
            for col in range(len(patterns[row])):
                if patterns[row][col] == 1:
                    x = 0 + col * 50
                    y = 50 + row * 25
                    color = colors[row % len(colors)]
                    block = Block(x, y, color)
                    blocks.append(block)
    
    return blocks
def len_blocks(blocks):
    l=0
    for b in blocks:
        if b.active:
            l+=1
    return l

game = True
clock = pygame.time.Clock()
current_level = 1
max_levels = 3

ball = Ball(240, 300)
platform = Platform(200, 350)
blocks = create_level(current_level)

move_right = False
move_left = False

while game:
    mw.fill(BACK)
    lenb=len(blocks)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                move_right = True
            elif e.key == pygame.K_LEFT:
                move_left = True
            elif e.key == pygame.K_SPACE and (len_blocks(blocks) == 0 or ball.rect.y > height):
                if len_blocks(blocks) == 0:
                    current_level += 1
                    if current_level > max_levels:
                        current_level = 1
                ball = Ball(240, 300)
                platform = Platform(200, 350)
                blocks = create_level(current_level)
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                move_right = False
            elif e.key == pygame.K_LEFT:
                move_left = False
    
    if move_right and platform.rect.right < width:
        platform.rect.x += 5
    if move_left and platform.rect.left > 0:
        platform.rect.x -= 5
    
    ball.move()
    
    if ball.rect.left <= 0 or ball.rect.right >= width:
        ball.bounce_x()
    if ball.rect.top <= 0:
        ball.bounce_y()
    
    if ball.rect.colliderect(platform.rect) and ball.speed_y > 0:
        ball.bounce_y()
        hit_pos = (ball.rect.centerx - platform.rect.centerx) / (platform.rect.width / 2)
        ball.speed_x = int(hit_pos * 3)
        if ball.speed_x == 0:
            if ball.speed_x >= 0:
                ball.speed_x = 1
            else:
                ball.speed_x = -1
    
    for block in blocks:
        if block.active and ball.rect.colliderect(block.rect):
            block.active = False
            
            ball_center_x = ball.rect.centerx
            ball_center_y = ball.rect.centery
            block_center_x = block.rect.centerx
            block_center_y = block.rect.centery
            
            dx = abs(ball_center_x - block_center_x)
            dy = abs(ball_center_y - block_center_y)
            
            if dx > dy:
                ball.bounce_x()
            else:
                ball.bounce_y()
            break
    
    for block in blocks:
        if block.active:
            block.draw()
    
    platform.draw()
    ball.draw()
    
    if ball.rect.y > height:
        time_text = Label(150, 200, 200, 50, BACK)
        time_text.set_text('YOU LOSE! Press SPACE', 30, (255, 0, 0))
        time_text.draw()
    elif len_blocks(blocks) == 0:
        if current_level >= max_levels:
            time_text = Label(150, 200, 200, 50, BACK)
            time_text.set_text('YOU WIN ALL! Press SPACE', 25, (0, 200, 0))
            time_text.draw()
        else:
            time_text = Label(150, 200, 200, 50, BACK)
            time_text.set_text('LEVEL COMPLETE! Press SPACE', 25, (0, 200, 0))
            time_text.draw()
    
    level_text = Label(10, 10, 100, 30, BACK)
    level_text.set_text(f'Level: {current_level}', 20, (0, 0, 0))
    level_text.draw()
    pygame.draw.rect(mw,(0,0,0),(0,0,width,height),1)
    pygame.display.update()
    clock.tick(60)

pygame.quit()


