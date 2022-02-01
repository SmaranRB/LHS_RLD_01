import pygame
import sys
import random
import time
pygame.init()

width = 1280
height = 720

Path_addn = 'Memory_cards'

White = (255,255,255)
Exp = (0, 255, 255)

Font = pygame.font.Font(Path_addn + '\\Fonts\\Lilly\\Lilly__.ttf',25)
Font2 = pygame.font.Font(Path_addn + '\\Fonts\\Quicksand\\Quicksand-Bold.otf',50)

Back_txt = 'Back'
Back_Button = Font2.render(Back_txt, True, White)
Back_Button_Rect = Back_Button.get_rect(center = (width//2,19*height//20))