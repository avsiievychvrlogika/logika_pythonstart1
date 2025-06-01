import pygame
import time
from random import randint
pygame.init()

BACK = (102, 255, 204)  # Light green background
mw = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ping Pong - 2 Players Implementation")
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

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10, color=None):
        super().__init__(x, y, width, height, color=color)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (width, height))
    
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

# Game classes
class Paddle(Area):
    def __init__(self, x, y, color=(255, 255, 255)):
        super().__init__(x, y, 20, 80, color=color)  # 20x80 paddle
        self.speed = 5
    
    def move_up(self):
        """Move paddle up with boundary checking"""
        # TODO: Check if paddle top is above 0
        # TODO: If safe, move paddle up by self.speed
        pass
    
    def move_down(self):
        """Move paddle down with boundary checking"""
        # TODO: Check if paddle bottom is below window height (500)
        # TODO: If safe, move paddle down by self.speed
        pass
    
    def draw(self):
        # Draw paddle as filled rectangle
        self.fill()

class Ball(Area):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20, color=(255, 255, 255))  # White ball
        self.speed_x = 4
        self.speed_y = 3
        self.base_speed = 4
    
    def move(self):
        """Move ball based on current speed"""
        # TODO: Update ball position using speed_x and speed_y
        # TODO: Add speed_x to rect.x
        # TODO: Add speed_y to rect.y
        pass
    
    def bounce_y(self):
        """Bounce ball vertically (reverse Y direction)"""
        # TODO: Reverse the Y speed (multiply by -1)
        pass
    
    def bounce_x(self):
        """Bounce ball horizontally (reverse X direction) and increase speed"""
        # TODO: Reverse the X speed (multiply by -1)
        # TODO: Increase speed slightly after each paddle hit
        # TODO: If speed_x > 0, add 0.2; if speed_x < 0, subtract 0.2
        pass
    
    def reset(self):
        """Reset ball to center with random direction"""
        # TODO: Set ball position to center of screen (240, 240)
        # TODO: Set random horizontal direction (left or right)
        # TODO: Set random vertical direction (up or down)
        # TODO: Use base_speed for horizontal, 3 for vertical
        # Hint: Use randint(0, 1) for random choice
        pass
    
    def draw(self):
        """Draw ball as circle"""
        # TODO: Draw ball as ellipse using pygame.draw.ellipse
        # TODO: Use mw, self.fill_color, and self.rect
        pass

# Game setup
game = True
clock = pygame.time.Clock()

# Create paddles - TODO: STUDENTS TO IMPLEMENT
# TODO: Create left paddle (Player A) at position (30, 210) with red color (255, 100, 100)
paddle_a = None

# TODO: Create right paddle (Player B) at position (450, 210) with blue color (100, 100, 255)
paddle_b = None

# Create ball - TODO: STUDENTS TO IMPLEMENT
# TODO: Create ball at center position (240, 240)
ball = None

# Score
score_a = 0
score_b = 0

# Controls (following established boolean pattern)
move_up_a = False
move_down_a = False
move_up_b = False
move_down_b = False

# Labels
score_label_a = Label(120, 20, 60, 40, BACK)
score_label_b = Label(320, 20, 60, 40, BACK)

