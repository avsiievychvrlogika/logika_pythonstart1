import pygame
import time
pygame.init()

BACK = (255, 255, 255)  # White background
GRID_COLOR = (0, 0, 0)  # Black grid lines
mw = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tic Tac Toe - 2 Players Implementation")
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

# Game classes
class GameCell(Area):
    def __init__(self, x, y, row, col):
        super().__init__(x, y, 140, 140, color=(240, 240, 240))
        self.row = row
        self.col = col
        self.value = ""  # "", "X", or "O"
        self.label = Label(x + 50, y + 50, 40, 40, (240, 240, 240))
    
    def set_value(self, value):
        """Set the cell value to X or O and update display"""
        # TODO: Set self.value to the given value
        # TODO: If value is "X", set label text to "X" with red color (255, 0, 0)
        # TODO: If value is "O", set label text to "O" with blue color (0, 0, 255)
        # TODO: If value is empty, set label text to empty string
        # Hint: Use self.label.set_text(text, size, color)
        pass
    
    def is_empty(self):
        """Check if cell is empty"""
        # TODO: Return True if self.value is empty string, False otherwise
        return True
    
    def draw(self):
        """Draw the cell with border and X/O"""
        # TODO: Draw cell background (use self.fill())
        # TODO: Draw black border around cell (use pygame.draw.rect with width=3)
        # TODO: Draw X or O if cell has value (use self.label.draw())
        pass

class TicTacToeGame:
    def __init__(self):
        self.current_player = "X"  # X starts first
        self.game_over = False
        self.winner = ""
        
        # Create 3x3 grid of cells - TODO: STUDENTS TO IMPLEMENT
        self.cells = []
        # TODO: Create 3x3 grid using nested loops
        # TODO: For each row (0, 1, 2) and col (0, 1, 2):
        # TODO: Calculate x position: 50 + col * 150
        # TODO: Calculate y position: 50 + row * 150
        # TODO: Create GameCell and add to self.cells
        # Hint: self.cells should be a list of lists (3 rows, 3 cols each)
    
    def handle_click(self, mouse_x, mouse_y):
        """Handle mouse click on game board"""
        # TODO: Check if game is over, if so, return early
        
        # TODO: Check which cell was clicked using nested loops
        # TODO: For each cell, use cell.collidepoint(mouse_x, mouse_y)
        # TODO: If cell is clicked AND empty:
        #   - Set cell value to current player
        #   - Check for winner
        #   - Check for draw
        #   - Switch players
        pass
    
    def check_winner(self):
        """Check if current player has won"""
        # TODO: Check all 3 rows for three in a row
        # TODO: Check all 3 columns for three in a row  
        # TODO: Check both diagonals for three in a row
        # Hint: Compare cell values, make sure they're not empty
        # Return True if winner found, False otherwise
        return False
    
    def is_board_full(self):
        """Check if board is completely full (draw condition)"""
        # TODO: Check all cells to see if any are empty
        # TODO: Return True if all cells have values, False if any empty
        return False
    
    def switch_player(self):
        """Switch between X and O players"""
        # TODO: If current_player is "X", change to "O"
        # TODO: If current_player is "O", change to "X"
        pass
    
    def draw(self):
        """Draw the entire game board"""
        # TODO: Draw all cells using nested loops
        # TODO: Call draw() method for each cell
        pass

# Game setup
game = True
clock = pygame.time.Clock()

# Create game - TODO: STUDENTS TO IMPLEMENT
# TODO: Create TicTacToeGame object
tic_tac_toe = None

# Game loop
while game:
    mw.fill(BACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # TODO: Handle left mouse click
            # TODO: Get mouse position using event.pos
            # TODO: Call tic_tac_toe.handle_click() with mouse coordinates
            pass
    
    # Draw game - TODO: STUDENTS TO IMPLEMENT
    # TODO: Call tic_tac_toe.draw() to draw the board
    
    # Draw game status - TODO: STUDENTS TO IMPLEMENT
    if tic_tac_toe and tic_tac_toe.game_over:
        # TODO: If game is over, show winner or draw message
        # TODO: Create Label with appropriate message
        # TODO: Show restart instruction
        pass
    else:
        # TODO: Show current player's turn
        # TODO: Create Label showing whose turn it is
        # TODO: Use different colors for X (red) and O (blue)
        pass
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()

# IMPLEMENTATION GUIDE FOR STUDENTS:
#
# Step 1: Create the game grid
# - Initialize TicTacToeGame object
# - Create 3x3 grid of GameCell objects
# - Calculate correct positions for each cell
#
# Step 2: Implement GameCell methods
# - set_value(): Update cell value and label display
# - is_empty(): Check if cell contains no value
# - draw(): Draw cell background, border, and X/O
#
# Step 3: Handle mouse input
# - Detect mouse clicks on cells
# - Check if clicked cell is empty
# - Place current player's mark
#
# Step 4: Implement win checking
# - Check rows: 3 cells in same row with same value
# - Check columns: 3 cells in same column with same value  
# - Check diagonals: 3 cells in diagonal with same value
#
# Step 5: Implement game flow
# - Switch between X and O players
# - Check for draw condition (board full)
# - Handle game over state
#
# Step 6: Add visual feedback
# - Show current player's turn
# - Display winner or draw message
# - Add restart instructions
#
# Focus on game logic and user interaction! 