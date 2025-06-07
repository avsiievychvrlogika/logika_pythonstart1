import pygame
import time
from random import randint
pygame.init()
BACK = (255,255,255)
mw = pygame.display.set_mode((500,500))
mw.fill(BACK)

class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = BACK
        if color:
            self.fill_color=color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)        
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Label(Area):	
    def set_text(self, text, fsize =12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text,True, text_color)
 
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width =10, height =10, color=None):
        super().__init__(x, y, width, height, color=color)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))

# TODO: Create Dinosaur class that inherits from Picture
class Dinosaur(Picture):
    def __init__(self, x, y):
        # TODO: Initialize dinosaur with "dinosaur.png", 50x50 size
        # TODO: Add variables for jumping: on_ground, jump_speed, gravity, ground_y
        pass
    
    def jump(self):
        # TODO: Make dinosaur jump only if on ground
        # Set jump_speed to -15 and on_ground to False
        pass
    
    def update(self):
        # TODO: Handle jump physics
        # If not on ground: move by jump_speed, add gravity to jump_speed
        # If reaches ground: reset position and jumping variables
        pass

# TODO: Create Cactus class that inherits from Area
class Cactus(Area):
    def __init__(self, x, y, speed):
        # TODO: Initialize cactus with green color (0, 150, 0), size 30x60
        # TODO: Set movement speed
        pass
    
    def update(self):
        # TODO: Move cactus to the left by speed
        pass
    
    def draw(self):
        # TODO: Draw cactus as green rectangle
        pass

# Ground class (completed for reference)
class Ground(Area):
    def __init__(self):
        super().__init__(0, 400, 500, 5, (100, 100, 100))

game = True
clock = pygame.time.Clock()

# TODO: Create game objects
dinosaur = None  # TODO: Create Dinosaur at position (50, 350)
ground = Ground()
obstacles = []   # List to store cacti
score = 0
frame_count = 0
game_speed = 5

# Controls
jump_pressed = False

while game:
    mw.fill(BACK)
    
    # Handle events (completed)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                jump_pressed = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_SPACE:
                jump_pressed = False
    
    # TODO: Make dinosaur jump when space is pressed
    # Use: if jump_pressed: dinosaur.jump()
    
    # TODO: Update dinosaur
    # Use: dinosaur.update()
    
    # Create new obstacles (completed)
    frame_count += 1
    if frame_count % 90 == 0:  # Every 90 frames
        new_cactus = Cactus(500, 340, game_speed)
        obstacles.append(new_cactus)
    
    # TODO: Update all obstacles
    # Use for loop to call update() on each obstacle
    
    # TODO: Remove obstacles that went off screen and increase score
    # Check if obstacle.rect.x < -30, then remove and add 1 to score
    
    # TODO: Check collisions between dinosaur and obstacles
    # If collision detected:
    #   - Show "GAME OVER" message using Label
    #   - Show final score using Label  
    #   - Wait 3 seconds with time.sleep(3)
    #   - Set game = False
    
    # TODO: Draw everything
    # 1. Draw ground: ground.fill()
    # 2. Draw dinosaur: dinosaur.draw()
    # 3. Draw all obstacles using for loop
    # 4. Draw score using Label
    
    pygame.display.update()
    clock.tick(40)

pygame.quit() 