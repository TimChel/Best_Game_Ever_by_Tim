import pygame
from Планшетка import A

FPS = 200
running = True
WIDTH = 800
HEIGHT = 700

BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
global level_len
level_len = len(A)
global level
with open("Level.txt", mode="r") as f:
    f.seek(0)
    level = int(f.read())
while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        A[level].update_event(event, mouse_pos)
        if event.type == pygame.QUIT:
            running = False
    A[level].update(mouse_pos)
    pygame.display.flip()

pygame.quit()
