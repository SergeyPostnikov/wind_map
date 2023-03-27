import pygame
from wind_field import generate_wind_field, get_square_points

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Установка размера окна
size = (500, 500)
screen = pygame.display.set_mode(size)

# Установка заголовка окна
pygame.display.set_caption("Стрелка в центре")


class Arrow(pygame.sprite.Sprite):
    def __init__(self, angle, size, x, y):
        super().__init__()
    
        self.image = pygame.Surface([size, size])
        self.image.fill(WHITE)
        pygame.draw.line(self.image, BLACK, [size/2, size/2], [size/2, size/10], int(size/6))
        pygame.draw.line(self.image, BLACK, [size/2, size/10], [size*0.6/2, size*0.4/2], int(size/6))
        pygame.draw.line(self.image, BLACK, [size/2, size/10], [size*0.4/2, size*0.4/2], int(size/6))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.image = pygame.transform.rotate(self.image, angle)


arrow = Arrow(45, 50, 250, 250)


# Создание группы спрайтов и добавление стрелки в эту группу
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(arrow)

# Цикл игры
done = False
while not done:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Обновление экрана
    all_sprites_group.update()
    screen.fill(WHITE)
    all_sprites_group.draw(screen)
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
