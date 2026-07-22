import pygame
import random
import sys

# Некоторые цвета
FRAME_COLOR = (0, 255, 205)  # Цвет рамки
HEADER_COLOR = (0, 205, 155)
WHITE = (255, 255, 255)
BLUE = (205, 255, 255)
SNAKE_COLOR = (0, 105, 0)  # Цвет змейки
RED = (225, 0, 0)  # APPLE_COLOR

# Некоторые размеры
SIZE_BLOCK = 20  # Габариты 1 блока/клетки
COUNT_BLOCKS = 20  # Кол-во блоков по длине и ширине
MARGIN = 1  # Линия разделения блоков
HEADER_MARGIN = 100  # Информационное табло
# Размеры окна
size = [
    SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
    SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN
]
print(size)

# Создание окна
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake_game")

# Скорость движения (отрисовки кадров)
timer = pygame.time.Clock()


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        """
        Проверка того, чтобы змейка не ушла за пределы игрового поля.
        """
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        """
        Логика для сравнения двух экземпляров класса.
        """
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def get_random_empty_block():
    """
    Функция перемещения яблока в случайную пустую ячейку.
    """
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = SnakeBlock(x, y)
    # Генерировать координаты до тех пор,
    # пока не получатся координаты пустой ячейки
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
        empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block


def draw_block(color, row, column):
    """
    Функция отрисовки блока.
    """
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


snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
apple = get_random_empty_block()

# Задание направлений движения
d_row = 0
d_col = 1

# Игровой цикл
while True:

    # Обработка нажатия клавиш
    for event in pygame.event.get():
        # Закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Управление клавишами
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:  # Вверх
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:  # Вниз
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:  # Влево
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:  # Вправо
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, (0, 0, size[0], HEADER_MARGIN))

    # Отрисовка поля
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, column)

    # Проверка столкновения головы змейки с краем поля
    head = snake_blocks[-1]
    if not head.is_inside():
        print("Crash")
        pygame.quit()
        sys.exit()

    draw_block(RED, apple.x, apple.y)  # Отрисовка яблока

    # Отрисовка змейки на поле
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    if apple == head:
        apple = get_random_empty_block()

    # Обработка отрисовки движения змейки при поворотах
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip()  # Перезаливка экрана
    timer.tick(3)  # Скорость обновления экрана

# # ==========
# При размере блока в 20 пикселей
# общие габариты окна выходят на
# [460, 560] пикселей
