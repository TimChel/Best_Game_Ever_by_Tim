import pygame

WIDTH = 600
HEIGHT = 500
FPS = 200

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
WHITE_minor = (180, 180, 180)

base_color = WHITE
next_color = GREEN
current_color = base_color
change_every_x_seconds = 1/3
number_of_steps = change_every_x_seconds * FPS
step = 1


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


arial_font = pygame.font.SysFont("Arial", 20)
text = arial_font.render("quit", True, WHITE)

running = True
start = 0
width_line = 20
start_radius = width_line
nachalo_x = 100
nachalo_y = 100
x, y = 3, 3
otnosh = 4
vert_boarder = (1+y*otnosh)*width_line
hor_boarder = (1+x*otnosh)*width_line
flag_end = 0
knot_flag = 0
knot_list = []
direction_list = []
tablet_board = [[nachalo_x, nachalo_x+hor_boarder], [nachalo_y, nachalo_y+vert_boarder]]
start_list = [[1, 1], [2,2]]
start_point_list = []
for i, j in start_list:
    start_point_list.append([(1/2 + i*otnosh)*width_line + nachalo_x, (1/2 + j*otnosh)*width_line + nachalo_y])
end_list = [[3, 0, y], [1, x, 0], [4, 0, 0]]
end_point_list = []
for i, j, k in end_list:
    end_point_list.append([i, (1/2 + j*otnosh)*width_line + nachalo_x, (1/2 + k*otnosh)*width_line + nachalo_y])
crack_list = [[2, 0, 0], [3, 0, 0], [2, 1, 1], [3, 1, 1]]
crack_point_list = []
for i, j, k in crack_list:
    crack_point_list.append([i, (1/2 + j*otnosh)*width_line + nachalo_x, (1/2 + k*otnosh)*width_line + nachalo_y])

