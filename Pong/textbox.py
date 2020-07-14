import pygame
#https://www.youtube.com/watch?v=kW-KIQGVMAQ

pygame.init()
pygame.display.set_caption('Text Box')
screen = pygame.display.set_mode((800,600))
vec = pygame.math.Vector2
white = (255, 255, 255)
black = (0, 0, 0)
gray = (176, 176, 176)
blue = (0,0,200)
red = (200,0,0)

class Text_box():
    def __init__(self, x, y, width=5, height=2, bg_color=gray,
                 active_color=blue, border=0, text_size = 20
                 ,text_color = white, border_color=red):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = vec(x,y)
        self.size = vec(width, height)
        self.image = pygame.Surface((width,height))
        self.bg_color = bg_color
        self.active_color = active_color
        self.active = False

        self.text = ""
        self.text_size = text_size
        self.font = pygame.font.SysFont('Arial', self.text_size, bold=True)
        self.text_color = text_color
        self.border = border
        self.border_color = border_color

    def update(self):
        pass

    def draw(self, screen):
        if not self.active:
            self.image.fill(self.bg_color)
            #Rendering text to image
            text = self.font.render(self.text, False, self.text_color)
            #getting size attributes of the text
            text_height = text.get_height()
            self.image.blit(text, (self.border*4,(self.height-text_height)//2))
        else:
            if self.border == 0:
                self.image.fill(self.bg_color)

            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.active_color,
                        (self.border, self.border, self.width-self.border*2,
                         self.height-self.border*2))

            text = self.font.render(self.text, False, self.text_color)
            text_height = text.get_height()
            text_width = text.get_width()
            if text_width < self.width - self.border * 2:
                self.image.blit(text, (self.border*4, (self.height - text_height) // 2))
            else:
                #text moves to the end as we type
                #self.border*4 - how far chars are from border
                self.image.blit(text, ((self.border*4)+
                                       (self.width-text_width-self.border*4),
                                       (self.height - text_height) // 2))
        screen.blit(self.image, self.pos)

    def check_click(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.active = True
            else:
                self.active = False
        else:
            self.active = False

    def add_text(self, key):
        #adding letters & special characters
        #8 -> backspace
        #32 -> space
        if key in range(97, 123) or key in range(48,58) or key == 32:
            text = list(self.text)
            text.append(chr(key))#output letters instead of numbers
            self.text = ''.join(text)#join characters into string
            print(self.text)
        #pop removes squares when hitting backspace
        elif key == 8:
            text = list(self.text)
            text.pop()
            self.text = ''.join(text)
            print(self.text)

        #enter
        elif key == 13:
            text = list(self.text)
            text.append(chr(key))
            self.text = ''.join(text)
            print(self.text)

        else:
            print(key)

    def return_value(self):
        return self.text

text_box = []
text_box.append(Text_box(300,300, 200, 50, gray, border=3))

def main():
    run = True
    while run:
        screen.fill(black)
        #mouse clicks, etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for box in text_box:
                    #return pos of mouse
                    box.check_click(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                for box in text_box:
                    if box.active:
                        box.add_text(event.key)

        screen.fill(black)
        font = pygame.font.SysFont('Arial',30, bold=True)
        input_font = font.render("Please enter your name:", True, white)
        Text_box(300, 300)
        screen.blit(input_font, (800 // 2 - 180, 600 // 2 - 100))

        for box in text_box:
            box.draw(screen)
        pygame.display.update()
main()
pygame.quit()