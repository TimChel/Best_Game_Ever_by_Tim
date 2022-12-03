import pygame

WIDTH = 400
HEIGHT = 400
FPS = 200

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((100, 80))
#         self.image.fill(BLACK)
#
#         # self.image = pygame.image.load("p1_jump.png")
#         # self.image.set_colorkey(WHITE)
#
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT / 2)
#         self.prev_time = pygame.time.get_ticks()
#         self.speed_x = 0.5
#
#     def update(self):
#         curr_time = pygame.time.get_ticks()
#         dt = curr_time - self.prev_time
#         self.rect.x += self.speed_x * dt
#         if self.rect.right > WIDTH:
#             self.speed_x *= -1
#             self.rect.right = WIDTH - (self.rect.right - WIDTH)
#         if self.rect.left < 0:
#             self.speed_x *= -1
#             self.rect.left = abs(self.rect.left)
#         self.prev_time = curr_time


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)

# arial_font = pygame.font.SysFont("Arial", 20)
# text = arial_font.render("quit", True, WHITE)

running = True
start = 0
width_line = 10
start_radius = width_line
x, y = 3, 3
otnosh = 5
start_point_x = (1/2 + x*otnosh)*width_line
start_point_y = (1/2 + y*otnosh)*width_line
end_point_x = 0*otnosh*width_line
end_point_y = (1+y*otnosh)*width_line
vert_boarder = (1+y*otnosh)*width_line
hor_boarder = (1+x*otnosh)*width_line
while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((mouse_pos[0] - start_point_x)**2 + (mouse_pos[1] - start_point_y)**2)**(1/2) <= start_radius:
                start = 1
                knot = [start_point_x, start_point_y]

        if event.type == pygame.MOUSEBUTTONUP:
            start = 0


    all_sprites.update()
    # collisions = pygame.sprite.spritecollide(player, group_of_entites, False)

    screen.fill(GREEN)
    pygame.draw.rect(screen, GREY, [0, 0, (1 + x*otnosh)*width_line, (1 + y*otnosh)*width_line])
    for i in range(x):
        for j in range(y):
            pygame.draw.rect(screen, BLACK, [(1 + i*otnosh)*width_line, (1 + j*otnosh)*width_line, width_line*(otnosh-1), width_line*(otnosh-1)])
    # screen.blit(text, (WIDTH / 2 + 50, HEIGHT / 2 + 10))
    pygame.draw.circle(screen, GREY, [start_point_x, start_point_y], start_radius)
    pygame.draw.rect(screen, GREY, [end_point_x, end_point_y, width_line, width_line])
    pygame.draw.circle(screen, GREY, [end_point_x + width_line/2, end_point_y + width_line], width_line/2)
    if start == 1:
        pygame.draw.circle(screen, WHITE, [start_point_x, start_point_y], width_line)
        if (abs(mouse_pos[0] - knot[0]) <= abs(mouse_pos[1] - knot[1]) or mouse_pos[0] < 0 or mouse_pos[0] > hor_boarder) and mouse_pos[1] > 0 and mouse_pos[1] < vert_boarder:
                if mouse_pos[1] - knot[1] > 0:
                    pygame.draw.rect(screen, WHITE, [knot[0]-width_line/2, knot[1], width_line, abs(mouse_pos[1] - knot[1])])
                else:
                    pygame.draw.rect(screen, WHITE, [knot[0] - width_line/2, mouse_pos[1], width_line, abs(mouse_pos[1] - knot[1])])
        else:
            if mouse_pos[0] > 0 and mouse_pos[0] < hor_boarder:
                if mouse_pos[0] - knot[0] > 0:
                    pygame.draw.rect(screen, WHITE, [knot[0], knot[1] - width_line/2, abs(mouse_pos[0] - knot[0]), width_line])
                else:
                    pygame.draw.rect(screen, WHITE, [mouse_pos[0], knot[1] - width_line/2, abs(mouse_pos[0] - knot[0]), width_line])


    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()