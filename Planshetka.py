import pygame

class Tablet():
    def __init__(self, FPS, BASE, PATH, SECOND_BASE, PATH_MAX, x, y, start_list, end_list, crack_list, point_required_list, square_list, star_list):
        pygame.mixer.init()
        self.panel_path_complete = pygame.mixer.Sound("Первые шаги/panel_path_complete-fix.ogg")
        self.panel_path_complete.set_volume(0.5)
        self.panel_start_tracing = pygame.mixer.Sound("Первые шаги/panel_start_tracing-fix.ogg")
        self.panel_start_tracing.set_volume(0.5)
        self.panel_success2 = pygame.mixer.Sound("Первые шаги/panel_success2-fix.ogg")
        self.panel_success2.set_volume(0.5)
        self.panel_abort_tracing = pygame.mixer.Sound("Первые шаги/panel_abort_tracing-fix.ogg")
        self.panel_abort_tracing.set_volume(0.5)
        self.panel_abort_finish_tracing = pygame.mixer.Sound("Первые шаги/panel_abort_finish_tracing-fix_1.ogg")
        self.panel_abort_finish_tracing.set_volume(0.5)
        self.panel_finish_tracing = pygame.mixer.Sound("Первые шаги/panel_finish_tracing-fix.ogg")
        self.panel_finish_tracing.set_volume(0.5)
        self.panel_failure = pygame.mixer.Sound("Первые шаги/panel_failure-fix.ogg")
        self.panel_failure.set_volume(0.5)
        self.tracing_step = 0
        self.tracing_timer = 600
        self.tracing_circle = 0

        self.FPS = FPS
        self.BLACK = (0, 0, 0)
        self.GREY = (128, 128, 128)
        self.GREEN = (0, 255, 0)
        self.WHITE = (255, 255, 255)
        self.WHITE_minor = (180, 180, 180)
        self.BASE = BASE
        self.PATH = PATH
        self.SECOND_BASE = SECOND_BASE
        self.PATH_MAX = PATH_MAX
        self.ORANGE = (255, 165, 0)
        self.VIOLET = (148, 0, 211)

        self.base_color = self.SECOND_BASE
        self.next_color = self.PATH_MAX
        self.current_color = self.base_color
        self.change_every_x_seconds = 1/4
        self.number_of_steps = self.change_every_x_seconds * self.FPS
        self.step = 1

        self.change_every_x_seconds1 = 1
        self.number_of_steps1 = self.change_every_x_seconds1 * self.FPS

        self.start = 0
        self.width_line = 20
        self.start_radius = self.width_line
        self.x, self.y = x, y
        self.otnosh = 4
        self.nachalo_x = pygame.display.Info().current_w//2 - (x*self.otnosh*self.width_line + self.otnosh)//2
        self.nachalo_y = pygame.display.Info().current_h//2 - (y*self.otnosh*self.width_line + self.otnosh)//2
        self.vert_boarder = (1 + self.y * self.otnosh) * self.width_line
        self.hor_boarder = (1 + self.x * self.otnosh) * self.width_line
        self.flag_chek = 0
        self.flag_end = 0
        self.flag_end_sound = 0
        self.knot_flag = 0
        self.knot_list = []
        self.direction_list = []
        self.tablet_board = [(self.nachalo_x, self.nachalo_x + self.hor_boarder), [self.nachalo_y, self.nachalo_y + self.vert_boarder]]
        self.start_list = start_list
        self.start_point_list = []
        for i, j in self.start_list:
            self.start_point_list.append(
                [(1 / 2 + i * self.otnosh) * self.width_line + self.nachalo_x, (1 / 2 + j * self.otnosh) * self.width_line + self.nachalo_y])
        self.end_list = end_list
        self.end_point_list = []
        for i, j, k in self.end_list:
            self.end_point_list.append(
                [i, (1 / 2 + j * self.otnosh) * self.width_line + self.nachalo_x, (1 / 2 + k * self.otnosh) * self.width_line + self.nachalo_y])
        # self.crack_list = [[2, 0, 0], [3, 0, 0]]
        self.crack_list = crack_list
        self.crack_point_list = []
        for i, j, k in self.crack_list:
            self.crack_point_list.append(
                [i, (1 / 2 + j * self.otnosh) * self.width_line + self.nachalo_x, (1 / 2 + k * self.otnosh) * self.width_line + self.nachalo_y])
        self.point_required_list = point_required_list
        self.point_required_point_list = []
        self.point_required_chek = []
        for i in self.point_required_list:
            if i[0] == 0:
                self.point_required_point_list.append(
                    [i[0], (1 / 2 + i[1] * self.otnosh) * self.width_line + self.nachalo_x,
                     (1 / 2 + i[2] * self.otnosh) * self.width_line + self.nachalo_y])
                self.point_required_chek.append([self.point_required_point_list[-1][1:3]])
            elif i[0] == 1:
                self.point_required_point_list.append(
                    [i[0], i[1], (1 / 2 + i[2] * self.otnosh) * self.width_line + self.nachalo_x,
                     (1 / 2 + i[3] * self.otnosh) * self.width_line + self.nachalo_y])
                if i[1] == 2:
                    self.point_required_chek.append([self.point_required_point_list[-1][2:4], [self.point_required_point_list[-1][2]+self.otnosh*self.width_line, self.point_required_point_list[-1][3]]])
                else:
                    self.point_required_chek.append([self.point_required_point_list[-1][2:4], [self.point_required_point_list[-1][2], self.point_required_point_list[-1][3] +self.otnosh*self.width_line]])
        self.square_list = square_list
        # self.square_list = []
        self.square_point_list = []
        for i in self.square_list:
            self.square_point_list.append([i[0], (1 / 2 + i[1] * self.otnosh) * self.width_line + self.nachalo_x,
                     (1 / 2 + i[2] * self.otnosh) * self.width_line + self.nachalo_y])
        self.star_list = star_list
        self.star_point_list = []
        for i in self.star_list:
            self.star_point_list.append([i[0], (1 / 2 + i[1] * self.otnosh) * self.width_line + self.nachalo_x,
                                           (1 / 2 + i[2] * self.otnosh) * self.width_line + self.nachalo_y])

        self.rect = 0
        self.circle1 = 0
        self.circle2 = 0
        self.flag_decline = 0

        self.list_circle = []
        self.list_rect = []

        self.end_point_draw = [[], []]
        for end_point in self.end_point_list:
            if end_point[0] == 1:
                self.end_point_draw[0].append([end_point[1] - self.width_line / 2, end_point[2] - self.width_line, self.width_line,
                                          3 / 2 * self.width_line])
                self.end_point_draw[1].append([[end_point[1], end_point[2] - self.width_line], self.width_line / 2])
            elif end_point[0] == 2:
                self.end_point_draw[0].append(
                    [end_point[1] - self.width_line / 2, end_point[2] - self.width_line / 2, 3 / 2 * self.width_line,
                     self.width_line])
                self.end_point_draw[1].append([[end_point[1] + self.width_line, end_point[2]], self.width_line / 2])
            elif end_point[0] == 3:
                self.end_point_draw[0].append([end_point[1] - self.width_line / 2, end_point[2] - self.width_line / 2, self.width_line,
                                          3 / 2 * self.width_line])
                self.end_point_draw[1].append([[end_point[1], end_point[2] + self.width_line], self.width_line / 2])
            elif end_point[0] == 4:
                self.end_point_draw[0].append([end_point[1] - self.width_line, end_point[2] - self.width_line / 2, 3 / 2 * self.width_line,
                                          self.width_line])
                self.end_point_draw[1].append([[end_point[1] - self.width_line, end_point[2]], self.width_line / 2])

        self.crack_point_draw = []
        for crack_point in self.crack_point_list:
            if crack_point[0] == 3:
                self.crack_point_draw.append(
                    [crack_point[1] - self.width_line / 2, crack_point[2] + self.otnosh * self.width_line / 2 - self.width_line / 4,
                     self.width_line, self.width_line / 2])
            if crack_point[0] == 2:
                self.crack_point_draw.append(
                    [crack_point[1] + self.otnosh * self.width_line / 2 - self.width_line / 4, crack_point[2] - self.width_line / 2,
                     self.width_line / 2, self.width_line])

        self.point_required_draw = []
        for point_required in self.point_required_point_list:
            if point_required[0] == 1:
                if point_required[1] == 3:
                    self.point_required_draw.append(
                        [point_required[2],
                         point_required[3] + self.otnosh * self.width_line / 2])
                if point_required[1] == 2:
                    self.point_required_draw.append(
                        [point_required[2] + self.otnosh * self.width_line / 2,
                         point_required[3]])
            else:
                self.point_required_draw.append(
                    [point_required[1], point_required[2]])

        self.square_draw = []
        for i in self.square_point_list:
            if i[0] == 0:
                self.square_draw.append([self.BLACK, i[1] +1/2*self.otnosh*self.width_line - self.width_line//2, i[2] +1/2*self.otnosh*self.width_line - self.width_line//2,
                                         self.width_line, self.width_line])
            elif i[0] == 1:
                self.square_draw.append([self.WHITE, i[1] +1/2*self.otnosh*self.width_line - self.width_line//2, i[2] +1/2*self.otnosh*self.width_line - self.width_line//2,
                                         self.width_line, self.width_line])
        self.star_draw = []
        for i in self.star_point_list:
            if i[0] == 0:
                self.star_draw.append(
                    [self.ORANGE, i[1] + 1 / 2 * self.otnosh * self.width_line,
                     i[2] + 1 / 2 * self.otnosh * self.width_line])
            elif i[0] == 1:
                self.star_draw.append(
                    [self.VIOLET, i[1] + 1 / 2 * self.otnosh * self.width_line,
                     i[2] + 1 / 2 * self.otnosh * self.width_line])
            elif i[0] == 2:
                self.star_draw.append(
                    [self.GREEN, i[1] + 1 / 2 * self.otnosh * self.width_line,
                     i[2] + 1 / 2 * self.otnosh * self.width_line])

    def update_event(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start == 0:
                for self.start_point in self.start_point_list:
                    if ((mouse_pos[0] - self.start_point[0]) ** 2 + (mouse_pos[1] - self.start_point[1]) ** 2) ** (
                            1 / 2) <= self.start_radius and self.start == 0:
                        self.start = 1
                        self.knot = [self.start_point[0], self.start_point[1]]
                        self.pos_0_x = mouse_pos[0]
                        self.pos_0_y = mouse_pos[1]
                        self.knot_flag = 1
                        self.direction_flag = -1
                        self.list_rect = []
                        self.rect = 0
                        self.list_circle = []
                        self.direction_list = []
                        self.knot_list = [[self.knot[0], self.knot[1]]]
                        self.flag_end = 0
                        self.flag_chek = 0
                        self.base_color = self.PATH
                        self.next_color = self.PATH_MAX
                        self.current_color = self.base_color
                        self.flag_decline = 0
                        self.step = 0
                        self.circle1 = 0
                        self.circle2 = 0
                        self.panel_start_tracing.play()


            else:
                self.chek_point_required()
                self.chek_square_star()
                self.start = 0
                self.knot_flag = 0
                self.flag_decline = 1
                self.panel_path_complete.stop()
                if self.flag_end == 1 and self.flag_chek == 0:
                    global level
                    if level == level_len - 1:
                        with open("Первые шаги/Level.txt", mode="w") as f:
                            f.seek(0)
                            level = 0
                            f.write(str(level))
                    else:
                        with open("Первые шаги/Level.txt", mode="w") as f:
                            f.seek(0)
                            level += 1
                            f.write(str(level))
                    self.panel_success2.play()
                    pygame.draw.rect(screen, self.BLACK, [0, 0, pygame.display.Info().current_w, pygame.display.Info().current_h])
                elif self.flag_end == 0:
                    self.panel_abort_tracing.play()
                elif self.flag_end == 1 and self.flag_chek == 1:
                    self.panel_failure.play()
                    self.flag_end = 0


    def update(self, mouse_pos):
        pygame.draw.rect(screen, self.BASE,
                         [self.nachalo_x - 2*self.width_line, self.nachalo_y -2*self.width_line, self.hor_boarder + 4*self.width_line, self.vert_boarder+ 4*self.width_line],
                         border_radius=self.width_line // 2)
        pygame.draw.rect(screen, self.SECOND_BASE, [self.nachalo_x, self.nachalo_y, self.hor_boarder, self.vert_boarder], border_radius=self.width_line // 2)
        for i in range(self.x):
            for j in range(self.y):
                pygame.draw.rect(screen, self.BASE,
                                 [(1 + i * self.otnosh) * self.width_line + self.nachalo_x, (1 + j * self.otnosh) * self.width_line + self.nachalo_y,
                                  self.width_line * (self.otnosh - 1), self.width_line * (self.otnosh - 1)])
        for start_point in self.start_point_list:
            pygame.draw.circle(screen, self.SECOND_BASE, [start_point[0], start_point[1]], self.start_radius)
        for end_point in self.end_point_draw[0]:
            pygame.draw.rect(screen, self.SECOND_BASE, end_point)
        for end_point in self.end_point_draw[1]:
            pygame.draw.circle(screen, self.SECOND_BASE, *end_point)
        for crack_point in self.crack_point_draw:
            pygame.draw.rect(screen, self.BASE, crack_point)
        for point_required in self.point_required_draw:
            pygame.draw.circle(screen, self.BLACK, point_required, self.width_line//4)
        for i in self.square_draw:
            pygame.draw.rect(screen, i[0], i[1:5], border_radius=self.width_line // 8)
        for i in self.star_draw:
            pygame.draw.circle(screen, i[0], i[1:3], self.width_line//2)

        if self.start == 1:
            pygame.draw.circle(screen, self.current_color, self.knot_list[0], self.width_line)
            if self.knot_flag == 1 and (
                    abs(mouse_pos[0] - self.pos_0_x) >= self.width_line / 2 or abs(mouse_pos[1] - self.pos_0_y) >= self.width_line / 2):
                if abs(mouse_pos[0] - self.pos_0_x) <= abs(mouse_pos[1] - self.pos_0_y):
                    if mouse_pos[1] - self.pos_0_y < 0 and (
                            self.knot[1] + (mouse_pos[1] - self.pos_0_y) > self.tablet_board[1][0] or [1, *self.knot] in self.end_point_list):
                        if len(self.direction_list) != 0 and self.direction_list[-1] == 3:
                            del self.knot_list[-1]
                            del self.list_rect[-1]
                            del self.list_circle[-1]
                            del self.direction_list[-1]
                            self.knot = [self.knot_list[-1][0], self.knot_list[-1][1]]
                            self.pos_0_y = self.pos_0_y - self.otnosh * self.width_line
                            self.direction_flag = 3
                            self.circle2 = 0

                        else:
                            self.direction_flag = 1
                            self.circle2 = 0

                    elif mouse_pos[1] - self.pos_0_y > 0 and (
                            self.knot[1] + (mouse_pos[1] - self.pos_0_y) < self.tablet_board[1][1] or [3, *self.knot] in self.end_point_list):
                        if len(self.direction_list) != 0 and self.direction_list[-1] == 1:
                            del self.knot_list[-1]
                            del self.list_rect[-1]
                            del self.list_circle[-1]
                            del self.direction_list[-1]
                            self.knot = [self.knot_list[-1][0], self.knot_list[-1][1]]
                            self.pos_0_y = self.pos_0_y + self.otnosh * self.width_line
                            self.direction_flag = 1
                            self.circle2 = 0

                        else:
                            self.direction_flag = 3
                            self.circle2 = 0

                    else:
                        self.pos_0_x, self.pos_0_y = mouse_pos[0], mouse_pos[1]
                else:
                    if mouse_pos[0] - self.pos_0_x > 0 and (
                            self.knot[0] + (mouse_pos[0] - self.pos_0_x) < self.tablet_board[0][1] or [2, *self.knot] in self.end_point_list):
                        if len(self.direction_list) != 0 and self.direction_list[-1] == 4:
                            del self.knot_list[-1]
                            del self.list_rect[-1]
                            del self.list_circle[-1]
                            del self.direction_list[-1]
                            self.knot = [self.knot_list[-1][0], self.knot_list[-1][1]]
                            self.pos_0_x = self.pos_0_x + self.otnosh * self.width_line
                            self.direction_flag = 4
                            self.circle2 = 0

                        else:
                            self.direction_flag = 2
                            self.circle2 = 0

                    elif mouse_pos[0] - self.pos_0_x < 0 and (
                            self.knot[0] + (mouse_pos[0] - self.pos_0_x) > self.tablet_board[0][0] or [4, *self.knot] in self.end_point_list):
                        if len(self.direction_list) != 0 and self.direction_list[-1] == 2:
                            del self.knot_list[-1]
                            del self.list_rect[-1]
                            del self.list_circle[-1]
                            del self.direction_list[-1]
                            self.knot = [self.knot_list[-1][0], self.knot_list[-1][1]]
                            self.pos_0_x = self.pos_0_x - self.otnosh * self.width_line
                            self.direction_flag = 2
                            self.circle2 = 0

                        else:
                            self.direction_flag = 4
                            self.circle2 = 0

                    else:
                        self.pos_0_x, self.pos_0_y = mouse_pos[0], mouse_pos[1]
                self.knot_flag = 0
            elif self.knot_flag == 1:
                if abs(mouse_pos[0] - self.pos_0_x) <= abs(mouse_pos[1] - self.pos_0_y) and \
                        ((self.knot[1] + (mouse_pos[1] - self.pos_0_y) > self.tablet_board[1][0] + self.width_line / 2 or [1,
                                                                                                       *self.knot] in self.end_point_list) and \
                         (self.knot[1] + (mouse_pos[1] - self.pos_0_y) < self.tablet_board[1][1] - self.width_line / 2) or [3,
                                                                                                        *self.knot] in self.end_point_list):

                    self.circle1 = [self.knot[0], self.knot[1] - (self.pos_0_y - mouse_pos[1])], self.width_line / 2
                    self.circle2 = [self.knot[0], self.knot[1] - (self.pos_0_y - mouse_pos[1]) / 2], self.width_line / 2

                elif abs(mouse_pos[0] - self.pos_0_x) >= abs(mouse_pos[1] - self.pos_0_y) and \
                        (self.knot[0] + (mouse_pos[0] - self.pos_0_x) < self.tablet_board[0][1] - self.width_line / 2 or [2,
                                                                                                      *self.knot] in self.end_point_list) and \
                        (self.knot[0] + (mouse_pos[0] - self.pos_0_x) > self.tablet_board[0][0] + self.width_line / 2 or [4,
                                                                                                      *self.knot] in self.end_point_list):

                    self.circle1 = [self.knot[0] + mouse_pos[0] - self.pos_0_x, self.knot[1]], self.width_line / 2
                    self.circle2 = [self.knot[0] + (mouse_pos[0] - self.pos_0_x) / 2, self.knot[1]], self.width_line / 2

            if self.knot_flag == 0:
                if self.direction_flag == 1:
                    if [self.knot[0], self.knot[1] - self.otnosh * self.width_line] in self.knot_list and self.pos_0_y - mouse_pos[1] > (
                            self.otnosh - 3 / 2) * self.width_line:
                        self.pos_0_y = mouse_pos[1] + (self.otnosh - 3 / 2) * self.width_line

                    if [3, self.knot[0], self.knot[1] - self.otnosh * self.width_line] in self.crack_point_list and self.pos_0_y - mouse_pos[
                        1] + self.width_line / 2 > (self.otnosh * self.width_line / 2 - self.width_line / 4):
                        self.pos_0_y = mouse_pos[1] + self.otnosh * self.width_line / 2 - self.width_line / 4 - self.width_line / 2

                    if [1, *self.knot] in self.end_point_list and self.pos_0_y - mouse_pos[1] >= 1 * self.width_line:
                        self.pos_0_y = mouse_pos[1] + 1 * self.width_line
                        self.flag_end = 1
                    else:
                        self.flag_end = 0

                    self.rect = [self.knot[0] - self.width_line / 2, self.knot[1] - (self.pos_0_y - mouse_pos[1]), self.width_line,
                            self.pos_0_y - mouse_pos[1]]
                    self.circle1 = [self.knot[0], self.knot[1] - (self.pos_0_y - mouse_pos[1])], self.width_line / 2

                    if self.pos_0_y - mouse_pos[1] > (self.otnosh) * self.width_line:
                        self.list_rect.append(
                            [self.knot[0] - self.width_line / 2, self.knot[1] - self.otnosh * self.width_line, self.width_line, self.otnosh * self.width_line])
                        self.list_circle.append([self.knot[0], self.knot[1] - self.otnosh * self.width_line])
                        self.direction_list.append(self.direction_flag)
                        self.knot_flag = 1
                        self.knot[1] -= self.otnosh * self.width_line
                        self.pos_0_y = mouse_pos[1]
                        self.pos_0_x = mouse_pos[0]
                        self.knot_list.append([self.knot[0], self.knot[1]])
                        self.rect = 0

                    elif self.pos_0_y - mouse_pos[1] < self.width_line / 2:
                        self.knot_flag = 1
                        self.pos_0_x = mouse_pos[0]
                        self.rect = 0

                elif self.direction_flag == 2:
                    if [self.knot[0] + self.otnosh * self.width_line, self.knot[1]] in self.knot_list and -self.pos_0_x + mouse_pos[0] > (
                            self.otnosh - 3 / 2) * self.width_line:
                        self.pos_0_x = mouse_pos[0] - (self.otnosh - 3 / 2) * self.width_line

                    if [2, *self.knot] in self.crack_point_list and -self.pos_0_x + mouse_pos[0] + self.width_line / 2 > (
                            self.otnosh * self.width_line / 2 - self.width_line / 4):
                        self.pos_0_x = mouse_pos[0] - self.otnosh * self.width_line / 2 + self.width_line / 4 + self.width_line / 2

                    if [2, *self.knot] in self.end_point_list and -self.pos_0_x + mouse_pos[0] >= 1 * self.width_line:
                        self.pos_0_x = mouse_pos[0] - 1 * self.width_line
                        self.flag_end = 1
                    else:
                        self.flag_end = 0

                    self.rect = [self.knot[0], self.knot[1] - self.width_line / 2, mouse_pos[0] - self.pos_0_x, self.width_line]
                    self.circle1 = [self.knot[0] + mouse_pos[0] - self.pos_0_x, self.knot[1]], self.width_line / 2

                    if - self.pos_0_x + mouse_pos[0] > (self.otnosh) * self.width_line:
                        self.list_rect.append([self.knot[0], self.knot[1] - self.width_line / 2, self.otnosh * self.width_line, self.width_line])
                        self.list_circle.append([self.knot[0] + self.otnosh * self.width_line, self.knot[1]])
                        self.direction_list.append(self.direction_flag)
                        self.knot_flag = 1
                        self.knot[0] += self.otnosh * self.width_line
                        self.pos_0_y = mouse_pos[1]
                        self.pos_0_x = mouse_pos[0]
                        self.knot_list.append([self.knot[0], self.knot[1]])
                        self.rect = 0

                    elif - self.pos_0_x + mouse_pos[0] < self.width_line / 2:
                        self.knot_flag = 1
                        self.pos_0_y = mouse_pos[1]
                        self.rect = 0

                elif self.direction_flag == 3:
                    if [self.knot[0], self.knot[1] + self.otnosh * self.width_line] in self.knot_list and -self.pos_0_y + mouse_pos[1] > (
                            self.otnosh - 3 / 2) * self.width_line:
                        self.pos_0_y = mouse_pos[1] - (self.otnosh - 3 / 2) * self.width_line

                    if [3, *self.knot] in self.crack_point_list and -self.pos_0_y + mouse_pos[1] + self.width_line / 2 > (
                            self.otnosh * self.width_line / 2 - self.width_line / 4):
                        self.pos_0_y = mouse_pos[1] - self.otnosh * self.width_line / 2 + self.width_line / 4 + self.width_line / 2

                    if [3, *self.knot] in self.end_point_list and -self.pos_0_y + mouse_pos[1] >= 1 * self.width_line:
                        self.pos_0_y = mouse_pos[1] - 1 * self.width_line
                        self.flag_end = 1
                    else:
                        self.flag_end = 0

                    self.rect = [self.knot[0] - self.width_line / 2, self.knot[1], self.width_line, mouse_pos[1] - self.pos_0_y]
                    self.circle1 = [self.knot[0], self.knot[1] + (-self.pos_0_y + mouse_pos[1])], self.width_line / 2

                    if - self.pos_0_y + mouse_pos[1] > (self.otnosh) * self.width_line:
                        self.list_rect.append([self.knot[0] - self.width_line / 2, self.knot[1], self.width_line, self.otnosh * self.width_line])
                        self.list_circle.append([self.knot[0], self.knot[1] + self.otnosh * self.width_line])
                        self.direction_list.append(self.direction_flag)
                        self.knot_flag = 1
                        self.knot[1] += self.otnosh * self.width_line
                        self.pos_0_y = mouse_pos[1]
                        self.pos_0_x = mouse_pos[0]
                        self.knot_list.append([self.knot[0], self.knot[1]])
                        self.rect = 0

                    elif - self.pos_0_y + mouse_pos[1] < self.width_line / 2:
                        self.knot_flag = 1
                        self.pos_0_x = mouse_pos[0]
                        self.rect = 0

                elif self.direction_flag == 4:
                    if [self.knot[0] - self.otnosh * self.width_line, self.knot[1]] in self.knot_list and self.pos_0_x - mouse_pos[0] > (
                            self.otnosh - 3 / 2) * self.width_line:
                        self.pos_0_x = mouse_pos[0] + (self.otnosh - 3 / 2) * self.width_line

                    if [2, self.knot[0] - self.otnosh * self.width_line, self.knot[1]] in self.crack_point_list and self.pos_0_x - mouse_pos[
                        0] + self.width_line / 2 > (self.otnosh * self.width_line / 2 - self.width_line / 4):
                        self.pos_0_x = mouse_pos[0] + self.otnosh * self.width_line / 2 - self.width_line / 4 - self.width_line / 2

                    if [4, *self.knot] in self.end_point_list and self.pos_0_x - mouse_pos[0] >= 1 * self.width_line:
                        self.pos_0_x = mouse_pos[0] + 1 * self.width_line
                        self.flag_end = 1
                    else:
                        self.flag_end = 0

                    self.rect = [self.knot[0] - (self.pos_0_x - mouse_pos[0]), self.knot[1] - self.width_line / 2, self.pos_0_x - mouse_pos[0],
                            self.width_line]
                    self.circle1 = [self.knot[0] - (-mouse_pos[0] + self.pos_0_x), self.knot[1]], self.width_line / 2

                    if self.pos_0_x - mouse_pos[0] > (self.otnosh) * self.width_line:
                        self.list_rect.append(
                            [self.knot[0] - self.otnosh * self.width_line, self.knot[1] - self.width_line / 2, self.otnosh * self.width_line, self.width_line])
                        self.list_circle.append([self.knot[0] - self.otnosh * self.width_line, self.knot[1]])
                        self.direction_list.append(self.direction_flag)
                        self.knot_flag = 1
                        self.knot[0] -= self.otnosh * self.width_line
                        self.pos_0_y = mouse_pos[1]
                        self.pos_0_x = mouse_pos[0]
                        self.knot_list.append([self.knot[0], self.knot[1]])
                        self.rect = 0

                    elif self.pos_0_x - mouse_pos[0] < self.width_line / 2:
                        self.knot_flag = 1
                        self.pos_0_y = mouse_pos[1]
                        self.rect = 0

        if self.flag_end_sound == 1 and self.flag_end == 0:
            self.flag_end_sound = 0
            self.panel_abort_finish_tracing.play()
            self.panel_path_complete.stop()

        if self.flag_end_sound == 0 and self.flag_end == 1:
            self.flag_end_sound = 1
            self.panel_finish_tracing.play()
            self.panel_path_complete.play(-1)

        if self.flag_end == 1 and self.start == 1:
            self.flag_end_sound = 1

            self.step += 1
            if self.step <= self.number_of_steps:
                self.current_color = [x + (((y - x) / self.number_of_steps) * self.step) for x, y in
                                 zip(pygame.color.Color(self.base_color), pygame.color.Color(self.next_color))]
            else:
                self.step = 1
                self.base_color, self.next_color = self.next_color, self.base_color
        elif self.start == 1:
            self.base_color = self.PATH
            self.next_color = self.PATH_MAX
            self.current_color = self.base_color
            self.tracing_step += 1
            if self.tracing_timer <= self.tracing_step:
                self.tracing_circle = 1
                self.tracing_step = 0
                self.panel_finish_tracing.play(1)
            for end_tracing in self.end_point_draw[1]:
                if self.tracing_circle == 1 and self.tracing_step < 200:
                    pygame.draw.circle(screen, self.WHITE, end_tracing[0], self.tracing_step // 10, width=1)
                if self.tracing_circle == 1 and 40 < self.tracing_step < 240:
                    pygame.draw.circle(screen, self.WHITE, end_tracing[0], (self.tracing_step - 40) // 10, width=1)
        elif self.flag_decline == 1 and self.flag_end == 1:
            self.step += 1
            if self.step <= self.number_of_steps:
                self.current_color = [x + (((y - x) / self.number_of_steps) * self.step) for x, y in
                                 zip(pygame.color.Color(self.base_color), pygame.color.Color(self.next_color))]
            else:
                self.step = 1
                self.base_color, self.next_color = self.next_color, self.base_color
                if self.base_color == self.PATH_MAX:
                    self.flag_decline = 0

        if self.flag_end == 0 and self.start == 0 and self.flag_decline == 1:
            self.step += 1
            if self.step <= self.number_of_steps1:
                self.current_color = [x + (((y - x) / self.number_of_steps1) * self.step) for x, y in
                                 zip(pygame.color.Color(self.base_color), pygame.color.Color(self.SECOND_BASE))]
            else:
                self.flag_decline = 0
                self.list_rect = []
                self.list_circle = []


        for i in self.list_rect:
            pygame.draw.rect(screen, self.current_color, i)
        for i in self.list_circle:
            pygame.draw.circle(screen, self.current_color, i, self.width_line / 2)
        if self.rect != 0:
            pygame.draw.rect(screen, self.current_color, self.rect)
        if self.circle2 != 0:
            pygame.draw.circle(screen, self.current_color, *self.circle2)
        if self.circle1 != 0:
            pygame.draw.circle(screen, self.current_color, *self.circle1)
        if len(self.knot_list) != 0:
            pygame.draw.circle(screen, self.current_color, self.knot_list[0], self.width_line)

        if self.flag_end == 0 and self.start == 0:
            self.tracing_step += 1
            if self.tracing_timer <= self.tracing_step:
                self.tracing_circle = 1
                self.tracing_step = 0
                self.panel_finish_tracing.play(2)
            for start_tracing in self.start_point_list:
                if self.tracing_circle == 1 and self.tracing_step < 200:
                    pygame.draw.circle(screen, self.WHITE, start_tracing, self.tracing_step // 5, width=1)
                if self.tracing_circle == 1 and 40 < self.tracing_step < 240:
                    pygame.draw.circle(screen, self.WHITE, start_tracing, (self.tracing_step - 40) // 5, width=1)
                if self.tracing_circle == 1 and 80 < self.tracing_step < 280:
                    pygame.draw.circle(screen, self.WHITE, start_tracing, (self.tracing_step - 80) // 5, width=1)

    def chek_point_required(self):
        for chek_point in self.point_required_chek:
            if len(chek_point) == 1:
                if chek_point[0] not in self.knot_list:
                    self.flag_chek = 1
            else:
                if chek_point not in ([self.knot_list[i], self.knot_list[i+1]] for i in range(len(self.knot_list)-1)) and  chek_point not in ([self.knot_list[-i], self.knot_list[-i-1]] for i in range(len(self.knot_list)-1)):
                    self.flag_chek = 1

    def chek_square_star(self):
        mass_chek_b = [[[(1/2+i*self.otnosh)*self.width_line + self.nachalo_x, (1/2+j*self.otnosh)*self.width_line+self.nachalo_y] for j in range(self.x+1)] for i in range(self.y+1)]
        mass_chek_chek_b = [[0 for j in range(self.x+1)] for i in
                       range(self.y+1)]
        mass_chek_af = []
        for i in range(len(mass_chek_b)-1):
            for j in range(len(mass_chek_b)-1):
                if mass_chek_chek_b[i][j] == 0:
                    mass_chek_af.append([mass_chek_b[i][j]])
                    mass_chek_chek_b[i][j] = 1
                    Tablet.chek_rec(i, j, mass_chek_af, mass_chek_b, mass_chek_chek_b, self.knot_list, self.x, self.y)
        for i in mass_chek_af:
            chek_star_temp = dict()
            for k in self.star_point_list:
                chek_star_temp[k[0]] = 0
            chek_temp = -1
            chek_flag = 0
            for j in i:
                for k in self.square_point_list:
                    if j == [k[2], k[1]] and (chek_temp != -1 and chek_temp != k[0]):
                        chek_flag = 1
                        break
                    elif j == [k[2], k[1]]:
                        chek_temp = k[0]
                for k in self.star_point_list:
                    if j == [k[2], k[1]]:
                        chek_star_temp[k[0]] += 1
                if chek_flag == 1:
                    break
            for key in chek_star_temp:
                if chek_star_temp[key] != 0 and chek_star_temp[key] != 2:
                    chek_flag = 1
                    break
            if chek_flag == 1:
                self.flag_chek = 1
                break



    def chek_rec(i, j, mass_chek_af, mass_chek_b, mass_chek_chek_b, knot_list, x, y):
        if j + 1 < x and i+1 <= y and mass_chek_chek_b[i][j + 1] == 0 and (
                [mass_chek_b[i + 1][j + 1], mass_chek_b[i][j + 1]] not in ([knot_list[k][::-1], knot_list[k + 1][::-1]]
                                                                           for k in
                                                                           range(len(knot_list) - 1)) and [
                    mass_chek_b[i + 1][j + 1], mass_chek_b[i][j + 1]] not in (
                [knot_list[-k-1][::-1], knot_list[-k - 2][::-1]] for k in range(len(knot_list) - 1))):
            mass_chek_af[-1].append(mass_chek_b[i][j+1])
            mass_chek_chek_b[i][j+1] = 1
            Tablet.chek_rec(i, j+1, mass_chek_af, mass_chek_b, mass_chek_chek_b, knot_list, x, y)
        if i+1<y and j+1 <=x and mass_chek_chek_b[i+1][j] == 0 and (
                [mass_chek_b[i + 1][j + 1], mass_chek_b[i+1][j]] not in ([knot_list[k][::-1], knot_list[k + 1][::-1]]
                                                                           for k in
                                                                           range(len(knot_list) - 1)) and [
                    mass_chek_b[i + 1][j + 1], mass_chek_b[i+1][j]] not in (
                [knot_list[-k-1][::-1], knot_list[-k - 2][::-1]] for k in range(len(knot_list) - 1))):
            mass_chek_af[-1].append(mass_chek_b[i+1][j])
            mass_chek_chek_b[i+1][j] = 1
            Tablet.chek_rec(i+1, j, mass_chek_af, mass_chek_b, mass_chek_chek_b, knot_list, x, y)


        if j > 0 and mass_chek_chek_b[i][j - 1] == 0 and (
                [mass_chek_b[i + 1][j], mass_chek_b[i][j]] not in ([knot_list[k][::-1], knot_list[k + 1][::-1]]
                                                                           for k in
                                                                           range(len(knot_list) - 1)) and [
                    mass_chek_b[i + 1][j], mass_chek_b[i][j]] not in (
                [knot_list[-k-1][::-1], knot_list[-k - 2][::-1]] for k in range(len(knot_list) - 1))):
            mass_chek_af[-1].append(mass_chek_b[i][j-1])
            mass_chek_chek_b[i][j-1] = 1
            Tablet.chek_rec(i, j-1, mass_chek_af, mass_chek_b, mass_chek_chek_b, knot_list, x, y)
        if i>0 and mass_chek_chek_b[i-1][j] == 0 and (
                [mass_chek_b[i][j + 1], mass_chek_b[i][j]] not in ([knot_list[k][::-1], knot_list[k + 1][::-1]]
                                                                           for k in
                                                                           range(len(knot_list) - 1)) and [
                    mass_chek_b[i][j + 1], mass_chek_b[i][j]] not in (
                [knot_list[-k-1][::-1], knot_list[-k - 2][::-1]] for k in range(len(knot_list) - 1))):
            mass_chek_af[-1].append(mass_chek_b[i-1][j])
            mass_chek_chek_b[i-1][j] = 1
            Tablet.chek_rec(i-1, j, mass_chek_af, mass_chek_b, mass_chek_chek_b, knot_list, x, y)



FPS = 200
running = True
WIDTH = 800
HEIGHT = 700

BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
A = []
A.append(Tablet(FPS, BASE = (251,183,1), PATH = (254,253,184), SECOND_BASE= (75,63,7), PATH_MAX = (254,248,242), x = 3, y = 0, start_list = [[0, 0]], end_list = [[2, 3, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (251,183,1), PATH = (254,253,184), SECOND_BASE= (75,63,7), PATH_MAX = (254,248,242), x = 6, y = 6, start_list = [[0, 6], [6 ,6]], end_list = [[1, 3, 0]],
               crack_list = [[2, 0, 0], [2, 2, 0], [2, 3, 0], [2, 0, 1], [2, 3, 1], [2, 0, 2], [2, 2, 2], [2, 4, 2],
                [2, 1, 3], [2, 3, 3], [2, 3, 4], [2, 4, 4], [2, 1, 5], [2, 4, 5], [2, 2, 6], [2, 4, 6], [3, 1, 2],
                [3, 1, 4], [3, 2, 1], [3, 2, 3], [3, 3, 1], [3, 3, 3], [3, 4, 0], [3, 4, 2], [3, 4, 4], [3, 5, 0],
                [3, 5, 2], [3, 5, 4], [3, 6, 1], [3, 6, 3]], point_required_list = [], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (251,183,1), PATH = (254,253,184), SECOND_BASE= (75,63,7), PATH_MAX = (254,248,242), x = 6, y = 6, start_list = [[0, 6]], end_list = [[2, 6, 6]],
               crack_list = [[2, 3, 0], [2, 1, 1], [2, 2, 1], [2, 4, 1], [2, 2, 2], [2, 4, 2], [2, 1, 3], [2, 3, 3],
                [2, 3, 4], [2, 4, 4], [2, 1, 5], [2, 4, 5], [2, 2, 6], [2, 4, 6], [3, 0, 2], [3, 1, 4], [3, 2, 1],
                 [3, 2, 3], [3, 3, 0], [3, 3, 3], [3, 4, 2], [3, 4, 4], [3, 5, 0], [3, 5, 2], [3, 5, 4], [3, 6, 1],
                  [3, 6, 3]], point_required_list = [], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (0,200,69), PATH = (246,254,252), SECOND_BASE= (0,85,31), PATH_MAX = (162,246,25), x = 2, y = 2, start_list = [[0, 2]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [[0, 0, 0], [0, 2, 2]], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (0,200,69), PATH = (246,254,252), SECOND_BASE= (0,85,31), PATH_MAX = (162,246,25), x = 3, y = 3, start_list = [[0, 3]], end_list = [[1, 3, 0]],
               crack_list = [[2, 0, 0], [2, 1, 1], [2, 2, 1], [3, 0, 0], [3, 2, 2]], point_required_list = [[0, 1, 0],
                [0, 2, 1], [0, 0, 2], [0, 1, 2], [0, 3, 3]], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (0,200,69), PATH = (246,254,252), SECOND_BASE= (0,85,31), PATH_MAX = (162,246,25), x = 3, y = 3, start_list = [[1, 1], [2, 2]], end_list = [[4, 0, 1]],
               crack_list = [[2, 0, 0], [3, 0, 0], [2, 2, 1], [3, 2, 2]], point_required_list = [[0, 1, 0], [0, 2, 1],
                [0, 3, 1], [0, 0, 2], [0, 1, 2], [0, 3, 3]], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (0,200,69), PATH = (246,254,252), SECOND_BASE= (0,85,31), PATH_MAX = (162,246,25), x = 3, y = 3, start_list = [[2, 0], [3, 0], [3, 2]], end_list = [[4, 0, 1]],
               crack_list = [[2, 0, 0], [3, 0, 0], [2, 2, 1], [3, 2, 2]], point_required_list = [[0, 1, 0], [0, 2, 1],
                [0, 3, 1], [0, 0, 2], [0, 1, 2], [0, 3, 3]], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (0,200,69), PATH = (246,254,252), SECOND_BASE= (0,85,31), PATH_MAX = (162,246,25), x = 4, y = 4, start_list = [[2, 2]], end_list = [[2, 4, 0]],
               crack_list = [[2, 2, 0]], point_required_list = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 0, 1], [0, 1, 1],
                [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 0, 2], [0, 1, 2], [0, 3, 2], [0, 4, 2], [0, 0, 3], [0, 1, 3],
                 [0, 2, 3], [0, 3, 3], [0, 4, 3], [0, 0, 4], [0, 1, 4], [0, 2, 4], [0, 3, 4], [0, 4, 4]], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (0,200,69), PATH = (246,254,252), SECOND_BASE= (0,85,31), PATH_MAX = (162,246,25), x = 4, y = 4, start_list = [[2, 2]], end_list = [[2, 4, 0]],
               crack_list = [[3, 1, 0], [3, 1, 3]], point_required_list = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 0, 1], [0, 1, 1],
                [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 0, 2], [0, 1, 2], [0, 3, 2], [0, 4, 2], [0, 0, 3], [0, 1, 3],
                 [0, 2, 3], [0, 3, 3], [0, 4, 3], [0, 0, 4], [0, 1, 4], [0, 2, 4], [0, 3, 4], [0, 4, 4]], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (0,200,69), PATH = (246,254,252), SECOND_BASE= (0,85,31), PATH_MAX = (162,246,25), x = 5, y = 5, start_list = [[2, 5]], end_list = [[3, 3, 5]],
               crack_list = [[2, 1, 1], [2, 3, 1], [2, 1, 4], [2, 3, 4], [3, 0, 1], [3, 1, 1], [3, 4, 1], [3, 5, 1],
                [3, 0, 3], [3, 1, 3], [3, 4, 3], [3, 5, 3]], point_required_list = [[1, 2, 2, 0], [1, 3, 0, 2],
                 [1, 3, 5, 2]], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (0,200,69), PATH = (246,254,252), SECOND_BASE= (0,85,31), PATH_MAX = (162,246,25), x = 5, y = 5, start_list = [[2, 5]], end_list = [[1, 3, 0]],
               crack_list = [[2, 1, 4], [2, 1, 5], [2, 3, 0], [2, 3, 1], [3, 0, 3], [3, 1, 3], [3, 4, 1], [3, 5, 1]],
                point_required_list = [[0, 0, 3], [0, 1, 3], [0, 2, 3], [0, 2, 4], [0, 2, 5], [0, 4, 5], [0, 5, 2],
                 [1, 2, 1, 0], [1, 3, 0, 1], [1, 3, 3, 1], [1, 3, 5, 3]], square_list = [],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 1, y = 2, start_list = [[0, 1]], end_list = [[2, 1, 1]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 0], [1, 0, 1]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 1, y = 2, start_list = [[0, 2]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 0], [1, 0, 1]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 1, y = 3, start_list = [[0, 3]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 0], [0, 0, 1], [1, 0, 2]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 2, y = 2, start_list = [[0, 2]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 1, 1]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 3, y =3, start_list = [[0, 3]], end_list = [[1, 3, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 0, 1],
                [0, 2, 1], [1, 1, 1],
                [1, 0, 2], [1, 1, 2], [1, 2, 2]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 3, y =3, start_list = [[0, 3]], end_list = [[4, 0, 2]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 0, 1],
                [0, 2, 1], [1, 1, 1],
                [1, 0, 2], [1, 1, 2], [1, 2, 2]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 4, y = 4, start_list = [[0, 4]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 0], [0, 3, 0], [0, 0, 1], [0, 1, 1],
                [0, 2, 1], [0, 3, 1], [0, 0, 2], [0, 2, 2], [0, 3, 2], [0, 3, 3], [1, 2, 0], [1, 1, 2], [1, 0, 3],
                 [1, 1, 3], [1, 2, 3]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 4, y = 4, start_list = [[0, 4]], end_list = [[2, 4, 2]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 0], [0, 3, 0], [0, 1, 0], [0, 1, 1],
                [0, 2, 1], [0, 3, 1], [0, 0, 2], [0, 2, 2], [0, 3, 3], [1, 2, 0], [1, 1, 2], [1, 0, 3],
                 [1, 1, 3], [1, 2, 3]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 4, y = 4, start_list = [[0, 4]], end_list = [[3, 3, 4]],
               crack_list = [], point_required_list = [], square_list = [[0, 3, 0], [0, 1, 0], [0, 0, 1],
                [0, 3, 1], [0, 0, 2], [0, 2, 2], [0, 3, 3], [1, 2, 0], [1, 1, 2], [1, 0, 3],
                 [1, 1, 3], [1, 2, 3]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 4, y = 5, start_list = [[2, 5]], end_list = [[1, 2, 0]],
               crack_list = [[2, 0, 5], [2, 3, 5], [3, 0, 4], [3, 1, 4], [3, 3, 4], [3, 4, 4]], point_required_list = [],
                square_list = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 0, 1], [0, 0, 1], [0, 3, 1], [0, 0, 2],
                 [0, 3, 2], [0, 0, 3], [0, 1, 3], [0, 3, 3], [1, 1, 1], [1, 2, 1], [1, 1, 2], [1, 2, 2]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 4, y = 4, start_list = [[0, 4]], end_list = [[2, 4, 0]],
               crack_list = [], point_required_list = [],
                square_list = [[0, 1, 0], [0, 2, 0], [0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 0, 2], [0, 1, 2],
                 [0, 2, 2], [0, 3, 2], [0, 1, 3], [0, 2, 3], [1, 0, 0], [1, 3, 0], [1, 0, 3], [1, 3, 3]],
               star_list = []))
A.append(Tablet(FPS, BASE = (76,74,249), PATH = (246,254,252), SECOND_BASE= (33,11,155), PATH_MAX = (94,145,249), x = 4, y = 4, start_list = [[0, 0], [4, 4]], end_list = [[1, 2, 0], [3, 2, 4]],
               crack_list = [], point_required_list = [],
                square_list = [[0, 1, 0], [0, 2, 0], [0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 0, 2], [0, 1, 2],
                 [0, 2, 2], [0, 3, 2], [0, 1, 3], [0, 2, 3], [1, 0, 0], [1, 3, 0], [1, 0, 3]],
               star_list = []))
A.append(Tablet(FPS, BASE = (197,197,196), PATH = (246,254,252), SECOND_BASE= (117,117,116), PATH_MAX = (193,254,234), x = 7, y = 7, start_list = [[4, 2], [6, 4], [2, 5], [0, 7]], end_list = [[4, 0, 0], [2, 7, 0], [2, 7, 7]],
               crack_list = [], point_required_list = [[1, 2, 6, 0], [1, 2, 6, 4], [1, 2, 1, 5], [1, 2, 0, 7], [1, 2, 5, 7], [1, 3, 7, 0],
                [1, 3, 7, 3], [1, 3, 0, 6]], square_list = [[0, 0, 0], [0, 5, 0], [0, 3, 1], [0, 4, 1], [0, 2, 4], [0, 6, 5],
                 [0, 6, 6], [1, 1, 0], [1, 0, 1], [1, 6, 0], [1, 3, 2], [1, 4, 2], [1, 2, 5], [1, 5, 6]],
               star_list = []))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 1, y = 2, start_list = [[0, 2]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 0, 1]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 3, y = 3, start_list = [[1, 3]], end_list = [[1, 1, 0]],
               crack_list = [[2, 0, 2], [2, 0, 3], [2, 2, 2], [3, 0, 0], [3, 3, 0]], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 2, 2]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [[2, 2, 0], [2, 1, 1], [2, 3, 1], [2, 1, 3], [2, 1, 4], [3, 0, 0], [3, 3, 0], [3, 4, 2]], point_required_list = [], square_list = [],
               star_list = [[0, 0, 3], [0, 3, 1]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 2, y = 2, start_list = [[1, 2]], end_list = [[1, 1, 0]],
               crack_list = [[2, 1, 1]], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 2, y = 2, start_list = [[1, 2]], end_list = [[1, 1, 0]],
               crack_list = [[3, 1, 0]], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [[2, 0, 0], [2, 2, 1], [2, 1, 2], [2, 2, 3], [2, 3, 4], [3, 1, 0], [3, 2, 0], [3, 3, 1], [3, 1, 2]], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 3, 0], [0, 0, 3], [0, 3, 3]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [[2, 3, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0], [3, 0, 1], [3, 1, 2], [3, 4, 3]], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 3, 0], [0, 0, 3], [0, 3, 3]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 3, y = 3, start_list = [[2, 3]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 3, y = 3, start_list = [[2, 3]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 1, 0], [0, 0, 2], [0, 2, 0], [0, 1, 2], [0, 2, 2]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 2], [0, 3, 0], [0, 3, 1], [0, 3, 2], [0, 3, 3]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (224,162,11), x = 4, y = 4, start_list = [[0, 4]], end_list = [[1, 4, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0 ,0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 1, 3], [0, 1, 0], [0, 2, 0], [0, 3, 0]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 2, y = 2, start_list = [[1, 2]], end_list = [[1, 1, 0]],
               crack_list = [[2, 1, 1]], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 0, 1], [1, 1 ,0], [1, 1, 1]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 2, y = 2, start_list = [[1, 2]], end_list = [[1, 1, 0]],
               crack_list = [[3, 1, 0]], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 0, 1], [1, 1 ,0], [1, 1, 1]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 2, y = 3, start_list = [[1, 3]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 3, 3], [1, 0, 1], [1, 1, 0], [1, 3, 2], [1, 2, 3]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 3, 3], [0, 0, 3], [0, 3, 0], [1, 0, 1], [1, 1, 0], [1, 3, 2], [1, 2, 3], [1, 1, 1], [1, 2, 2]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 3, 2], [0, 2, 3], [0, 3, 3], [1, 2, 0], [1, 3, 0], [1, 3, 1], [1, 0, 2], [1, 0, 3], [1, 1, 3]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[1, 1, 1], [0, 0, 1], [0, 1, 0], [0, 3, 2], [0, 2, 3], [1, 2, 2], [0, 2, 0], [1, 3, 0], [0, 3, 1], [0, 0, 2], [1, 0, 3], [0, 1, 3]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [[2, 3, 0], [3, 0, 1]], point_required_list = [], square_list = [],
               star_list = [[0, 2, 1], [0, 0, 3], [1, 0, 0], [1, 3, 0], [2, 0, 1], [2, 2, 2]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 4, y = 3, start_list = [[2, 3]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 0, 2], [0, 1, 2], [0, 2, 2], [0, 3, 2], [0, 2, 1], [0, 3, 1], [1, 0, 0],
               [1, 1, 0], [1, 0, 1], [1, 1, 1], [2, 2, 0], [2, 3, 0]]))
A.append(Tablet(FPS, BASE = (85,100,109), PATH = (246,254,252), SECOND_BASE= (31,46,55), PATH_MAX = (238,143,39),x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 1, 0], [0, 0, 1], [0, 0, 2], [0, 1, 3], [1, 2, 0], [1, 3, 1], [1, 3, 2], [1, 2, 3],
                [2, 1, 1], [2, 2, 1], [2, 2, 2], [2, 1, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 3, y = 3, start_list = [[0, 3]], end_list = [[1, 3, 0]],
               crack_list = [[2, 0, 0], [2, 2, 1], [3, 0, 0], [3, 2, 2]], point_required_list = [[0, 1, 0], [0, 2, 1],
                [0, 1, 2], [0, 0, 2], [0, 3, 3]], square_list = [],
               star_list = [[0, 0, 2], [0, 1, 1]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 3, y = 3, start_list = [[0, 3]], end_list = [[1, 3, 0]],
               crack_list = [[2, 0, 0], [2, 2, 1], [3, 0, 0], [3, 2, 2]], point_required_list = [[0, 1, 0], [0, 2, 1],
                [0, 1, 2], [0, 0, 2], [0, 3, 3]], square_list = [],
               star_list = [[0, 1, 1], [0, 2, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [[0, 0, 0], [0, 0, 4], [0, 4, 0], [0, 4, 4]],
                square_list = [],
               star_list = [[0, 2, 0], [0, 0, 3]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 4, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [[0, 0, 0], [0, 0, 4], [0, 4, 0], [0, 4, 4]],
                square_list = [],
               star_list = [[0, 0, 0], [0, 0, 3], [0, 3, 0], [0, 3, 3]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 5, y = 5, start_list = [[3, 5]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [[0, 0, 0], [0, 5, 0], [0, 2, 2], [0, 2, 3], [0, 3, 2], [0, 3, 3],
                [0, 0, 5], [0, 5, 5]], square_list = [],
               star_list = [[0, 0, 0], [0, 4, 0], [0, 4, 4], [0, 2, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 3, y = 3, start_list = [[1, 3]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 1, 1], [1, 0, 1]],
               star_list = [[0, 0, 0], [0, 2, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 3, y = 3, start_list = [[1, 3]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 2 ,0], [0, 2, 2], [1, 0, 0], [1, 0, 2]],
               star_list = [[0, 0, 1], [0, 2, 1]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 3, y = 3, start_list = [[1, 3]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 2 ,0], [0, 2, 2], [1, 0, 0], [1, 0, 2]],
               star_list = [[0, 0, 1], [0, 2, 1], [0, 1, 0], [0, 1, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 3, y = 3, start_list = [[1, 3]], end_list = [[1, 1, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 2 ,0], [1, 2, 2], [1, 0, 0], [0, 0, 2]],
               star_list = [[0, 0, 1], [0, 2, 1], [0, 1, 0], [0, 1, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 3, y = 3, start_list = [[1, 3]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 1, 0], [0, 1, 2], [1, 0, 1], [1, 2, 1]],
               star_list = [[2, 0, 0], [2, 0, 2], [2, 2, 0], [2, 2, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 5, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [], point_required_list = [], square_list = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 2, 0],
                [1, 0, 3], [1, 1, 3], [1, 4, 1], [1, 4, 2]],
               star_list = [[1, 0, 0], [1, 1, 0], [1, 0, 2], [1, 1, 2], [1, 3, 1], [1, 3, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 5, y = 4, start_list = [[2, 4]], end_list = [[1, 2, 0]],
               crack_list = [[3, 4, 2], [2, 1, 3]], point_required_list = [], square_list = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 2, 0],
                [1, 0, 3], [1, 1, 3], [1, 4, 1], [1, 4, 2]],
               star_list = [[1, 0, 0], [1, 1, 0], [1, 0, 2], [1, 1, 2], [1, 3, 1], [1, 3, 2]]))
A.append(Tablet(FPS, BASE = (145,148,145), PATH = (246,254,252), SECOND_BASE= (57,64,60), PATH_MAX = (241,16,246),x = 5, y = 5, start_list = [[5, 5]], end_list = [[4, 0, 0]],
               crack_list = [], point_required_list = [], square_list = [],
               star_list = [[0, 3, 0], [0, 4, 0], [0, 4, 1], [0, 0, 3], [0, 0, 4], [0, 1, 4],
                            [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 2, 0], [1, 2, 4], [1, 3, 4], [1, 4, 4], [1, 4, 3], [1, 4, 2]]))
global level_len
level_len = len(A)
global level
with open("Первые шаги/Level.txt", mode="r") as f:
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
