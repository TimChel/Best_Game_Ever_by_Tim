import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))

buttons = pygame.sprite.Group()
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

class Button(pygame.sprite.Sprite):
    def __init__(self, screen, position, text, size, colors="white on blue", hid = 1):
        super().__init__()
        self.colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        self.font = pygame.font.SysFont("Arial", size-10)
        self.text_render = self.font.render(text, 1, self.fg)
        self.image = self.text_render
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.hid = hid
        self.update()
        buttons.add(self)

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.hid:
            pass
        else:
            pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
            pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
            pygame.draw.line(screen, (70, 70, 70), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
            pygame.draw.line(screen, (70, 70, 70), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
            pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Start_W:
    def __init__(self):
        self.b0 = Button(screen, (900, 350), "Login", 60, "red on yellow", 0)
        self.b1 = Button(screen, (830, 500), "Registration", 60, "red on yellow", 0) 
    
    def update(self):
        self.b0.update()
        self.b1.update()
        buttons.draw(screen)
        pygame.display.update()
    
    def _not_hover(self):
        for x in buttons:
            try:
                if x.hid:
                    pass
                else:
                    x.colors = "red on yellow"
                    x.update()
            except Exception as e:
                print(e)
    
    def not_hover(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
        if event.type == pygame.MOUSEMOTION:
            # 2. put the collide check for mouse hover here for each button
            if self.b0.rect.collidepoint(pygame.mouse.get_pos()):
                self.b0.colors = "red on green"
            elif self.b1.rect.collidepoint(pygame.mouse.get_pos()):
                self.b1.colors = "red on green"
            else:
                # this will work for every buttons going back to original color after mouse goes out
                self._not_hover()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 3. here the interactions with the click of the mouse... done
            if self.b0.rect.collidepoint(pygame.mouse.get_pos()):
                self.b0.hid = 1
                print("login")
                WM.goto("Auth")
                print(9)
            if self.b1.rect.collidepoint(pygame.mouse.get_pos()):
                self.b1.hid = 1
                print("registration")        
                
class Auth_W:
    def __init__(self):
        self.input_box1 = InputBox(100, 100, 140, 32)
        self.input_box2 = InputBox(100, 300, 140, 32)
        self.input_boxes = [self.input_box1, self.input_box2] 
    
    def update(self):
        for box in self.input_boxes:
            box.update()
        for box in self.input_boxes:
             box.draw(screen)
    
    def not_hover(self, event):
        for box in self.input_boxes:
            box.handle_event(event)        


class Window_maneger:
    def __init__(self):
        self.sw = Start_W()
        self.auth = Auth_W()
        self.app = {"Start": self.sw, "Auth": self.auth}
        self.current = "Start"
    
    def update(self):
        self.app[self.current].update()
        
    def not_hover(self, event):
        self.app[self.current].not_hover(event)
        
    def goto(self, page_name):
        self.update()
        print(0)
        pygame.display.update()
        self.current = page_name
        
        

def menu():
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            WM.not_hover(event)
        WM.update()
    pygame.quit()

WM = Window_maneger()
menu()
