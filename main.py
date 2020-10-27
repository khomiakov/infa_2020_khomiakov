import pygame
import pygame.draw as d
from random import randint

pygame.init()

FPS = 30
window_heigth = 600
tablo_height = 50
window_length = 1200
screen = pygame.display.set_mode((window_length, window_heigth))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball():
    def __init__(self, color, x, y, r, speed_x, speed_y, lives):
        """

        :param color:
        :param x:  projection of center of the circle on x
        :param y: projection of center of the circle on y
        :param r: radius of the circle
        :param speed_x: projection of speed on x
        :param speed_y: projection of speed on y
        :param lives: lives of the circle
        """
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.lives = lives
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        '''
        this function moves the ball
        :return:
        '''
        self.x += self.speed_x
        self.y += self.speed_y
        d.circle(screen, self.color, (self.x, self.y), self.r)

    def change_color(self, color):
        '''
        this function changes color
        :param color:
        :return:
        '''
        self.color = color

    def change_speed(self, speed_x, speed_y):
        '''
        this function changes projections of speed
        :param speed_x:
        :param speed_y:
        :return:
        '''
        self.speed_x = speed_x
        self.speed_y = speed_y

    def lose_life(self):
        self.lives += -1

    def remove_ball(self):
        '''
        this function removes ball
        :return:
        '''
        d.circle(screen, BLACK, (self.x, self.y), self.r)

    def near_top_wall(self, tablo_height):
        '''
        :param tablo_height: distance for text 'score:'
        :return: true if ball is touching top of the window
        '''

        if self.y - self.r < 10 + tablo_height:
            return True
        else:
            return False

    def near_left_wall(self):
        '''

        :return: True if ball is touching left wall of the window
        '''
        if self.x - self.r < 10:
            return True
        else:
            return False

    def near_right_wall(self, window_length):
        '''

        :param window_length: length of screen
        :return: True if ball is touching right wall of the window
        '''
        if window_length - 10 < self.x + self.r:
            return True
        else:
            return False

    def near_bottom_wall(self, window_height):
        '''

        :param window_height: height of screen
        :return: True if ball is touching bottom of the window
        '''
        if window_height - 10 < self.y + self.r:
            return True
        else:
            return False

    def click_not_miss(self, click_x, click_y, ):
        '''

        :param click_x: x position of mouse
        :param click_y: y position of mouse
        :return: True if you clicks on ball
        '''
        if (click_x - self.x) ** 2 + (click_y - self.y) ** 2 <= self.r ** 2:
            return True
        else:
            return False

    def text_lives(self):
        '''
        this function types count of lives in the center of ball
        :return:
        '''
        font_size = 30
        param_text = pygame.font.SysFont('calibri', font_size)
        text_place = param_text.render(str(self.lives), 1, BLACK)
        screen.blit(text_place, (self.x - int(font_size / 3), self.y - int(font_size / 2)))


