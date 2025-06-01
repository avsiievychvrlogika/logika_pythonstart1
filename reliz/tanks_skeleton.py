import pygame
import time
from random import randint, choice
pygame.init()

BACK = (50, 50, 50)  # Dark gray background
mw = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tanks Game - Implementation")
mw.fill(BACK)

# Base classes following established pattern
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
    def set_text(self, text, fsize=12, text_color=(255, 255, 255)):
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

# Game classes
class Tank(Picture):
    def __init__(self, filename, x, y, speed=2):
        super().__init__(filename, x, y, 40, 40)
        self.speed = speed
        self.direction = 'up'  # up, down, left, right
        self.can_shoot = True
        self.shoot_delay = 0
        self.original_image = self.image.copy()  # Store original image for rotation
        self.angle = 0  # Current rotation angle
    
    def move(self, direction, walls):
        """Move tank in specified direction with collision detection"""
        # TODO: Store old position for collision checking
        # TODO: Move tank based on direction (up/down/left/right)
        # TODO: Update tank rotation angle based on direction
        # TODO: Update tank's visual rotation
        # TODO: Check if tank goes outside window boundaries (0-460 range)
        # TODO: Check collision with walls and revert position if needed
        pass
    
    def update_rotation(self):
        """Update tank's visual rotation based on movement direction"""
        # TODO: Rotate the original image to avoid quality loss
        # TODO: Update rect to maintain center position after rotation
        pass
    
    def shoot(self):
        """Create a bullet if tank can shoot"""
        # TODO: Check if tank can shoot (self.can_shoot)
        # TODO: Calculate bullet starting position based on tank direction
        # TODO: Set shooting delay and can_shoot to False
        # TODO: Return new Bullet object, or None if can't shoot
        return None
    
    def update(self):
        """Update tank's shooting delay"""
        # TODO: Decrease shoot_delay if > 0
        # TODO: Set can_shoot to True when delay reaches 0
        pass

class EnemyTank(Tank):
    def __init__(self, filename, x, y):
        super().__init__(filename, x, y, speed=1)
        self.move_timer = 0
        self.shoot_timer = randint(60, 120)
    
    def ai_move(self, walls, player):
        """AI movement for enemy tank"""
        # TODO: Increase move_timer
        # TODO: Change direction randomly every 60 frames
        # TODO: Move in current direction
        # Hint: Use choice(['up', 'down', 'left', 'right']) for random direction
        pass
    
    def ai_shoot(self):
        """AI shooting for enemy tank"""
        # TODO: Decrease shoot_timer
        # TODO: If timer <= 0, reset timer and try to shoot
        # TODO: Return bullet if shot, None otherwise
        return None

class Bullet(Area):
    def __init__(self, x, y, direction):
        super().__init__(x, y, 6, 6, color=(255, 255, 0))  # Yellow bullet
        self.direction = direction
        self.speed = 5
    
    def move(self):
        """Move bullet in its direction"""
        # TODO: Move bullet based on direction (up/down/left/right)
        # TODO: Use self.speed for movement distance
        pass
    
    def is_off_screen(self):
        """Check if bullet has left the screen"""
        # TODO: Return True if bullet is outside 0-500 range for x or y
        return False
    
    def draw(self):
        # Draw bullet as colored rectangle
        self.fill()

# Game setup
game = True
clock = pygame.time.Clock()

# Create player tank - TODO: STUDENTS TO IMPLEMENT
# TODO: Create Tank object at starting position (50, 420)
player_tank = None

# Create enemy tanks - TODO: STUDENTS TO IMPLEMENT
enemy_tanks = []
# TODO: Create 3 EnemyTank objects at different positions
# Suggested positions: (100, 50), (250, 50), (400, 50)

# Create walls - TODO: STUDENTS TO IMPLEMENT
walls = []
# TODO: Create Picture objects for walls at various positions
# Use "wall.png" filename, 40x40 size
# Suggested positions: (150,150), (190,150), (230,150), (300,250), etc.

