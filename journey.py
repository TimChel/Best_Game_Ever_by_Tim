import pygame
import os


pygame.init()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
running = True


# world setup
x = 250
y = 250


knight_frames = ["knight_f_idle_anim_f0", "knight_f_run_anim_f0", "knight_f_run_anim_f1", "knight_f_run_anim_f2"]
player = pygame.image.load(os.path.join("frames/" + knight_frames[0] + ".png"))
player = pygame.transform.scale(player, (128, 128))
curr_frame = 0
steps_delay_init = 50
steps_delay = steps_delay_init


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    step = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        step = True
        y = y - 1
    if keys[pygame.K_DOWN]:
        step = True
        y = y + 1
    if keys[pygame.K_LEFT]:
        step = True
        x = x - 1
    if keys[pygame.K_RIGHT]:
        step = True
        x = x + 1
    if step == False:
        curr_frame = 0
        player = pygame.image.load(os.path.join("frames/" + knight_frames[curr_frame] + ".png"))
        player = pygame.transform.scale(player, (128, 128))

    screen.fill((255, 255, 255))

    screen.blit(player, (x, y))

    if step == True:
        steps_delay -= 1

    if steps_delay == 0:
        steps_delay = steps_delay_init
        curr_frame = (curr_frame + 1) % len(knight_frames)
        player = pygame.image.load(os.path.join("frames/" + knight_frames[curr_frame] + ".png"))
        player = pygame.transform.scale(player, (128, 128))

    pygame.display.flip()

pygame.quit()
