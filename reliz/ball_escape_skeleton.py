import pygame
import math
from random import randint
pygame.init()

BACK = (20, 20, 40)  # Dark blue background
mw = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ball Escape - Game Mechanics")
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
        if self.fill_color!=BACK:
            self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Physics Simulation Functions - ALL IMPLEMENTED
def apply_gravity(ball):
    """Apply gravity force to ball's vertical velocity - PHYSICS COMPLETE"""
    ball.speed_y += ball.gravity

def apply_air_resistance(ball):
    """Apply air resistance to reduce ball velocity - PHYSICS COMPLETE"""
    ball.speed_x *= ball.friction
    ball.speed_y *= ball.friction

def update_ball_position(ball):
    """Update ball position based on current velocity - PHYSICS COMPLETE"""
    ball.center_x += ball.speed_x
    ball.center_y += ball.speed_y
    ball.rect.x = ball.center_x - 8
    ball.rect.y = ball.center_y - 8

def handle_wall_collisions(ball):
    """Handle ball bouncing off window boundaries - PHYSICS COMPLETE"""
    if ball.center_x <= ball.radius:
        ball.center_x = ball.radius
        ball.speed_x = abs(ball.speed_x) * ball.bounce_damping
    elif ball.center_x >= 500 - ball.radius:
        ball.center_x = 500 - ball.radius
        ball.speed_x = -abs(ball.speed_x) * ball.bounce_damping
        
    if ball.center_y <= ball.radius:
        ball.center_y = ball.radius
        ball.speed_y = abs(ball.speed_y) * ball.bounce_damping
    elif ball.center_y >= 500 - ball.radius:
        ball.center_y = 500 - ball.radius
        ball.speed_y = -abs(ball.speed_y) * ball.bounce_damping

def calculate_circle_collision(ball, circle, old_x, old_y):
    """Calculate if ball collides with circle and return collision data - PHYSICS COMPLETE"""
    distance = calculate_distance(ball.center_x, ball.center_y, circle.center_x, circle.center_y)
    old_distance = calculate_distance(old_x, old_y, circle.center_x, circle.center_y)
    
    crossed_inward = old_distance > circle.radius and distance <= circle.radius + ball.radius
    crossed_outward = old_distance < circle.radius and distance >= circle.radius - ball.radius
    
    if crossed_inward or crossed_outward:
        dx = ball.center_x - circle.center_x
        dy = ball.center_y - circle.center_y
        angle = math.degrees(math.atan2(dy, dx))
        
        if angle < 0:
            angle += 360
        
        gap_start = circle.gap_start % 360
        gap_end = (circle.gap_start + circle.gap_size) % 360
        
        if gap_start < gap_end:
            in_gap = gap_start <= angle <= gap_end
        else:
            in_gap = angle >= gap_start or angle <= gap_end
        
        return {
            'collision': not in_gap,
            'crossed_inward': crossed_inward,
            'distance': distance,
            'dx': dx,
            'dy': dy
        }
    
    return {'collision': False}

def apply_circle_bounce(ball, circle, collision_data):
    """Apply bounce physics when ball hits circle - PHYSICS COMPLETE"""
    dx = collision_data['dx']
    dy = collision_data['dy']
    distance = collision_data['distance']
    crossed_inward = collision_data['crossed_inward']
    
    if distance > 0:
        normal_x = dx / distance
        normal_y = dy / distance
    else:
        normal_x = 1
        normal_y = 0
    
    dot_product = ball.speed_x * normal_x + ball.speed_y * normal_y
    ball.speed_x = (ball.speed_x - 2 * dot_product * normal_x) * ball.bounce_damping
    ball.speed_y = (ball.speed_y - 2 * dot_product * normal_y) * ball.bounce_damping
    
    if crossed_inward:
        target_distance = circle.radius + ball.radius + 1
        ball.center_x = circle.center_x + normal_x * target_distance
        ball.center_y = circle.center_y + normal_y * target_distance
    else:
        target_distance = circle.radius - ball.radius - 1
        if target_distance > 0:
            ball.center_x = circle.center_x + normal_x * target_distance
            ball.center_y = circle.center_y + normal_y * target_distance

