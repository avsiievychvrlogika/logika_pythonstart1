import pygame
import time
import random

pygame.init()

BACK = (200, 255, 255)  # Light blue background
mw = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game - Implementation")
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
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Game classes inheriting from Area
class Food(Area):
    def __init__(self):
        # Initialize with placeholder values, will be set in respawn()
        super().__init__(0, 0, 20, 20, color=(255, 0, 0))  # Red food
        self.respawn()
    
    def draw(self):
        self.fill()
    
    def respawn(self):
        """Place food at random grid-aligned position"""
        # TODO: Calculate grid positions to align with snake movement
        # TODO: Use 20x20 grid (same as snake segment size)
        # TODO: Calculate max_x and max_y positions within 480x480 play area
        # TODO: Generate random x and y coordinates on the grid
        # TODO: Update self.rect.x and self.rect.y
        # Hint: max_x = (480 - 20) // 20, then x = random.randint(0, max_x) * 20
        pass

class SnakeSegment(Area):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20, color=(0, 0, 0))  # Black snake
    
    def draw(self):
        self.fill()

class Snake:
    def __init__(self):
        self.segments = []  # List of SnakeSegment objects
        self.direction = "RIGHT"  # Current movement direction
        
        # Create initial snake - TODO: STUDENTS TO IMPLEMENT
        # TODO: Create snake starting at center of screen (240, 240)
        # TODO: Add 3 segments: head at center, then 2 body segments to the left
        # TODO: Each segment is 20x20 pixels
        # Hint: Head at (240, 240), then (220, 240), then (200, 240)
    
    def draw(self):
        """Draw all snake segments"""
        # TODO: Draw each segment in self.segments list
        pass
    
    def grow(self):
        """Add new segment to snake's tail"""
        # TODO: Get the last segment (tail) from self.segments
        # TODO: Create new SnakeSegment at same position as tail
        # TODO: Add new segment to end of self.segments list
        pass
    
    def move(self):
        """Move snake by adding new head and removing tail - CORE SNAKE ALGORITHM"""
        # TODO: Get current head position
        # TODO: Calculate new head position based on direction:
        #   - RIGHT: add 20 to x
        #   - LEFT: subtract 20 from x  
        #   - DOWN: add 20 to y
        #   - UP: subtract 20 from y
        # TODO: Create new SnakeSegment at new head position
        # TODO: Insert new head at beginning of segments list
        # TODO: Remove last segment (tail) from segments list
        # This creates the illusion of movement!
        pass
    
    def collision(self):
        """Check for wall and self collisions"""
        # TODO: Get head segment (first in list)
        # TODO: Check wall collision (head outside 0-480 range)
        # TODO: Check self collision (head touching any body segment)
        # TODO: Return True if collision detected, False otherwise
        return False
    
    def get_head(self):
        """Get the head segment for collision checking"""
        # TODO: Return first segment in self.segments list
        return None

# Game setup
game = True
clock = pygame.time.Clock()

# Create game objects - TODO: STUDENTS TO IMPLEMENT
# TODO: Create Snake object
snake = None

# TODO: Create Food object  
food = None

score = 0

# Labels
score_label = Label(10, 10, 150, 30, BACK)

# Game loop
while game:
    mw.fill(BACK)
    
    # Handle events - TODO: STUDENTS TO IMPLEMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            # TODO: Handle arrow key presses
            # TODO: Change snake direction, but prevent reverse direction
            # TODO: UP key: set direction to "UP" (but not if current direction is "DOWN")
            # TODO: Similar logic for DOWN, LEFT, RIGHT
            pass
    
    # Move snake - TODO: STUDENTS TO IMPLEMENT
    # TODO: Call snake.move() method
    
    # Check collisions - TODO: STUDENTS TO IMPLEMENT
    # TODO: Check if snake hit wall or itself using snake.collision()
    # TODO: If collision, show "GAME OVER" message and end game
    
    # Check food collision - TODO: STUDENTS TO IMPLEMENT
    # TODO: Check if snake head collides with food
    # TODO: If collision:
    #   - Make snake grow
    #   - Respawn food at new location
    #   - Increase score
    
    # Check win condition - TODO: STUDENTS TO IMPLEMENT
    # TODO: If score reaches target (e.g., 10), show "YOU WIN!" and end game
    
    # Draw everything
    if snake:
        snake.draw()
    
    if food:
        food.draw()
    
    # Draw score
    score_label.set_text(f"Score: {score}", 20, (0, 0, 0))
    score_label.draw()
    
    # Draw border
    border_color = (0, 0, 0)
    border_thickness = 2
    pygame.draw.rect(mw, border_color, (0, 0, 480, 480), border_thickness)
    
    pygame.display.update()
    clock.tick(10)  # Slow game speed for better control

pygame.quit()

# SNAKE ALGORITHM EXPLANATION:
#
# The Snake Game Algorithm - Core Concepts:
#
# 1. SNAKE REPRESENTATION:
#    - Snake is a list of segments (rectangles)
#    - First segment = head, others = body
#    - Each segment is 20x20 pixels on a grid
#
# 2. MOVEMENT ALGORITHM (The Key!):
#    - Add new head in direction of movement
#    - Remove tail segment
#    - This creates illusion of snake "moving"
#    - Example: [Head, Body1, Body2, Tail] becomes [NewHead, Head, Body1, Body2]
#
# 3. GROWTH ALGORITHM:
#    - When eating food: add new head BUT don't remove tail
#    - Snake gets longer by 1 segment
#    - Example: [Head, Body, Tail] + food = [NewHead, Head, Body, Tail]
#
# 4. COLLISION DETECTION:
#    - Wall collision: head position outside boundaries
#    - Self collision: head position equals any body segment position
#
# 5. DIRECTION CONTROL:
#    - Only allow perpendicular direction changes
#    - Prevent 180-degree turns (snake can't reverse into itself)
#
# 6. GRID SYSTEM:
#    - Everything moves in 20-pixel increments
#    - Ensures clean movement and collision detection
#    - Food spawns on grid-aligned positions
#
# IMPLEMENTATION GUIDE FOR STUDENTS:
#
# Step 1: Create snake and food objects
# - Initialize Snake with 3 segments in a row
# - Create Food object that spawns randomly
#
# Step 2: Implement Snake.move() - THE CORE ALGORITHM
# - Calculate new head position based on direction
# - Add new head to front of segments list
# - Remove tail from back of segments list
#
# Step 3: Implement direction control
# - Handle arrow key presses
# - Prevent reverse direction (UP when going DOWN, etc.)
#
# Step 4: Implement collision detection
# - Check if head hits walls (outside 0-480 range)
# - Check if head hits body (compare positions)
#
# Step 5: Implement food system
# - Detect when snake head touches food
# - Grow snake (don't remove tail on next move)
# - Respawn food at random grid position
#
# Step 6: Add game conditions
# - Game over on collision
# - Win condition at target score
# - Score display and game state management
#
# The beauty of Snake is in its simplicity - it's just list manipulation
# creating the illusion of a moving, growing creature! 