# Game loop
while game:
    mw.fill(BACK)
    
    # Handle events - TODO: STUDENTS TO IMPLEMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            # TODO: Handle key presses for Player A (W/S keys)
            # TODO: Handle key presses for Player B (UP/DOWN arrow keys)
            # TODO: Set appropriate movement booleans to True
            pass
        elif event.type == pygame.KEYUP:
            # TODO: Handle key releases for both players
            # TODO: Set appropriate movement booleans to False
            pass
    
    # Move paddles - TODO: STUDENTS TO IMPLEMENT
    # TODO: Check movement booleans and call appropriate paddle methods
    # TODO: If move_up_a is True, call paddle_a.move_up()
    # TODO: Similar logic for all four movement directions
    
    # Move ball - TODO: STUDENTS TO IMPLEMENT
    # TODO: Call ball.move() method
    
    # Ball collision with walls - TODO: STUDENTS TO IMPLEMENT
    # TODO: Check if ball hits top or bottom wall (y <= 0 or y >= 500)
    # TODO: If collision, call ball.bounce_y()
    
    # Ball collision with paddles - TODO: STUDENTS TO IMPLEMENT
    # TODO: Check collision between ball and paddle_a (when ball moving left)
    # TODO: Check collision between ball and paddle_b (when ball moving right)
    # TODO: Call ball.bounce_x() on paddle collision
    # Hint: Use ball.colliderect(paddle.rect) and check ball speed direction
    
    # Scoring - TODO: STUDENTS TO IMPLEMENT
    # TODO: Check if ball goes off left side (score for Player B)
    # TODO: Check if ball goes off right side (score for Player A)
    # TODO: Increase appropriate score, reset ball, add brief pause
    # Hint: Use time.sleep(0.5) for pause
    
    # Check win condition - TODO: STUDENTS TO IMPLEMENT
    # TODO: Check if either player reaches 5 points
    # TODO: Display winner message and end game
    # TODO: Show message for 2 seconds then quit
    
    # Draw everything
    if paddle_a:
        paddle_a.draw()
    
    if paddle_b:
        paddle_b.draw()
    
    if ball:
        ball.draw()
    
    # Draw scores - TODO: STUDENTS TO IMPLEMENT
    # TODO: Set score text for both players using score_label_a and score_label_b
    # TODO: Use different colors: red (255, 0, 0) for Player A, blue (0, 0, 255) for Player B
    # TODO: Draw both score labels
    
    # Draw center line
    for y in range(0, 500, 20):
        pygame.draw.rect(mw, (255, 255, 255), (248, y, 4, 10))
    
    # Draw border
    border_color = (0, 0, 0)
    border_thickness = 2
    pygame.draw.rect(mw, border_color, (0, 0, 500, 500), border_thickness)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()

# PING PONG GAME MECHANICS EXPLANATION:
#
# Core Game Elements:
#
# 1. PADDLE SYSTEM:
#    - Two paddles (left and right players)
#    - Vertical movement with boundary checking
#    - Smooth movement using boolean controls
#    - Speed-based position updates
#
# 2. BALL PHYSICS:
#    - Constant movement in X and Y directions
#    - Bouncing off top/bottom walls (reverse Y)
#    - Bouncing off paddles (reverse X + speed increase)
#    - Reset to center after scoring
#
# 3. COLLISION DETECTION:
#    - Ball vs walls (top/bottom boundaries)
#    - Ball vs paddles (left/right collision)
#    - Ball vs screen edges (scoring)
#    - Paddle vs screen boundaries (movement limits)
#
# 4. GAME FLOW:
#    - Two-player simultaneous control
#    - Score tracking for both players
#    - Win condition (first to reach target score)
#    - Ball reset after each point
#
# 5. CONTROL SYSTEM:
#    - Boolean-based smooth movement
#    - Separate controls for each player
#    - Event-driven input handling
#
# IMPLEMENTATION GUIDE FOR STUDENTS:
#
# Step 1: Create game objects
# - Create both paddles at correct positions
# - Create ball at center
# - Set up initial properties
#
# Step 2: Implement paddle movement
# - Handle KEYDOWN/KEYUP events for both players
# - Use boolean variables for smooth movement
# - Add boundary checking to prevent paddles leaving screen
#
# Step 3: Implement ball movement
# - Basic movement using speed_x and speed_y
# - Ball drawing as circle (ellipse)
# - Ball reset to center with random direction
#
# Step 4: Implement collision detection
# - Ball bouncing off top/bottom walls
# - Ball bouncing off paddles (with speed increase)
# - Check collision direction for realistic physics
#
# Step 5: Implement scoring system
# - Detect when ball leaves left/right edges
# - Award points to appropriate player
# - Reset ball and add brief pause
#
# Step 6: Add game conditions
# - Win condition (first to 5 points)
# - Game over screen with winner announcement
# - Score display with player colors
#
# Focus on physics, collision detection, and multiplayer interaction! 