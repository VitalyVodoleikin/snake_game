import pygame

size = [400, 600]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake_game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
