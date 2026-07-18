import pygame

# Некоторые цвета
FRAME_COLOR = (0, 255, 205)  # Цвет рамки
HEADER_COLOR = (0, 205, 155)
WHITE = (255, 255, 255)
BLUE = (205, 255, 255)

# Некоторые размеры
SIZE_BLOCK = 20  # Габариты 1 блока/клетки
COUNT_BLOCKS = 20  # Кол-во блоков по длине и ширине
MARGIN = 1  # Линия разделения блоков
HEADER_MARGIN = 100  # Информационное табло
# Размеры окна
size = [
    SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * SIZE_BLOCK,
    SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * SIZE_BLOCK + HEADER_MARGIN
]
print(size)

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
    pygame.draw.rect(screen, HEADER_COLOR, (0, 0, size[0], HEADER_MARGIN))

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
                    SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                    HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                    SIZE_BLOCK,
                    SIZE_BLOCK
                )
            )

    pygame.display.flip()

# # ==========
# При размере блока в 20 пикселей
# общие габариты окна выходят на
# [460, 560] пикселей
