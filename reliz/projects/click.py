import pygame
import sys
import random
import time
pygame.init()

WIDTH, HEIGHT = 450, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
BACK = WHITE
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    
    def color(self, new_color):
        self.fill_color = new_color
    
    def fill(self):
        pygame.draw.rect(screen, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Label(Area):	
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
 
    def draw(self, shift_x=0, shift_y=0):
        if self.fill_color is not None:
            self.fill()
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

GAME_TIME = 60  
INITIAL_RADIUS = 30
dot_colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
dot_values = [1, 2, 3, 2, 5]  

def reset_game():
    global dot_x, dot_y, score, start_time, cur_time, game_over, dot_color, dot_value, radius
    radius = INITIAL_RADIUS
    dot_x = random.randint(radius, WIDTH - radius)
    dot_y = random.randint(105 + radius, HEIGHT - radius)
    dot_color_index = random.randint(0, len(dot_colors) - 1)
    dot_color = dot_colors[dot_color_index]
    dot_value = dot_values[dot_color_index]
    score = 0
    start_time = time.time()
    cur_time = start_time
    game_over = False

def new_dot():
    global dot_x, dot_y, dot_color, dot_value, radius
    elapsed_time = time.time() - start_time
    radius = max(15, INITIAL_RADIUS - int(elapsed_time / 10))  
    
    dot_x = random.randint(radius, WIDTH - radius)
    dot_y = random.randint(105 + radius, HEIGHT - radius)
    dot_color_index = random.randint(0, len(dot_colors) - 1)
    dot_color = dot_colors[dot_color_index]
    dot_value = dot_values[dot_color_index]

reset_game()

time_text = Label(300, 0, 50, 50, BACK)
time_text.set_text("Час:", 30, (0, 200, 0))

timer = Label(370, 0, 100, 50, BACK)

score_text = Label(10, 10, 200, 50, BACK)


clock = pygame.time.Clock()

def draw_dot(x, y, color, r):
    pygame.draw.circle(screen, color, (x, y), r)
    pygame.draw.circle(screen, BLACK, (x, y), r, 2)

def draw_game_over():
    score_text.draw()
    
    game_over_text = Label(WIDTH//2 - 100, HEIGHT//2 - 100, 200, 50, None)
    game_over_text.set_text("ГРА ЗАВЕРШЕНА!", 36, BLACK)
    game_over_text.draw()
    
   
    
    restart_text = Label(WIDTH//2 - 120, HEIGHT//2 + 50, 240, 50, None)
    restart_text.set_text("Натисніть SPACE для нової гри", 20, BLACK)
    restart_text.draw()

game = True
while game:

    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                reset_game()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mx, my = event.pos
            dist = ((mx - dot_x) ** 2 + (my - dot_y) ** 2) ** 0.5
            if dist <= radius:
                score += dot_value
                new_dot()

    if not game_over:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, GAME_TIME - int(elapsed_time))        
        
        if remaining_time <= 0:
            game_over = True
        
        draw_dot(dot_x, dot_y, dot_color, radius)
        
        score_text.set_text(f"Очки: {score}", 30, (0, 0, 0))
        score_text.draw()
        
        timer.set_text(f"{remaining_time}с", 30, (200, 200, 0))
        timer.draw()
        time_text.draw()
       
    
    else:
        draw_game_over()       

    
    pygame.display.update()
    clock.tick(60)

