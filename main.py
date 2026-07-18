import pygame

# Некоторые цвета
FRAME_COLOR = (0, 255, 205)  # Цвет рамки
WHITE = (255, 255, 255)
BLUE = (205, 255, 255)

# Некоторые размеры
size = [500, 600]  # Размеры окна
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIT = 1

# Создание окна
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake_game")

# Игровой цикл
while True:

    # Закрытие окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)

    # Отрисовка поля
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(
                screen,
                color,
                (
                    10 + column * SIZE_BLOCK + MARGIT * (column + 1),
                    20 + row * SIZE_BLOCK + MARGIT * (row + 1),
                    SIZE_BLOCK, SIZE_BLOCK)
            )

    pygame.display.flip()