while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:

        if event.type == pygame.MOUSEBUTTONDOWN:
            for start_point in start_point_list:
                if ((mouse_pos[0] - start_point[0]) ** 2 + (mouse_pos[1] - start_point[1]) ** 2) ** (
                        1 / 2) <= start_radius and start == 0:
                    start = 1
                    knot = [start_point[0], start_point[1]]
                    pos_0_x = mouse_pos[0]
                    pos_0_y = mouse_pos[1]
                    knot_flag = 1
                    direction_flag = -1
                    list_rect = []
                    list_circle = []
                    direction_list = []
                    knot_list = [[knot[0], knot[1]]]
                    flag_end = 0

        if event.type == pygame.MOUSEBUTTONUP:
            start = 0
            knot_flag = 0
            base_color = WHITE
            next_color = GREEN
            current_color = base_color
            if flag_end == 1:
                print("Win")

    screen.fill(BLACK)
    pygame.draw.rect(screen, GREY, [nachalo_x, nachalo_y, hor_boarder, vert_boarder], border_radius=width_line//2)
    for i in range(x):
        for j in range(y):
            pygame.draw.rect(screen, BLACK, [(1 + i*otnosh)*width_line + nachalo_x, (1 + j*otnosh)*width_line + nachalo_y, width_line*(otnosh-1), width_line*(otnosh-1)])
    for start_point in start_point_list:
        pygame.draw.circle(screen, GREY, [start_point[0], start_point[1]], start_radius)
    for end_point in end_point_list:
        if end_point[0] == 1:
            pygame.draw.rect(screen, GREY, [end_point[1] - width_line / 2, end_point[2] - width_line, width_line,
                                            3 / 2 * width_line])
            pygame.draw.circle(screen, GREY,
                               [end_point[1], end_point[2] - width_line], width_line / 2)
        elif end_point[0] == 2:
            pygame.draw.rect(screen, GREY, [end_point[1] - width_line / 2, end_point[2] - width_line/2, 3/2*width_line,
                                            width_line])
            pygame.draw.circle(screen, GREY,
                               [end_point[1] + width_line, end_point[2]], width_line / 2)
        elif end_point[0] == 3:
            pygame.draw.rect(screen, GREY, [end_point[1] - width_line / 2, end_point[2] - width_line / 2, width_line,
                                            3 / 2 * width_line])
            pygame.draw.circle(screen, GREY, [end_point[1], end_point[2] + width_line], width_line / 2)
        elif end_point[0] == 4:
            pygame.draw.rect(screen, GREY,
                             [end_point[1] - width_line, end_point[2] - width_line / 2, 3 / 2 * width_line,
                              width_line])
            pygame.draw.circle(screen, GREY,
                               [end_point[1] - width_line, end_point[2]], width_line / 2)
    for crack_point in crack_point_list:
        if crack_point[0] == 3:
            pygame.draw.rect(screen, BLACK, [crack_point[1]-width_line/2, crack_point[2] + otnosh*width_line/2 - width_line/4, width_line, width_line/2])
        if crack_point[0] == 2:
            pygame.draw.rect(screen, BLACK, [crack_point[1] + otnosh*width_line/2 - width_line/4, crack_point[2] - width_line/2, width_line/2, width_line])
    if start == 1:
        pygame.draw.circle(screen, current_color, knot_list[0], width_line)
        if knot_flag == 1 and (abs(mouse_pos[0] - pos_0_x) >= width_line/2 or abs(mouse_pos[1] - pos_0_y) >= width_line/2):
            if abs(mouse_pos[0] - pos_0_x) <= abs(mouse_pos[1] - pos_0_y):
                if mouse_pos[1] - pos_0_y < 0 and (knot[1] + (mouse_pos[1] - pos_0_y) > tablet_board[1][0] or [1, *knot] in end_point_list):
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
                elif mouse_pos[1] - pos_0_y > 0 and (knot[1] + (mouse_pos[1] - pos_0_y) < tablet_board[1][1] or [3, *knot] in end_point_list):
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
                if mouse_pos[0] - pos_0_x > 0 and (knot[0] + (mouse_pos[0] - pos_0_x) < tablet_board[0][1] or [2, *knot] in end_point_list):
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
                elif mouse_pos[0] - pos_0_x < 0 and (knot[0] + (mouse_pos[0] - pos_0_x) > tablet_board[0][0] or [4, *knot] in end_point_list):
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
        elif knot_flag == 1:
            if abs(mouse_pos[0] - pos_0_x) <= abs(mouse_pos[1] - pos_0_y) and \
                    ((knot[1] + (mouse_pos[1] - pos_0_y) > tablet_board[1][0] + width_line/2  or [1, *knot] in end_point_list) and \
                     (knot[1] + (mouse_pos[1] - pos_0_y) < tablet_board[1][1] - width_line/2) or [3, *knot] in end_point_list):
                pygame.draw.circle(screen, current_color, [knot[0], knot[1] - (pos_0_y - mouse_pos[1])], width_line / 2)
                pygame.draw.circle(screen, current_color, [knot[0], knot[1] - (pos_0_y - mouse_pos[1])/2], width_line / 2)
            elif abs(mouse_pos[0] - pos_0_x) >= abs(mouse_pos[1] - pos_0_y) and\
                    (knot[0] + (mouse_pos[0] - pos_0_x) < tablet_board[0][1] - width_line/2 or [2, *knot] in end_point_list) and \
                    (knot[0] + (mouse_pos[0] - pos_0_x) > tablet_board[0][0] + width_line/2 or [4, *knot] in end_point_list):
                pygame.draw.circle(screen, current_color, [knot[0] + mouse_pos[0] - pos_0_x, knot[1]], width_line / 2)
                pygame.draw.circle(screen, current_color, [knot[0] + (mouse_pos[0] - pos_0_x)/2, knot[1]], width_line / 2)

        if knot_flag == 0:
            if direction_flag == 1:
                if [knot[0], knot[1]-otnosh*width_line] in knot_list and pos_0_y - mouse_pos[1] > (otnosh -3/2)*width_line:
                    pos_0_y = mouse_pos[1] + (otnosh - 3/2)*width_line

                if [3, knot[0], knot[1] - otnosh*width_line] in crack_point_list and pos_0_y - mouse_pos[1] + width_line/2 > (otnosh*width_line/2 - width_line/4):
                    pos_0_y = mouse_pos[1] + otnosh*width_line/2 - width_line/4 - width_line/2

                if [1, *knot] in end_point_list and pos_0_y - mouse_pos[1] >= 1*width_line:
                    pos_0_y = mouse_pos[1] + 1*width_line
                    flag_end = 1
                else:
                    flag_end = 0

                pygame.draw.rect(screen, current_color,
                                     [knot[0] - width_line / 2, knot[1] - (pos_0_y - mouse_pos[1]), width_line,
                                     pos_0_y - mouse_pos[1]])
                pygame.draw.circle(screen, current_color, [knot[0], knot[1] - (pos_0_y - mouse_pos[1])], width_line / 2)

                if pos_0_y - mouse_pos[1] > (otnosh )*width_line:
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
                if ([knot[0]+otnosh*width_line, knot[1]] in knot_list and -pos_0_x + mouse_pos[0] > (otnosh -3/2)*width_line):
                    pos_0_x = mouse_pos[0] - (otnosh - 3/2)*width_line

                if [2, *knot] in crack_point_list and -pos_0_x + mouse_pos[0] + width_line/2 > (otnosh*width_line/2 - width_line/4):
                    pos_0_x = mouse_pos[0] - otnosh*width_line/2 + width_line/4 + width_line/2

                if [2, *knot] in end_point_list and -pos_0_x + mouse_pos[0] >= 1*width_line:
                    pos_0_x = mouse_pos[0] - 1*width_line
                    flag_end = 1
                else:
                    flag_end = 0

                pygame.draw.rect(screen, current_color,
                                 [knot[0], knot[1] - width_line / 2, mouse_pos[0] - pos_0_x, width_line])
                pygame.draw.circle(screen, current_color, [knot[0] + mouse_pos[0] - pos_0_x, knot[1]], width_line / 2)

                if - pos_0_x + mouse_pos[0] > (otnosh )*width_line:
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

                if [3, *knot] in crack_point_list and -pos_0_y + mouse_pos[1] + width_line/2 > (otnosh*width_line/2 - width_line/4):
                    pos_0_y = mouse_pos[1] - otnosh*width_line/2 + width_line/4 + width_line/2

                if [3, *knot] in end_point_list and -pos_0_y + mouse_pos[1] >= 1*width_line:
                    pos_0_y = mouse_pos[1] - 1*width_line
                    flag_end = 1
                else:
                    flag_end = 0

                pygame.draw.rect(screen, current_color,
                                 [knot[0] - width_line / 2, knot[1], width_line, mouse_pos[1] - pos_0_y])
                pygame.draw.circle(screen, current_color, [knot[0], knot[1] + (-pos_0_y + mouse_pos[1])], width_line / 2)

                if - pos_0_y + mouse_pos[1] > (otnosh )*width_line:
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

                if [2, knot[0] - otnosh*width_line, knot[1]] in crack_point_list and pos_0_x - mouse_pos[0] + width_line/2 > (otnosh*width_line/2 - width_line/4):
                    pos_0_x = mouse_pos[0] + otnosh*width_line/2 - width_line/4 - width_line/2

                if [4, *knot] in end_point_list and pos_0_x - mouse_pos[0] >= 1*width_line:
                    pos_0_x = mouse_pos[0] + 1*width_line
                    flag_end = 1
                else:
                    flag_end = 0

                pygame.draw.rect(screen, current_color,
                                 [knot[0] - (pos_0_x - mouse_pos[0]), knot[1] - width_line / 2, pos_0_x - mouse_pos[0], width_line])
                pygame.draw.circle(screen, current_color, [knot[0] - (-mouse_pos[0] + pos_0_x), knot[1]], width_line / 2)

                if pos_0_x - mouse_pos[0] > (otnosh )*width_line:
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
            pygame.draw.rect(screen, current_color, i)

        for i in list_circle:
            pygame.draw.circle(screen, current_color, i, width_line/2)

    if flag_end == 1:
        step += 1
        if step < number_of_steps:
            # (y-x)/number_of_steps calculates the amount of change per step required to
            # fade one channel of the old color to the new color
            # We multiply it with the current step counter
            current_color = [x + (((y - x) / number_of_steps) * step) for x, y in
                             zip(pygame.color.Color(base_color), pygame.color.Color(next_color))]
        else:
            step = 1
            base_color, next_color = next_color, base_color
    else:
        base_color = WHITE
        next_color = GREEN
        current_color = base_color

    pygame.display.flip()

pygame.quit()