# it's a rectangle button with text in center
class mfti_button():
    def __init__(self, color, x, y, speed_x, speed_y, length, height, text_color, lives):
        '''

        :param color: color of button
        :param x: projection of center of button on x
        :param y: projection of center of button on y
        :param speed_x: projection of speed on x
        :param speed_y: projection of speed on y
        :param length: length of rect.
        :param height: height of rect
        :param text_color: color of the text
        :param lives: lives of button connecting with the text
        '''
        self.color = color
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.length = length
        self.height = height
        self.text_color = text_color
        self.lives = lives

    # functions typing text
    def be_lazy(self):
        '''
        this function types text 'be lazy' in the center of button
        :return:
        '''
        font_size = int(self.height / 2)  # size of the font
        param_text = pygame.font.SysFont('calibri', font_size)  # some parameters of the font
        text_ren = param_text.render('be lazy', 1, self.text_color)  # rendering text
        screen.blit(text_ren, (
            int(self.x - font_size * 1.5), int(self.y - font_size * 0.5)))  # bliting text in the center of button

    def be_lay(self):
        '''
        this function types text 'be lay' in the center of button
        :return:
        '''
        font_size = int(self.height / 2)
        param_text = pygame.font.SysFont('calibri', font_size)
        text_ren = param_text.render('be lay', 1, self.text_color)
        screen.blit(text_ren, (int(self.x - font_size * 1.5), int(self.y - font_size * 0.5)))

    def bo_lay(self):
        '''
        this function types text 'bo lay' in the center of button
        :return:
        '''
        font_size = int(self.height / 2)
        param_text = pygame.font.SysFont('calibri', font_size)
        text_ren = param_text.render('bo lay', 1, self.text_color)
        screen.blit(text_ren, (int(self.x - font_size * 1.5), int(self.y - font_size * 0.5)))

    def boltay(self):
        '''
        this function types text 'boltay' in the center of button
        :return:
        '''
        font_size = int(self.height / 2)
        param_text = pygame.font.SysFont('calibri', font_size)
        text_ren = param_text.render('boltay', 1, self.text_color)
        screen.blit(text_ren, (int(self.x - font_size * 1.5), int(self.y - font_size * 0.5)))

    def botay(self):
        '''
        this function types text 'botay' in the center of button
        :return:
        '''
        font_size = int(self.height / 2)
        param_text = pygame.font.SysFont('calibri', font_size)
        text_ren = param_text.render('botay', 1, self.text_color)
        screen.blit(text_ren, (int(self.x - font_size * 1.5), int(self.y - font_size * 0.5)))

    def BOTAY(self):
        '''
        this function types text 'BOTAY!' in the center of button
        :return:
        '''
        font_size = int(self.height / 2)
        param_text = pygame.font.SysFont('calibri', font_size)
        text_ren = param_text.render('BOTAY!', 1, RED)
        screen.blit(text_ren, (int(self.x - font_size * 1.5), int(self.y - font_size * 0.5)))

    # movement functions
    def move(self):
        '''
        this function moves button
        :return:
        '''
        self.x += self.speed_x
        self.y += self.speed_y
        d.rect(screen, self.color, (self.x - int(self.length / 2), self.y - int(self.height / 2), self.length,
                                    self.height))

    def change_speed_grav(self, mouse_x, mouse_y):
        '''
        this function creates gravitation between mouse and button by changing speed
        :param mouse_x: x position of mouse
        :param mouse_y: y position of mouse
        :return:
        '''
        k = 20000  # coeffitient of prportionality in gravitation
        r_square = (mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2  # distance^2 between center of rect. and mouse
        if (r_square > 100):  # we are turning off gravity if rect near mouse
            if mouse_x - self.x != 0:
                self.speed_x += int(k / (r_square) ** 1.5 * abs(mouse_x - self.x) + 1) * abs(mouse_x - self.x) / (
                        mouse_x - self.x)
            if mouse_y - self.y != 0:
                self.speed_y += int(k / (r_square) ** 1.5 * abs(mouse_y - self.y) + 1) * abs(mouse_y - self.y) / (
                        mouse_y - self.y)
        # if r_square too big gravitation becoming common power proportional acceleration equal 1

    def change_speed(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    # functions of walls
    def near_top_wall(self, tablo_height):
        '''

        :param tablo_height: distance for text 'score:'
        :return: True if rect is touching top of the window
        '''
        if self.y - int(self.height / 2) < 10 + tablo_height:
            return True
        else:
            return False

    def near_left_wall(self):
        '''

        :return: True if rect is touching left wall of the window
        '''
        if self.x - int(self.length / 2) < 10:
            return True
        else:
            return False

    def near_right_wall(self, window_length):
        '''

        :param window_length: length of screen
        :return: True if rect is touching right wall of the window
        '''

        if window_length - 10 < self.x + int(self.length / 2):
            return True
        else:
            return False

    def near_bottom_wall(self, window_height):
        '''

        :param window_height: height of screen
        :return: True if rect is touching bottom of the window
        '''
        if window_height - 10 < self.y + int(self.height / 2):
            return True
        else:
            return False

    def click_not_miss(self, click_x, click_y):
        '''

        :param click_x: x position of mouse
        :param click_y: y position of mouse
        :return: True if you clicks on button
        '''
        if abs(click_x - self.x) < abs(self.length / 2) and abs(click_y - self.y) > abs(self.height / 2):
            return True
        else:
            return False

    def lose_life(self):
        self.lives += -1


def text(points, window_length, tablo_height):
    '''
    this function types your points on the top of screen
    :param points: points that you get
    :param window_length: length of screen
    :param tablo_height: distance for text 'score:'
    :return:
    '''
    param_text = pygame.font.SysFont('calibri', tablo_height - 10)
    text_ren = param_text.render(points, 1, WHITE)
    screen.blit(text_ren, (int(window_length / 2) - 20, 5))


rmin = 20  # minimal radius of ball
rmax = 60  # maximal radius of ball
vmax = 10  # maximal speed of ball and rect
vmin = -10  # minimal speed of ball and rect
length_button = 100
height_button = 60
# creating objects
t = mfti_button(COLORS[randint(0, 5)], randint(int(length_button / 2), window_length - int(length_button / 2)),
                randint(int(height_button / 2) + tablo_height, window_heigth - int(length_button / 2)), 0, 0,
                length_button, height_button, BLACK, 6)
a = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50), randint(tablo_height + 50, window_heigth - 50),
         randint(rmin, rmax), randint(vmin, vmax),
         randint(vmin, vmax), 10)
b = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50), randint(tablo_height + 50, window_heigth - 50),
         randint(rmin, rmax), randint(vmin, vmax),
         randint(vmin, vmax), 10)
c = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50), randint(tablo_height + 50, window_heigth - 50),
         randint(rmin, rmax), randint(vmin, vmax),
         randint(vmin, vmax), 10)
e = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50), randint(tablo_height + 50, window_heigth - 50),
         randint(rmin, rmax), randint(vmin, vmax),
         randint(vmin, vmax), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = event.pos
            all_balls = [a, b, c, e, t]
            all_lives = [a.lives, b.lives, c.lives, e.lives, t.lives]
            for i in range(0, 5):
                if all_balls[i].click_not_miss(click_x, click_y) == True:
                    all_balls[i].lose_life()
                    if (all_balls[i].lives == 0) and (i == 4):
                        all_balls[i].lives = 1
                    if i == 4:
                        points += 5
                    else:
                        points += 1
                    all_balls[i].color = COLORS[randint(0, 5)]
                #removing ball
                if all_lives[i] == 1:
                    if i != 4:
                        all_balls[i].remove_ball()
                        all_balls[i].x = randint(50, window_length - 50)
                        all_balls[i].y = randint(tablo_height + 50, window_heigth - 50)
                        all_balls[i].r = randint(rmin, rmax)
                        all_balls[i].speed_x = randint(vmin, vmax)
                        all_balls[i].speed_y = randint(vmin, vmax)
                        all_balls[i].lives = 10
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            t.change_speed_grav(mouse_x, mouse_y)
    all_balls = [a, b, c, e, t]
    # if object touches wall
    for i in range(0, 5):
        if all_balls[i].near_top_wall(tablo_height) == True:
            all_balls[i].change_speed(randint(vmin, vmax), randint(1, vmax))
        if all_balls[i].near_bottom_wall(window_heigth) == True:
            all_balls[i].change_speed(randint(vmin, vmax), randint(vmin, -1))
        if all_balls[i].near_right_wall(window_length) == True:
            all_balls[i].change_speed(randint(vmin, -1), randint(vmin, vmax))
        if all_balls[i].near_left_wall() == True:
            all_balls[i].change_speed(randint(1, vmax), randint(vmin, vmax))
        all_balls[i].move()
        if i != 4:
            all_balls[i].text_lives()
    # changing text on the button
    if t.lives == 6:
        t.be_lazy()
    if t.lives == 5:
        t.be_lay()
    if t.lives == 4:
        t.bo_lay()
    if t.lives == 3:
        t.boltay()
    if t.lives == 2:
        t.botay()
    if t.lives == 1:
        t.BOTAY()
    pygame.display.update()
    screen.fill(BLACK)
    text('score: ' + str(points), window_length, tablo_height)
pygame.quit()
