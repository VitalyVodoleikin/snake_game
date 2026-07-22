from email.policy import default

import pygame
import pygame_menu
import random
import sys

from pygame_menu.examples.other.image_background import surface

# Инициализация игры
pygame.init()

# Лого
bg_image = pygame.image.load("snake_logo.jpg")

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

courier = pygame.font.SysFont("courier", 36)  # Ссылка на шрифт


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


def start_the_game():
    """
    Главная функция игры.
    """

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

    snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_random_empty_block()

    # Задание направлений движения
    d_row = buf_row = 0
    d_col = buf_col = 1

    # Счетчик очков игры
    total = 0

    # Скорость игры
    speed = 1

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
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:  # Вниз
                    buf_row = 1
                    buf_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:  # Влево
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:  # Вправо
                    buf_row = 0
                    buf_col = 1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, (0, 0, size[0], HEADER_MARGIN))

        # Создание текстов для отрисовки счета и скорости на табло
        text_total = courier.render(f"Total: {total}", 0, WHITE)
        text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
        # Прикрепление текста к экрану
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK + 250, SIZE_BLOCK))

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
            # pygame.quit()
            # sys.exit()
            break

        draw_block(RED, apple.x, apple.y)  # Отрисовка яблока

        # Отрисовка змейки на поле
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)

        pygame.display.flip()  # Перезаливка экрана

        # Змейка съедает яблоко
        if apple == head:
            total += 1
            speed = total // 5 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()

        # Обработка отрисовки движения змейки при поворотах
        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            print("Crash yourself")
            # pygame.quit()
            # sys.exit()
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        timer.tick(2 + speed)  # Скорость обновления экрана


# Загрузка меню
main_theme = theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.65)

menu = pygame_menu.Menu("Snake_game", 260, 220, theme=main_theme)

menu.add.text_input("Имя: ", default="Игрок 1")
menu.add.button("Играть", start_the_game)
menu.add.button("Выход", pygame_menu.events.EXIT)

while True:

    screen.blit(bg_image, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()

# # ==========
# При размере блока в 20 пикселей
# общие габариты окна выходят на
# [460, 560] пикселей
