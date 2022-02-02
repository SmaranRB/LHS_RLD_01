import pygame
#from pygame import movie
import sys

File = 'Red_Card'

screen = pygame.display.set_mode((800,800))
Bg =  pygame.transform.scale(pygame.image.load('Assets\\Cards 1\\'+File+'.png').convert_alpha(),(50*2,70*2))
Bg2 =  pygame.transform.scale(pygame.image.load('Assets\\Cards 1\\'+File+'1.png').convert_alpha(),(50*2,70*2))
Bg3 =  pygame.transform.scale(pygame.image.load('Assets\\Cards 1\\'+File+'2.png').convert_alpha(),(50*2,70*2))
Bg4 =  pygame.transform.scale(pygame.image.load('Assets\\Cards 1\\'+File+'3.png').convert_alpha(),(50*2,70*2))
Bg5 =  pygame.transform.scale(pygame.image.load('Assets\\90_Deg.png').convert_alpha(),(50*2,70*2))

i = 0
'''
movie = pygame.movie.Movie('D:\\xyz.mp4')
mrect = movie.get_rect(center = (400,400))
movie.set_display(screen, mrect.move(65, 150))
movie.set_volume(0)
movie.play()
'''
while True:

    i+=1

    for event in pygame.event.get(): # Handling user input
            
        if event.type == pygame.QUIT: # Handling User input to quit game
            pygame.quit()
            sys.exit() #Safely exits the code

    if i % 8 == 0:
        screen.fill((255,255,0))
        screen.blit(Bg, (350,350))

    elif (i-1)%8 ==0:    
        screen.fill((255,255,0))
        screen.blit(Bg2, (350,350))

    elif (i-2)%8 == 0:
        screen.fill((255,255,0))
        screen.blit(Bg3, (350,350))
        
    elif (i-3)%8 == 0:
        screen.fill((255,255,0))
        screen.blit(Bg4, (350,350))

    elif (i-4)%8 ==0:    
        screen.fill((255,255,0))
        screen.blit(Bg5, (350,350))

    elif (i-5)%8 == 0:
        screen.fill((255,255,0))
        screen.blit(pygame.transform.flip(Bg4,True,False), (350,350))
        
    elif (i-6)%8 == 0:
        screen.fill((255,255,0))
        screen.blit(pygame.transform.flip(Bg3,True,False), (350,350))

    elif (i-7)%8 == 0:
        screen.fill((255,255,0))
        screen.blit(pygame.transform.flip(Bg2,True,False), (350,350))

    pygame.display.update()
    pygame.time.Clock().tick(60)