def calculate_distance(x1, y1, x2, y2):
    """Calculate distance between two points - PHYSICS COMPLETE"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Core Game Logic Functions - STUDENTS TO IMPLEMENT
def check_circle_escape(ball, circles):
    """Check which circles the ball has escaped and remove them"""
    # TODO: Check each circle to see if ball is outside it
    # Remove escaped circles from the list
    # Hint: Use is_ball_outside_circle() function
    pass

def is_ball_outside_circle(ball, circle):
    """Check if ball is completely outside a circle"""
    # TODO: Calculate distance from ball to circle center
    # Return True if distance > circle.radius
    # Hint: Use calculate_distance function
    return False

def update_circle_rotations(circles):
    """Update rotation of all circles"""
    # TODO: Call update() method for each circle
    pass

def check_win_condition(circles):
    """Check if player has won (escaped all circles)"""
    # TODO: Return True if circles list is empty
    return False

def check_time_limit(time_left):
    """Check if time limit has been reached"""
    # TODO: Return True if time_left <= 0
    return False

class Ball(Area):
    def __init__(self, x, y):
        super().__init__(x, y, 16, 16, color=(255, 255, 255))  # White ball
        self.center_x = x + 8
        self.center_y = y + 8
        self.speed_x = 3.0  # Higher initial speed
        self.speed_y = -2.0  # Higher initial vertical velocity
        self.radius = 8
        self.gravity = 0.03  # Even less gravity
        self.friction = 0.9998  # Even less air resistance
        self.bounce_damping = 0.98  # Much more bouncy (was 0.95)
    
    def move(self, circles):
        """Main movement function using separated physics and game logic"""
        # Store old position for collision detection
        old_x = self.center_x
        old_y = self.center_y
        
        # Apply physics simulations - ALL IMPLEMENTED
        apply_gravity(self)
        apply_air_resistance(self)
        update_ball_position(self)
        handle_wall_collisions(self)
        
        # Handle circle collisions - PHYSICS COMPLETE
        for circle in circles:
            collision_data = calculate_circle_collision(self, circle, old_x, old_y)
            if collision_data['collision']:
                apply_circle_bounce(self, circle, collision_data)
                break  # Only handle one collision per frame
    
    def draw(self):
        # Draw ball as circle
        pygame.draw.circle(mw, (255, 255, 255), (int(self.center_x), int(self.center_y)), self.radius)
    
    def distance_from_center(self, center_x, center_y):
        # Calculate distance from ball to center point
        return calculate_distance(self.center_x, self.center_y, center_x, center_y)

class Circle:
    def __init__(self, center_x, center_y, radius, gap_start, gap_size):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.gap_start = gap_start  # Angle where gap starts (in degrees)
        self.gap_size = gap_size    # Size of gap (in degrees)
        self.color = (0, 255, 200)  # Cyan color
        self.thickness = 4
        self.rotation_speed = 0.8  # Clockwise rotation speed (degrees per frame)
    
    def update(self):
        # Rotate clockwise - IMPLEMENTED
        self.gap_start += self.rotation_speed
        if self.gap_start >= 360:
            self.gap_start -= 360
    
    def draw(self):
        """Draw the circle with a gap"""
        # TODO: Draw circle segments, leaving gap empty
        # Hint: Use pygame.draw.lines to draw circle segments
        # Skip drawing where the gap is located
        # You can use the same approach as in the main game
        pass

class Game:
    def __init__(self):
        self.center_x = 250
        self.center_y = 250
        
        # Create ball at center
        self.ball = Ball(self.center_x - 8, self.center_y - 8)
        
        # Create circles - TODO: STUDENTS TO IMPLEMENT
        self.circles = []
        # TODO: Create 6 circles with different radii
        # Use: Circle(center_x, center_y, radius, gap_start, gap_size)
        # Radii should be: 60, 90, 120, 150, 180, 210
        # Use randint(0, 360) for random gap positions
        # Use gap_size = 60 for all circles
        
        self.game_over = False
        self.won = False
        
        # Timer
        self.time_left = 30  # 30 seconds to escape
        self.timer = 0
    
    def update(self):
        if self.game_over:
            return
        
        # Update game logic (separated from physics)
        update_circle_rotations(self.circles)
        
        # Move ball (physics handled internally)
        self.ball.move(self.circles)
        
        # Check game conditions
        check_circle_escape(self.ball, self.circles)
        
        # Check win condition
        if check_win_condition(self.circles):
            self.game_over = True
            self.won = True
        
        # Update timer
        self.timer += 1
        if self.timer >= 60:  # 60 frames = 1 second
            self.timer = 0
            self.time_left -= 1
            
            if check_time_limit(self.time_left):
                self.game_over = True
                self.won = False
    
    def draw(self):
        # Draw circles
        for circle in self.circles:
            circle.draw()
        
        # Draw ball
        self.ball.draw()
        
        # Draw timer
        timer_text = Label(10, 10, 150, 30, BACK)
        timer_text.set_text(f'Time: {self.time_left}s', 20, (255, 255, 255))
        timer_text.draw()
        
        # Draw circles remaining
        circles_text = Label(10, 50, 200, 30, BACK)
        circles_text.set_text(f'Circles left: {len(self.circles)}', 16, (255, 255, 255))
        circles_text.draw()
        
        # Draw game over messages
        if self.game_over:
            if self.won:
                result_text = Label(150, 200, 200, 50, BACK)
                result_text.set_text('YOU ESCAPED!', 30, (0, 255, 0))
                result_text.draw()
            else:
                result_text = Label(150, 200, 200, 50, BACK)
                result_text.set_text('TIME UP!', 30, (255, 0, 0))
                result_text.draw()
            
            restart_text = Label(120, 260, 260, 30, BACK)
            restart_text.set_text('Close and restart to play again', 16, (200, 200, 200))
            restart_text.draw()

# Game setup
game = True
clock = pygame.time.Clock()
ball_game = Game()

# Game loop
while game:
    mw.fill(BACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    # Update game
    ball_game.update()
    
    # Draw game
    ball_game.draw()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()

# IMPLEMENTATION GUIDE FOR STUDENTS:
# 
# Step 1: Create the circle obstacles (in Game.__init__)
# - Add 6 Circle objects to self.circles list
# - Use radii: 60, 90, 120, 150, 180, 210
# - Use randint(0, 360) for random gap positions
# - Set gap_size = 60 for all circles
#
# Step 2: Implement Circle.draw()
# - Draw circle segments, leaving gap empty
# - Use same approach as main game with pygame.draw.lines
# - Skip drawing where gap is located
#
# Step 3: Implement game logic functions
# - check_circle_escape(): Remove circles ball has escaped
# - is_ball_outside_circle(): Check if ball is outside circle
# - update_circle_rotations(): Update all circles
# - check_win_condition(): Return True if no circles left
# - check_time_limit(): Return True if time is up
#
# All physics calculations are COMPLETE - focus on game mechanics! 