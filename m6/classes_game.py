class Button():
    def __init__(self, x, y, text, w):
        self.rect = pygame.Rect(x, y, w, 50)
        self.rect_image = pygame.Surface((w, 50))
        self.rect_image.fill(BLUE)
        self.rect_image_active = pygame.Surface((w, 50))
        self.rect_image_active.fill(GREEN)
        
        self.font = pygame.font.Font(None, 32)
        self.text_image = self.font.render(text, True, WHITE)
        self.text_rect = pygame.Rect(x, y, len(text)*20, 32)
        self.text_rect.centerx = self.rect.centerx
        self.text_rect.top = y + 5
        self.active = False
        self.fn = None
        self.activated = False

    def update(self):
        x, y = pygame.mouse.get_pos()
        collision = self.rect.collidepoint(x, y)
        click = pygame.mouse.get_pressed()[0]
        
        if not click and self.activated:
            self.activated = False
        
        if collision:
            self.active = True
            if click and self.fn and not self.activated:
                self.activated = True
                self.fn()
                
        else:
            self.active = False

    def draw(self, surface):
        if self.active:
            surface.blit(self.rect_image,(self.rect.x, self.rect.y))
        else:
            surface.blit(self.rect_image_active,(self.rect.x, self.rect.y))
        surface.blit(self.text_image, (self.text_rect.x, self.text_rect.y))

    def onclick(self, fn):
        self.fn = fn
class Sprite():
    def __init__(self, coord, color):
        # створення зображення-об'єкта (поверхня 100x100)
        self.image = pygame.Surface((100, 100))
        # заливка зображення вказаним кольором
        self.image.fill(color)
        # створення прямокутника (Rect) на основі координат і розміру
        self.rect = pygame.Rect(coord, (100, 100))
        # швидкість руху по осі x та y
        self.dx = 0
        self.dy = 0


    def update(self):
        return None
        # оновлення позиції: рух по x
        self.rect.centerx += self.dx
        # перевірка на зіткнення з правою межею вікна
        if self.rect.right > 500:
            self.dx = -2  # змінити напрямок руху вліво
        # перевірка на зіткнення з лівою межею вікна
        elif self.rect.left < 0:
            self.dx = 2   # змінити напрямок руху вправо


    def draw(self, surface):
        # відображення зображення (image) на екрані
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, coord):
        # Створення поверхні для зображення гравця (квадрат 50x50 пікселів)
        super().__init__((coord), BLACK)
        
        self.dy = 5
        self.dx = 5


    def update(self):
        # Отримання стану натиснутих клавіш
        keys = pygame.key.get_pressed()

        # Рух гравця вліво
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.dx
        # Рух гравця вправо
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.dx
        # Рух гравця вгору
        if keys[pygame.K_UP]:
            self.rect.y -= self.dy
        # Рух гравця вниз
        if keys[pygame.K_DOWN]:
            self.rect.y += self.dy


        # Обмеження руху гравця межами вікна - не виходити за лівий край
        if self.rect.left < 0:
            self.rect.left = 0
        # не виходити за правий край
        if self.rect.right > 500:
            self.rect.right = 500
        # не виходити за верхній край
        if self.rect.top < 0:
            self.rect.top = 0
        # не виходити за нижній край
        if self.rect.bottom > 500:
            self.rect.bottom = 500


    def draw(self, surface):
        super().draw(surface)

class Label:
    def __init__(self, x, y, w, h, color, text_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text_color = text_color
        self.text = ""
        self.font = pygame.font.Font(None, 32)

    def set_text(self, text, font_size, color, text_color):
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.text_color = text_color
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_image = self.font.render(self.text, True, self.text_color)
        screen.blit(text_image, (self.rect.x + 10, self.rect.y + 10))
