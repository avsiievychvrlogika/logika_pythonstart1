import pygame
import time
pygame.init()

BACK = (255, 255, 255)  
GRID_COLOR = (0, 0, 0)  
mw = pygame.display.set_mode((500, 500))
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

class GameCell(Area):
    def __init__(self, x, y, row, col):
        super().__init__(x, y, 140, 140, color=(240, 240, 240))
        self.row = row
        self.col = col
        self.value = "" 
        self.label = Label(x + 50, y + 50, 40, 40, (240, 240, 240))
    
    def set_value(self, value):
        self.value = value
        if value == "X":
            self.label.set_text("X", 80, (255, 0, 0))  
        elif value == "O":
            self.label.set_text("O", 80, (0, 0, 255))  
        else:
            self.label.set_text("", 80, (0, 0, 0))
    
    def is_empty(self):
        return self.value == ""
    
    def draw(self):
        self.fill()        
        pygame.draw.rect(mw, GRID_COLOR, self.rect, 3)        
        if self.value != "":
            self.label.draw()

class TicTacToeGame:
    def __init__(self):
        self.current_player = "X"  
        self.game_over = False
        self.winner = ""        
       
        self.cells = []
        for row in range(3):
            cell_row = []
            for col in range(3):
                x = 50 + col * 150  
                y = 50 + row * 150
                cell = GameCell(x, y, row, col)
                cell_row.append(cell)
            self.cells.append(cell_row)
    
    def handle_click(self, mouse_x, mouse_y):
        if self.game_over:
            return
        
        for row in range(3):
            for col in range(3):
                cell = self.cells[row][col]
                if cell.collidepoint(mouse_x, mouse_y) and cell.is_empty():
                    cell.set_value(self.current_player)                    
                    if self.check_winner():
                        self.game_over = True
                        self.winner = self.current_player
                    elif self.is_board_full():
                        self.game_over = True
                        self.winner = "Draw"
                    else:
                        if self.current_player == "X":
                            self.current_player = "O"
                        else:
                            self.current_player = "X"
                    return
    
    def check_winner(self):
        for row in range(3):
            if (self.cells[row][0].value == self.cells[row][1].value == 
                self.cells[row][2].value != ""):
                return True
        
        for col in range(3):
            if (self.cells[0][col].value == self.cells[1][col].value == 
                self.cells[2][col].value != ""):
                return True
        
        if (self.cells[0][0].value == self.cells[1][1].value == 
            self.cells[2][2].value != ""):
            return True
        
        if (self.cells[0][2].value == self.cells[1][1].value == 
            self.cells[2][0].value != ""):
            return True
        
        return False
    
    def is_board_full(self):
        for row in range(3):
            for col in range(3):
                if self.cells[row][col].is_empty():
                    return False
        return True
    
    def draw(self):
        for row in range(3):
            for col in range(3):
                self.cells[row][col].draw()


game = True
clock = pygame.time.Clock()
tic_tac_toe = TicTacToeGame()


while game:
    mw.fill(BACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                mouse_x, mouse_y = event.pos
                tic_tac_toe.handle_click(mouse_x, mouse_y)
    
    tic_tac_toe.draw()
    
    if tic_tac_toe.game_over:
        if tic_tac_toe.winner == "Draw":
            result_text = Label(150, 10, 200, 30, BACK)
            result_text.set_text("Нічия!", 24, (100, 100, 100))
        else:
            result_text = Label(150, 10, 200, 30, BACK)
            if tic_tac_toe.winner == "X":
                result_text.set_text("Виграв хрестик", 30, (255, 0, 0))
            else:
                result_text.set_text("Виграв нулик", 30, (0, 0, 255))
        result_text.draw()
        
        restart_text = Label(120, 460, 260, 30, BACK)
        restart_text.set_text("Перезапусти гру", 36, (100, 100, 100))
        restart_text.draw()
    else:
        
        current_text = Label(150, 10, 200, 30, BACK)
        if tic_tac_toe.current_player == "X":
            current_text.set_text("Ходить хрестик", 30, (255, 0, 0))
        else:
            current_text.set_text("Ходить нулик", 30, (0, 0, 255))
        current_text.draw()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit() 