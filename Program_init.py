import pygame
import sys
import random
import mysql.connector as m
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Autism iLearner')

passwd = 'Ac!$rB*6MySQL'

#Colors

White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Grey = (169,169,169)
Exp = (0, 255, 255)

#Background
bg = '5.png'
bg_image = pygame.transform.scale(pygame.image.load('FrontPage\\'+bg).convert_alpha(),(width, height))

#Font
Font = pygame.font.Font('Memory_cards\\Fonts\\Lilly\\Lilly__.ttf',100)
Font2 = pygame.font.Font('Memory_cards\\Fonts\\Quicksand\\Quicksand-Bold.otf',50)
Font3 = pygame.font.SysFont('Kristen ITC', 40)
Font4 = pygame.font.SysFont('Kristen ITC', 19)
#Music
Bg_Music = pygame.mixer.music.load('Memory_cards\\Sounds\\Bg_Music_2.3.mp3')

#Back Button
Back_txt = 'Back'
Back_Button = Font2.render(Back_txt, True, White)
Back_Button_Rect = Back_Button.get_rect(center = (width//5,19*height//20))

def sql_data_creation():
    try:
        con = m.connect(
            host = 'localhost',
            user = 'root',
            password = passwd)

        mycursor = con.cursor()

        mycursor.execute('create database if not exists autism')
        mycursor.execute('use autism')
        mycursor.execute('''create table if not exists user1
                         (game varchar(15), t_time int(5), date datetime default now())''')

    except Exception as e:
        print(e)

sql_data_creation()

def fade(width, height,bg, prog = 'in'): 

    fade = pygame.transform.scale(pygame.image.load('FrontPage\\'+bg).convert_alpha(),(width, height))
    
    if prog == 'in':
        prog_range = range(0,50)
    else:
        prog_range = range(50,0,-1)

    for alpha in prog_range:
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)

def Hover_color_change(Button_txt,Button_Rect, Color = Black):

    x,y = pygame.mouse.get_pos()
    
    if Button_Rect.collidepoint(x, y) == True:
        Button = Font2.render(Button_txt, True, Exp)
    
    else:
        Button = Font2.render(Button_txt, True, Color)

    return Button