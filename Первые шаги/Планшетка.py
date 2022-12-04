import pygame

WIDTH = 1000
HEIGHT = 800
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
width_line = 20
start_radius = width_line
x, y = 4, 4
setka = [[0 for j in range(y)] for i in range(x)]
otnosh = 5
start_x = 1
start_y = 1
start_point_x = (1/2 + start_x*otnosh)*width_line
start_point_y = (1/2 + start_y*otnosh)*width_line
end_point_x = 0*otnosh*width_line
end_point_y = (1+y*otnosh)*width_line
vert_boarder = (1+y*otnosh)*width_line
hor_boarder = (1+x*otnosh)*width_line
knot_flag = 0
knot_list = []
direction_list = []
tablet_board = [[0, hor_boarder], [0, vert_boarder]]
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
                setka[start_x][start_y] = 1
                knot = [start_point_x, start_point_y]
                pos_0_x = mouse_pos[0]
                pos_0_y = mouse_pos[1]
                knot_flag = 1
                direction_flag = -1
                list_rect = []
                list_circle = []
                direction_list = []
                knot_list = []
                knot_list.append([knot[0], knot[1]])

        if event.type == pygame.MOUSEBUTTONUP:
            start = 0
            knot_flag = 0


    all_sprites.update()
    # collisions = pygame.sprite.spritecollide(player, group_of_entites, False)

    screen.fill(GREEN)
    pygame.draw.rect(screen, GREY, [0, 0, hor_boarder, vert_boarder])
    for i in range(x):
        for j in range(y):
            pygame.draw.rect(screen, BLACK, [(1 + i*otnosh)*width_line, (1 + j*otnosh)*width_line, width_line*(otnosh-1), width_line*(otnosh-1)])
    pygame.draw.circle(screen, GREY, [start_point_x, start_point_y], start_radius)
    pygame.draw.rect(screen, GREY, [end_point_x, end_point_y, width_line, width_line])
    pygame.draw.circle(screen, GREY, [end_point_x + width_line/2, end_point_y + width_line], width_line/2)
    if start == 1:
        pygame.draw.circle(screen, WHITE, [start_point_x, start_point_y], width_line)
        if knot_flag == 1 and (abs(mouse_pos[0] - pos_0_x) >= width_line/2 or abs(mouse_pos[1] - pos_0_y) >= width_line/2):
            if abs(mouse_pos[0] - pos_0_x) <= abs(mouse_pos[1] - pos_0_y):
                if mouse_pos[1] - pos_0_y < 0 and knot[1] + (mouse_pos[1] - pos_0_y) > tablet_board[1][0]:
                    if len(direction_list) != 0 and direction_list[-1] == 3:
                        del knot_list[-1]
                        del list_rect[-1]
                        del list_circle[-1]
                        del direction_list[-1]
                        knot = [knot_list[-1][0], knot_list[-1][1]]
                        pos_0_y = pos_0_y - otnosh*width_line
                        direction_flag = 3
                    else:
                        direction_flag = 1
                elif mouse_pos[1] - pos_0_y > 0 and knot[1] + (mouse_pos[1] - pos_0_y) < tablet_board[1][1]:
                    if len(direction_list) != 0 and direction_list[-1] == 1:
                        del knot_list[-1]
                        del list_rect[-1]
                        del list_circle[-1]
                        del direction_list[-1]
                        knot = [knot_list[-1][0], knot_list[-1][1]]
                        pos_0_y = pos_0_y + otnosh * width_line
                        direction_flag = 1
                    else:
                        direction_flag = 3
                else:
                    pos_0_x, pos_0_y = mouse_pos[0], mouse_pos[1]
            else:
                if mouse_pos[0] - pos_0_x > 0 and knot[0] + (mouse_pos[0] - pos_0_x) < tablet_board[0][1]:
                    if len(direction_list) != 0 and direction_list[-1] == 4:
                        del knot_list[-1]
                        del list_rect[-1]
                        del list_circle[-1]
                        del direction_list[-1]
                        knot = [knot_list[-1][0], knot_list[-1][1]]
                        pos_0_x = pos_0_x + otnosh * width_line
                        direction_flag = 4
                    else:
                        direction_flag = 2
                elif mouse_pos[0] - pos_0_x < 0 and knot[0] + (mouse_pos[0] - pos_0_x) > tablet_board[0][0]:
                    if len(direction_list) != 0 and direction_list[-1] == 2:
                        del knot_list[-1]
                        del list_rect[-1]
                        del list_circle[-1]
                        del direction_list[-1]
                        knot = [knot_list[-1][0], knot_list[-1][1]]
                        pos_0_x = pos_0_x - otnosh * width_line
                        direction_flag = 2
                    else:
                        direction_flag = 4
                else:
                    pos_0_x, pos_0_y = mouse_pos[0], mouse_pos[1]
            knot_flag = 0

        if knot_flag == 0:
            if direction_flag == 1:
                if [knot[0], knot[1]-otnosh*width_line] in knot_list and pos_0_y - mouse_pos[1] > (otnosh -3/2)*width_line:
                    pos_0_y = mouse_pos[1] + (otnosh - 3/2)*width_line
                pygame.draw.rect(screen, WHITE,
                                     [knot[0] - width_line / 2, knot[1] - (pos_0_y - mouse_pos[1]), width_line,
                                     pos_0_y - mouse_pos[1]])
                pygame.draw.circle(screen, WHITE, [knot[0], knot[1] - (pos_0_y - mouse_pos[1])], width_line / 2)
                if pos_0_y - mouse_pos[1] > (otnosh - 1/2)*width_line and [knot[0], knot[1]-otnosh*width_line] not in knot_list:
                    list_rect.append([knot[0] - width_line / 2, knot[1]-otnosh*width_line, width_line,  otnosh*width_line])
                    list_circle.append([knot[0], knot[1]-otnosh*width_line])
                    direction_list.append(direction_flag)
                    knot_flag = 1
                    knot[1] -= otnosh*width_line
                    pos_0_y = mouse_pos[1]
                    pos_0_x = mouse_pos[0]
                    knot_list.append([knot[0], knot[1]])
                elif pos_0_y - mouse_pos[1] < width_line/2:
                    knot_flag = 1
                    pos_0_x = mouse_pos[0]
            elif direction_flag == 2:
                if [knot[0]+otnosh*width_line, knot[1]] in knot_list and -pos_0_x + mouse_pos[0] > (otnosh -3/2)*width_line:
                    pos_0_x = mouse_pos[0] - (otnosh - 3/2)*width_line
                pygame.draw.rect(screen, WHITE,
                                 [knot[0], knot[1] - width_line / 2, mouse_pos[0] - pos_0_x, width_line])
                pygame.draw.circle(screen, WHITE, [knot[0] + mouse_pos[0] - pos_0_x, knot[1]], width_line / 2)
                if - pos_0_x + mouse_pos[0] > (otnosh - 1/2)*width_line:
                    list_rect.append([knot[0], knot[1] - width_line / 2, otnosh*width_line, width_line])
                    list_circle.append([knot[0] + otnosh * width_line, knot[1]])
                    direction_list.append(direction_flag)
                    knot_flag = 1
                    knot[0] += otnosh*width_line
                    pos_0_y = mouse_pos[1]
                    pos_0_x = mouse_pos[0]
                    knot_list.append([knot[0], knot[1]])
                elif - pos_0_x - mouse_pos[0] < width_line/2:
                    knot_flag = 1
                    pos_0_y = mouse_pos[1]
            elif direction_flag == 3:
                if [knot[0], knot[1]+otnosh*width_line] in knot_list and -pos_0_y + mouse_pos[1] > (otnosh -3/2)*width_line:
                    pos_0_y = mouse_pos[1] - (otnosh - 3/2)*width_line
                pygame.draw.rect(screen, WHITE,
                                 [knot[0] - width_line / 2, knot[1], width_line, mouse_pos[1] - pos_0_y])
                pygame.draw.circle(screen, WHITE, [knot[0], knot[1] + (-pos_0_y + mouse_pos[1])], width_line / 2)
                if - pos_0_y + mouse_pos[1] > (otnosh - 1/2)*width_line:
                    list_rect.append([knot[0] - width_line / 2, knot[1], width_line, otnosh*width_line])
                    list_circle.append([knot[0], knot[1] + otnosh * width_line])
                    direction_list.append(direction_flag)
                    knot_flag = 1
                    knot[1] += otnosh*width_line
                    pos_0_y = mouse_pos[1]
                    pos_0_x = mouse_pos[0]
                    knot_list.append([knot[0], knot[1]])
                elif - pos_0_y + mouse_pos[1] < width_line/2:
                    knot_flag = 1
                    pos_0_x = mouse_pos[0]
            elif direction_flag == 4:
                if [knot[0]-otnosh*width_line, knot[1]] in knot_list and pos_0_x - mouse_pos[0] > (otnosh -3/2)*width_line:
                    pos_0_x = mouse_pos[0] + (otnosh - 3/2)*width_line
                pygame.draw.rect(screen, WHITE,
                                 [knot[0] - (pos_0_x - mouse_pos[0]), knot[1] - width_line / 2, pos_0_x - mouse_pos[0], width_line])
                pygame.draw.circle(screen, WHITE, [knot[0] - (-mouse_pos[0] + pos_0_x), knot[1]], width_line / 2)
                if pos_0_x - mouse_pos[0] > (otnosh - 1/2)*width_line:
                    list_rect.append([knot[0] - otnosh*width_line, knot[1] - width_line / 2, otnosh*width_line, width_line])
                    list_circle.append([knot[0] - otnosh * width_line, knot[1]])
                    direction_list.append(direction_flag)
                    knot_flag = 1
                    knot[0] -= otnosh*width_line
                    pos_0_y = mouse_pos[1]
                    pos_0_x = mouse_pos[0]
                    knot_list.append([knot[0], knot[1]])
                elif pos_0_x - mouse_pos[0] < width_line/2:
                    knot_flag = 1
                    pos_0_y = mouse_pos[1]
        for i in list_rect:
            pygame.draw.rect(screen, WHITE, i)
        for i in list_circle:
            pygame.draw.circle(screen, WHITE, i, width_line/2)

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()