# Bullets lists
player_bullets = []
enemy_bullets = []

# Game controls - using boolean variables (established pattern)
move_up = False
move_down = False
move_left = False
move_right = False
shoot = False

# Game loop
while game:
    mw.fill(BACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            # TODO: Set movement booleans to True for arrow keys
            # TODO: Set shoot to True for SPACE key
            pass
        elif event.type == pygame.KEYUP:
            # TODO: Set movement booleans to False when keys released
            # TODO: Set shoot to False when SPACE released
            pass
    
    # Player movement - TODO: STUDENTS TO IMPLEMENT
    # TODO: Check movement booleans and call player_tank.move() with appropriate direction
    
    # Player shooting - TODO: STUDENTS TO IMPLEMENT
    # TODO: If shoot is True, try to get bullet from player_tank.shoot()
    # TODO: If bullet created, add to player_bullets list
    
    # TODO: Call player_tank.update()
    
    # Enemy AI - TODO: STUDENTS TO IMPLEMENT
    for enemy in enemy_tanks[:]:  # Use slice to avoid modification during iteration
        # TODO: Call enemy.ai_move() with walls and player_tank
        # TODO: Call enemy.update()
        # TODO: Try to get bullet from enemy.ai_shoot()
        # TODO: If bullet created, add to enemy_bullets list
        pass
    
    # Update player bullets - TODO: STUDENTS TO IMPLEMENT
    for bullet in player_bullets[:]:
        # TODO: Move bullet
        # TODO: Check if bullet is off screen and remove if needed
        # TODO: Check collision with walls and remove bullet if hit
        # TODO: Check collision with enemies and remove both if hit
        pass
    
    # Update enemy bullets - TODO: STUDENTS TO IMPLEMENT
    for bullet in enemy_bullets[:]:
        # TODO: Move bullet
        # TODO: Check if bullet is off screen and remove if needed
        # TODO: Check collision with walls and remove bullet if hit
        # TODO: Check collision with player and end game if hit
        pass
    
    # Draw everything
    for wall in walls:
        wall.draw()
    
    if player_tank:
        player_tank.draw()
    
    for enemy in enemy_tanks:
        enemy.draw()
    
    for bullet in player_bullets:
        bullet.draw()
    
    for bullet in enemy_bullets:
        bullet.draw()
    
    # Check win condition - TODO: STUDENTS TO IMPLEMENT
    # TODO: If no enemy tanks left, show win message and end game
    
    pygame.display.update()
    clock.tick(60)

# Game over screen - TODO: STUDENTS TO IMPLEMENT
# TODO: Show "GAME OVER!" message if player lost

pygame.quit()

# IMPLEMENTATION GUIDE FOR STUDENTS:
#
# Step 1: Create game objects
# - Create player_tank at starting position
# - Create 3 enemy tanks at different positions
# - Create wall objects for obstacles
#
# Step 2: Implement Tank.move()
# - Store old position for collision checking
# - Move based on direction (change x or y by speed)
# - Update rotation angle and visual rotation
# - Check boundaries and wall collisions
#
# Step 3: Implement shooting system
# - Tank.shoot(): Create bullet at tank position
# - Tank.update(): Handle shooting delay
# - Bullet.move(): Move bullet in its direction
# - Bullet.is_off_screen(): Check screen boundaries
#
# Step 4: Implement controls
# - Handle KEYDOWN/KEYUP events for movement and shooting
# - Use boolean variables for smooth movement
#
# Step 5: Implement AI
# - EnemyTank.ai_move(): Random direction changes
# - EnemyTank.ai_shoot(): Periodic shooting
#
# Step 6: Implement collision detection
# - Bullet vs walls (remove bullet)
# - Player bullets vs enemies (remove both)
# - Enemy bullets vs player (game over)
# - Tank vs walls (prevent movement)
#
# Step 7: Implement game conditions
# - Win: All enemies destroyed
# - Lose: Player hit by enemy bullet
#
# Focus on game mechanics and logic - no complex physics needed! 