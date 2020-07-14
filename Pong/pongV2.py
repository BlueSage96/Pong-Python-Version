import pygame, sys
import pygame.gfxdraw, pygame.font
vec = pygame.math.Vector2
import os
from os import path #builds file location

#importing another file in same project:
#https://www.youtube.com/watch?v=0v9ATbJTQDc

#https://www.mrmichaelsclass.com/python-programming/python-projects/pygame-pong
#https://www.101computing.net/pong-tutorial-using-pygame-controlling-the-paddles/
#https://github.com/EricsonWillians/PyClassicPong/blob/master/run.py
#https://www.daniweb.com/programming/software-development/threads/334979/adding-pause-feature-in-pygame

#got ball to be round:
#https://www.dropbox.com/sh/wjlachxiy8zayf1/AABUx7y0MX9t8Xmi3PL6RoW5a?dl=0&preview=Pygame+pong+with+game+class.py

#sound
#https://www.youtube.com/watch?v=YZknoOWCaj4&feature=youtu.be

#start menu:
#part 1:
#https://www.youtube.com/watch?time_continue=1465&v=zFBQJ9bU5kQ&feature=emb_logo
#https://www.youtube.com/watch?v=aRMxsTWHiKs

#pause function
#https://www.youtube.com/watch?v=sDL7P2Jhlh8&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=39

#buttons
#https://pythonprogramming.net/pygame-button-function/

#button outline thickness:
#https://www.youtube.com/watch?v=4_9twnEduFA

#pause
#https://www.youtube.com/watch?v=Et--T7SKHnk&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=17

#transparent images
#https://stackoverflow.com/questions/12879225/pygame-applying-transparency-to-an-image-with-alpha#16177852
#http://www.pygame.org/docs/ref/surface.html

#normal circle ontop of anti-alias one to give thickness
#https://www.reddit.com/r/pygame/comments/g9ttyx/is_there_a_way_to_draw_unfilled_anti_aliased/

pygame.init()
win = pygame.display.set_mode((800,600))

pygame.display.set_caption('Pong')
background = pygame.image.load("Atari.jpg").convert(24)
sys.setrecursionlimit(10000) # 10000 is an example, try with different values

white = (255, 255, 255)
black = (0, 0, 0)
gray = (176, 176, 176)

blue = (0,0,200)
red = (200,0,0)
green = (0,200,0)

bright_blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

