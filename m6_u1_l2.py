import pygame


# Визначення кольорів у форматі RGB
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Ініціалізація Pygame
pygame.init()


# Створення вікна розміром 500x500 пікселів
screen = pygame.display.set_mode((500, 500))


# Об'єкт для контролю частоти оновлення екрану (FPS)
clock = pygame.time.Clock()


# Змінна для основного циклу гри
running = True


# Клас, що описує гравця
class Player:
    def __init__(self, coord):
        # Створення поверхні для зображення гравця (квадрат 50x50 пікселів)
        self.image = pygame.Surface((50, 50))
        # Заповнення поверхні чорним кольором
        self.image.fill(BLACK)
        # Прямокутник, який задає позицію та розмір гравця
        self.rect = pygame.Rect(coord, (50,50))
        # Швидкість руху гравця по осях x та y
        self.speed = 5


    def update(self):
        # Отримання стану натиснутих клавіш
        keys = pygame.key.get_pressed()


        # Рух гравця вліво
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        # Рух гравця вправо
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # Рух гравця вгору
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        # Рух гравця вниз
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


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
        # Відображення гравця на заданій поверхні (екрані)
        surface.blit(self.image, (self.rect.x, self.rect.y))


# Створення гравця в початковій позиції (250, 400)
player = Player((250, 400))


# Основний цикл гри
while running:
    # Обробка подій (наприклад, натискання кнопки закриття вікна)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Завершення циклу, коли користувач закриває вікно


    # Заповнення екрану жовтим кольором
    screen.fill(YELLOW)
   
    # Оновлення позиції гравця відповідно до натиснутих клавіш
    player.update()
    # Відображення гравця на екрані
    player.draw(screen)


    # Оновлення екрану, щоб показати все намальоване за цей цикл
    pygame.display.flip()


    # Обмеження швидкості циклу до 50 кадрів в секунду
    clock.tick(50)


# Завершення роботи з Pygame
pygame.quit()
