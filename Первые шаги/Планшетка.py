import pygame

class Tablet():
    def __init__(self, FPS):
        pygame.mixer.init()
        self.panel_path_complete = pygame.mixer.Sound("panel_path_complete-fix.ogg")
        self.panel_path_complete.set_volume(0.1)
        self.panel_start_tracing = pygame.mixer.Sound("panel_start_tracing-fix.ogg")
        self.panel_start_tracing.set_volume(0.1)
        self.panel_success2 = pygame.mixer.Sound("panel_success2-fix.ogg")
        self.panel_success2.set_volume(0.1)
        self.panel_abort_tracing = pygame.mixer.Sound("panel_abort_tracing-fix.ogg")
        self.panel_abort_tracing.set_volume(0.1)
        self.panel_abort_finish_tracing = pygame.mixer.Sound("panel_abort_finish_tracing-fix_1.ogg")
        self.panel_abort_finish_tracing.set_volume(0.1)
        self.panel_finish_tracing = pygame.mixer.Sound("panel_finish_tracing-fix.ogg")
        self.panel_finish_tracing.set_volume(0.1)
        self.panel_failure = pygame.mixer.Sound("panel_failure-fix.ogg")
        self.panel_failure.set_volume(0.1)
        self.tracing_step = 0
        self.tracing_timer = 600
        self.tracing_circle = 0

        self.FPS = FPS
        self.BLACK = (0, 0, 0)
        self.GREY = (128, 128, 128)
        self.GREEN = (0, 255, 0)
        self.WHITE = (255, 255, 255)
        self.WHITE_minor = (180, 180, 180)

        self.base_color = self.GREY
        self.next_color = self.GREEN
        self.current_color = self.base_color
        self.change_every_x_seconds = 1 / 3
        self.number_of_steps = self.change_every_x_seconds * self.FPS
        self.step = 1

        self.change_every_x_seconds1 = 1
        self.number_of_steps1 = self.change_every_x_seconds1 * self.FPS

        self.start = 0
        self.width_line = 20
        self.start_radius = self.width_line
        self.nachalo_x = 100
        self.nachalo_y = 100
        self.x, self.y = 3, 3
        self.otnosh = 4
        self.vert_boarder = (1 + self.y * self.otnosh) * self.width_line
        self.hor_boarder = (1 + self.x * self.otnosh) * self.width_line
        self.flag_chek = 0
        self.flag_end = 0
        self.flag_end_sound = 0
        self.knot_flag = 0
        self.knot_list = []
        self.direction_list = []
        self.tablet_board = [(self.nachalo_x, self.nachalo_x + self.hor_boarder), [self.nachalo_y, self.nachalo_y + self.vert_boarder]]
        self.start_list = [[1, 1], [2, 2]]
        self.start_point_list = []
        for i, j in self.start_list:
            self.start_point_list.append(
                [(1 / 2 + i * self.otnosh) * self.width_line + self.nachalo_x, (1 / 2 + j * self.otnosh) * self.width_line + self.nachalo_y])
        self.end_list = [[3, 0, self.y], [1, self.x, 0], [4, 0, 0]]
        self.end_point_list = []
        for i, j, k in self.end_list:
            self.end_point_list.append(
                [i, (1 / 2 + j * self.otnosh) * self.width_line + self.nachalo_x, (1 / 2 + k * self.otnosh) * self.width_line + self.nachalo_y])
        self.crack_list = [[2, 0, 0], [3, 0, 0], [2, 1, 1], [3, 1, 1]]
        self.crack_point_list = []
        for i, j, k in self.crack_list:
            self.crack_point_list.append(
                [i, (1 / 2 + j * self.otnosh) * self.width_line + self.nachalo_x, (1 / 2 + k * self.otnosh) * self.width_line + self.nachalo_y])
        self.point_required_list = [[0, 2, 2], [1, 2, 2, 2]]
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
                        self.base_color = self.WHITE
                        self.next_color = self.GREEN
                        self.current_color = self.base_color
                        self.flag_decline = 0
                        self.step = 0
                        self.circle1 = 0
                        self.circle2 = 0
                        self.panel_start_tracing.play()


            else:
                self.chek()
                self.start = 0
                self.knot_flag = 0
                self.flag_decline = 1
                self.panel_path_complete.stop()
                if self.flag_end == 1 and self.flag_chek == 0:
                    print("Win")
                    self.panel_success2.play()
                elif self.flag_end == 0:
                    self.panel_abort_tracing.play()
                elif self.flag_end == 1 and self.flag_chek == 1:
                    self.panel_failure.play()
                    self.flag_end = 0


    def update(self, mouse_pos):
        screen.fill(self.BLACK)
        pygame.draw.rect(screen, self.GREY, [self.nachalo_x, self.nachalo_y, self.hor_boarder, self.vert_boarder], border_radius=self.width_line // 2)
        for i in range(self.x):
            for j in range(self.y):
                pygame.draw.rect(screen, self.BLACK,
                                 [(1 + i * self.otnosh) * self.width_line + self.nachalo_x, (1 + j * self.otnosh) * self.width_line + self.nachalo_y,
                                  self.width_line * (self.otnosh - 1), self.width_line * (self.otnosh - 1)])
        for start_point in self.start_point_list:
            pygame.draw.circle(screen, self.GREY, [start_point[0], start_point[1]], self.start_radius)
        for end_point in self.end_point_draw[0]:
            pygame.draw.rect(screen, self.GREY, end_point)
        for end_point in self.end_point_draw[1]:
            pygame.draw.circle(screen, self.GREY, *end_point)
        for crack_point in self.crack_point_draw:
            pygame.draw.rect(screen, self.BLACK, crack_point)
        for point_required in self.point_required_draw:
            pygame.draw.circle(screen, self.BLACK, point_required, self.width_line//4)

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
            if self.step <= self.number_of_steps1:
                self.current_color = [x + (((y - x) / self.number_of_steps1) * self.step) for x, y in
                                 zip(pygame.color.Color(self.base_color), pygame.color.Color(self.next_color))]
            else:
                self.step = 1
                self.base_color, self.next_color = self.next_color, self.base_color
        elif self.start == 1:
            self.base_color = self.WHITE
            self.next_color = self.GREEN
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
            if self.step <= self.number_of_steps1:
                self.current_color = [x + (((y - x) / self.number_of_steps1) * self.step) for x, y in
                                 zip(pygame.color.Color(self.base_color), pygame.color.Color(self.next_color))]
            else:
                self.step = 1
                self.base_color, self.next_color = self.next_color, self.base_color
                if self.base_color == self.WHITE:
                    self.flag_decline = 0

        if self.flag_end == 0 and self.start == 0 and self.flag_decline == 1:
            self.step += 1
            if self.step <= self.number_of_steps1:
                self.current_color = [x + (((y - x) / self.number_of_steps1) * self.step) for x, y in
                                 zip(pygame.color.Color(self.base_color), pygame.color.Color(self.GREY))]
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

    def chek(self):
        for chek_point in self.point_required_chek:
            print(chek_point)
            print(self.knot_list)
            if len(chek_point) == 1:
                if chek_point[0] not in self.knot_list:
                    print('Yes')
                    self.flag_chek = 1
            else:
                if chek_point not in ([self.knot_list[i], self.knot_list[i+1]] for i in range(len(self.knot_list)-1)) and  chek_point not in ([self.knot_list[-i], self.knot_list[-i-1]] for i in range(len(self.knot_list)-1)):
                    print('No')
                    self.flag_chek = 1




FPS = 200
running = True
WIDTH = 600
HEIGHT = 500

BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
A = Tablet(FPS)

while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        A.update_event(event, mouse_pos)
        if event.type == pygame.QUIT:
            running = False
    A.update(mouse_pos)
    pygame.display.flip()

pygame.quit()