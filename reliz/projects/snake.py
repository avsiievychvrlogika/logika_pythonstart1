import pygame
import time
import random

pygame.init()

BACK = (200, 255, 255)  
width = 460
height = 460
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


class Food(Area):
    def __init__(self):
        super().__init__(0, 0, 20, 20, color=(255, 0, 0))  
        self.respawn()
    
    def draw(self):
        self.fill()
    
    def respawn(self):
        max_x = (480 - 20) // 20  
        max_y = (480 - 20) // 20
        x = random.randint(0, max_x) * 20
        y = random.randint(0, max_y) * 20
        
        self.rect.x = x
        self.rect.y = y

class SnakeSegment(Area):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20, color=(0, 0, 0)) 
    
    def draw(self):
        self.fill()

class Snake:
    def __init__(self):
        self.segments = []
        self.direction = "RIGHT"
        
        center_x = 240  
        center_y = 240
        
        self.segments.append(SnakeSegment(center_x, center_y))        
        self.segments.append(SnakeSegment(center_x - 20, center_y))
        self.segments.append(SnakeSegment(center_x - 40, center_y))
    
    def draw(self):
        for segment in self.segments:
            segment.draw()
    
    def grow(self):
        tail = self.segments[-1]
        new_segment = SnakeSegment(tail.rect.x, tail.rect.y)
        self.segments.append(new_segment)
    
    def move(self):
        head = self.segments[0]
        new_x = head.rect.x
        new_y = head.rect.y
        
        if self.direction == "RIGHT":
            new_x += 20
        elif self.direction == "LEFT":
            new_x -= 20
        elif self.direction == "DOWN":
            new_y += 20
        elif self.direction == "UP":
            new_y -= 20
        
        new_head = SnakeSegment(new_x, new_y)
        self.segments.insert(0, new_head)
                
        self.segments.pop()
    
    def collision(self):
        head = self.segments[0]
        
        
        if (head.rect.x < 0 or head.rect.x >= width - 20 or 
            head.rect.y < 0 or head.rect.y >= height - 20):
            return True
        
        
        for segment in self.segments[1:]:
            if head.colliderect(segment.rect):
                return True
        
        return False
    
    def get_head(self):
        return self.segments[0]


game = True
clock = pygame.time.Clock()

snake = Snake()
food = Food()
score = 0

score_label = Label(10, 10, 150, 30, BACK)

move_up = False
move_down = False
move_left = False
move_right = False


while game:
    mw.fill(BACK)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
    
    snake.move()
    
    if snake.collision():
        gameover_label = Label(150, 200, 200, 100, BACK)
        gameover_label.set_text("GAME OVER", 40, (255, 0, 0))
        gameover_label.draw()
        pygame.display.update()
        time.sleep(2)
        game = False
        continue
    
    
    if snake.get_head().colliderect(food.rect):
        snake.grow()
        food.respawn()
        score += 1
    
    
    if score >= 10:
        win_label = Label(150, 200, 200, 100, BACK)
        win_label.set_text("YOU WIN!", 40, (0, 200, 0))
        win_label.draw()
        pygame.display.update()
        time.sleep(2)
        game = False
        continue
    
    
    snake.draw()
    food.draw()
    
    
    score_label.set_text(f"Score: {score}", 20, (0, 0, 0))
    score_label.draw()
    
    
    border_color = (0, 0, 0)
    border_thickness = 2
    pygame.draw.rect(mw, border_color, (0, 0, width, height), border_thickness)
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()