class Leaderboard():
    def __init__(self):
        self.load_data()

    def load_data(self):
        #load high score
        self.dir = path.dirname(__file__)
        #with block
        #w = write
        with open(path.join(self.dir, "highscore.txt"), 'w') as f:
            #like try/catch block in java
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def draw_leaderboard(self):
        lead = True
        while lead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start_screen()

            background.set_alpha(150)
            win.fill(black)
            win.blit(background, (0, 0))

            # lines
            # vertical
            pygame.draw.line(win, white, (800 // 2 - 10, 50), (800 // 2 - 10, 50500), width=5)

            # horizontal
            pygame.draw.line(win, white, (0, 50), (850, 50), width=5)

            leaderboard_font = font.render("Leaderboard", True, white)
            win.blit(leaderboard_font, (800 // 2 - 100, 600 // 2 - 300))

            player_font = font.render("Player", True, white)
            win.blit(player_font, (800 // 2 - 300, 600 // 2 - 250))

            num_of_wins_font = font.render("Wins", True, white)
            win.blit(num_of_wins_font, (800 // 2 + 150, 600 // 2 - 250))
            pygame.display.flip()
            pygame.display.update()

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
text_box.append(Text_box(300,200, 200, 50, gray, border=3))

class Paddle1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,85])
        self.image.fill(bright_red)
        self.rect = self.image.get_rect()
        self.points = 0

    def reset(self):
        self.rect.x = 5
        self.rect.y = 225

class Paddle2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,85])
        self.image.fill(bright_blue)
        self.rect = self.image.get_rect()
        self.points = 0

    def reset(self):
        self.rect.x = 770
        self.rect.y = 225

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ball_image = pygame.Surface([20,20])

        pygame.draw.circle(ball_image, white, (10, 10), 10)
        self.image = ball_image
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, white, (8, 8), 8)

        self.speed = 12
        self.dx = 1
        self.dy = 1

    def reset(self):
        self.rect.x = 375
        self.rect.y = 250
        self.speed = 12
        self.dx = 1
        self.dy = 1

#locations
paddle1 = Paddle1()
paddle1.rect.x = 5
paddle1.rect.y = 225

paddle2 = Paddle2()
paddle2.rect.x = 770
paddle2.rect.y = 225

ball = Ball()
ball.rect.x = 375
ball.rect.y = 250

winner = 10
paddle_speed = 30

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)
font = pygame.font.SysFont('Arial', 30, bold=True)

lb = Leaderboard()

def redraw():
    win.fill(black)
    #lines
    #vertical
    pygame.draw.line(win, white, (800//2, 50), (800//2, 50500), width=5)

    #horizontal
    pygame.draw.line(win, white, (0,50), (850,50), width=5)

    #circle in center of game
    # drew a normal circle ontop of anti-alias one to give thickness
    pygame.draw.circle(win, white, (400, 300), 100, width=5)
    #anti-aliased circle - pygame.gfxdraw docs
    pygame.gfxdraw.aacircle(win, 400,300, 100, white)

    #Title Font
    text = font.render('Pong', True, white, 30)
    textRect = text.get_rect()
    textRect.center = (800//2, 25)
    win.blit(text, textRect)

    #Player 1 Score
    p1_score = font.render(str(paddle1.points), True, red)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (75, 25)
    win.blit(p1_score, p1Rect)

    # Player 2 Score
    p2_score = font.render(str(paddle2.points), True, blue)
    p2Rect = p1_score.get_rect()
    p2Rect.center = (675, 25)
    win.blit(p2_score, p2Rect)

    # winner
    if paddle1.points == winner:
        #resets the game after winning a game & clicking start again
        ball.reset()
        paddle1.reset()
        paddle2.reset()
        paddle1.points = 0
        paddle2.points = 0

        win.fill(black)
        winner_font = font.render("Player 1 wins!", True, white)
        win.blit(winner_font, (800 // 2 - 80, 600 // 2 - 20))
        screen = pygame.display.set_mode((800, 600))
        pygame.time.delay(2000)
        winners_name()
        # lb.draw_leaderboard()

    if paddle2.points == winner:
        # resets the game after winning a game & clicking start again
        ball.reset()
        paddle1.reset()
        paddle2.reset()
        paddle1.points = 0
        paddle2.points = 0

        win.fill(black)
        winner_font = font.render("Player 2 wins!", True, white)
        win.blit(winner_font, (800 // 2 - 80, 600 // 2 - 20))
        screen = pygame.display.set_mode((800, 600))
        pygame.time.delay(2000)
        winners_name()
        # lb.draw_leaderboard()

    all_sprites.draw(win)
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None, outline=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if outline:
        # *2 affects outline thickness
        pygame.draw.rect(win, outline, (x - 2 * 2, y - 2 * 2, w + 4 * 2, h + 4 * 2), 0)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))
        if click[0] == 1:
            if action == "play":
                game()

            elif action == "exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(win, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("Arial", 50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    win.blit(textSurf, textRect)

def winners_name():
    run = True
    while run:
        win.fill(black)
        # mouse clicks, etc
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for box in text_box:
                    # return pos of mouse
                    box.check_click(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                for box in text_box:
                    if box.active:
                        box.add_text(event.key)
                    if event.key == pygame.K_ESCAPE:
                        start_screen()
                    if event.key == pygame.K_TAB:
                        lb.draw_leaderboard()

        # win.fill(black)
        # font = pygame.font.SysFont('Arial', 30, bold=True)
        # input_font = font.render("Please enter your name:", True, white)
        # Text_box(300, 200)
        # win.blit(input_font, (800 // 2 - 170, 600 // 2 - 200))

        name_font = font.render("Press escape to return to the main menu", True, white)
        win.blit(name_font, (800 // 2 - 250, 600 // 2))

        for box in text_box:
            box.draw(win)
        pygame.display.update()

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.blit(background, (0, 0))
        button("Continue", 280, 200, 220, 60, green, bright_green, "play", black)
        button("Quit", 280, 350, 220, 60, red, bright_red, "exit", black)

        pygame.display.update()

def start_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.blit(background, (0, 0))
        button("Start",280,200,220,60,green,bright_green, "play", black)
        button("Quit",280, 350, 220, 60, red, bright_red, "exit", black)
        pygame.display.update()

def game():
    run = True
    while run:
        # gets rid of screen tearing going from start screen to game
        win.fill(black)
        redraw()#gets rid of screen tearing

        # changes speed of ball & paddles
        #fps
        pygame.time.delay(50)

        #mouse clicks, etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                if event.key == pygame.K_TAB:
                    lb.draw_leaderboard()

        key = pygame.key.get_pressed()

        #Paddle 1
        if key[pygame.K_w]:
            paddle1.rect.y -= paddle_speed

        if key[pygame.K_s]:
            paddle1.rect.y += paddle_speed

        #Paddle 2
        if key[pygame.K_UP]:
            paddle2.rect.y -= paddle_speed

        if key[pygame.K_DOWN]:
            paddle2.rect.y += paddle_speed

        ball.rect.x += ball.speed * ball.dx  #speed * direction
        ball.rect.y += ball.speed * ball.dy

        #collision with walls
        # bounce off top of the screen
        if ball.rect.y < 60:
            ball.dy = 1

        #bounce off bottom of the screen
        if ball.rect.y > 575:
            ball.dy = -1

        # bounce off right side of the screen
        if ball.rect.x > 780:
            ball.rect.x, ball.rect.y = 375, 250
            ball.dx = -1
            paddle1.points += 1

        # bounce off left side of the screen
        if ball.rect.x < 5:
            ball.rect.x, ball.rect.y = 375, 250
            ball.dx = 1
            paddle2.points += 1

        #collision with paddles
        if paddle1.rect.colliderect(ball.rect):
            ball.dx = 1
            os.system("afplay bounce.wav&")

        if paddle2.rect.colliderect(ball.rect):
            ball.dx = -1
            os.system("afplay bounce.wav&")

        #keep paddles from going off the screen
        #top
        if paddle1.rect.y < 55:
            paddle1.rect.y = 55

        if paddle2.rect.y < 55:
            paddle2.rect.y = 55

        #bottom
        if paddle1.rect.y > 510:
            paddle1.rect.y = 510

        if paddle2.rect.y > 510:
            paddle2.rect.y = 510


start_screen()
game()
pygame.quit()