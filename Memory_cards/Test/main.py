import pygame
import sys
import random
pygame.init()

Font = pygame.font.Font('Fonts\\Lilly\\Lilly__.ttf',25)
Font2 = pygame.font.Font('Fonts\\Quicksand\\Quicksand-Bold.otf',50)
Bg_Music = pygame.mixer.music.load('Sounds\\Bg_Music_2.3.mp3')

def Background(Width = 800 ,Height = 400):
    Bg =  pygame.transform.scale(pygame.image.load('Assets\\Bg\\Bg.jpg').convert_alpha(),(Width,Height))
    screen =Load_Screen(Width, Height)#Loading background onto the window
    screen.blit(Bg,(0,0))
    
    return Width,Height,screen , Bg

def Load_Images(Width,Height,screen):
    #Assets\Cards 1\Green_Card.png
    L = ['Cards 1\\Green_Card','Cards 1\\Red_Card']
    File_Selected = random.sample(L, 1)[0]
    if File_Selected == 'Cards 1\\Green_Card':
        File_Selected_2 = 'Cards 1\\Red_Card'

    else:
        File_Selected_2 = 'Cards 1\\Green_Card'

    L2 = [(1,2),(2,3),(1,3)]
    Combination_Selected = random.sample(L2,1)[0]

    Img_Size = (100,140)

    if Combination_Selected == (1,2): # Elents in same column are same
        
        Tile_1 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'.png').convert_alpha(), Img_Size)
        Tile_1_Rect = Tile_1.get_rect(center = (Width//3,Height//3))

        Tile_2 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected_2+'.png').convert_alpha(), Img_Size)
        Tile_2_Rect = Tile_2.get_rect(center = (2*Width//3,Height//3))

        Tile_3 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected_2+'.png').convert_alpha(),Img_Size)
        Tile_3_Rect = Tile_3.get_rect(center = (2*Width//3,2*Height//3))

        Tile_4 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'.png').convert_alpha(),Img_Size)
        Tile_4_Rect = Tile_4.get_rect(center = (Width//3,2*Height//3))

    elif Combination_Selected == (2,3): # Elements in same row are same 
        
        Tile_1 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'.png').convert_alpha(),Img_Size)
        Tile_1_Rect = Tile_1.get_rect(center = (Width//3,Height//3))

        Tile_2 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'.png').convert_alpha(), Img_Size)
        Tile_2_Rect = Tile_2.get_rect(center = (2*Width//3,Height//3))

        Tile_3 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected_2+'.png').convert_alpha(), Img_Size)
        Tile_3_Rect = Tile_3.get_rect(center = (2*Width//3,2*Height//3))

        Tile_4 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected_2+'.png').convert_alpha(),Img_Size)
        Tile_4_Rect = Tile_4.get_rect(center = (Width//3,2*Height//3))

    elif Combination_Selected == (1,3): # Diagonal elements are same
        
        Tile_1 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'.png').convert_alpha(), Img_Size)
        Tile_1_Rect = Tile_1.get_rect(center = (Width//3,Height//3))

        Tile_2 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected_2+'.png').convert_alpha(), Img_Size)
        Tile_2_Rect = Tile_2.get_rect(center = (2*Width//3,Height//3))

        Tile_3 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'.png').convert_alpha(), Img_Size)
        Tile_3_Rect = Tile_3.get_rect(center = (2*Width//3,2*Height//3))

        Tile_4 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected_2+'.png').convert_alpha(), Img_Size)
        Tile_4_Rect = Tile_4.get_rect(center = (Width//3,2*Height//3))    

    Grey_Tile = pygame.transform.scale(pygame.image.load('Assets\\White_Card.png').convert_alpha(), Img_Size)


    return File_Selected, File_Selected_2, Combination_Selected, Grey_Tile, Tile_1,Tile_1_Rect , Tile_2,Tile_2_Rect , Tile_3,Tile_3_Rect , Tile_4,Tile_4_Rect

def Flip_animation(screen, Grey_Tile, Tile , File_Selected, Tile_Rect, sec_Tile, sec_Tile_rect, sec_Tile_Match,sec_Tile_Click , tert_Tile, tert_Tile_rect , tert_Tile_Match, tert_Tile_Click,  quat_Tile, quat_Tile_rect  , quat_Tile_Match ,quat_Tile_Click , Dir , Bg):
    
    Img_Size = (100,140)
    File_Selected_w = 'White_Card'
    Delay = 15

    Frame_1 = pygame.transform.scale(pygame.image.load('Assets\\White_Card1.png').convert_alpha(), Img_Size)
    Frame_2 = pygame.transform.scale(pygame.image.load('Assets\\White_Card2.png').convert_alpha(), Img_Size)
    Frame_3 = pygame.transform.scale(pygame.image.load('Assets\\White_Card3.png').convert_alpha(), Img_Size)

    Frame_90_deg = pygame.transform.scale(pygame.image.load('Assets\\90_Deg.png').convert_alpha(), Img_Size)

    Frame_4 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'1.png').convert_alpha(), Img_Size)
    Frame_5 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'2.png').convert_alpha(), Img_Size)
    Frame_6 = pygame.transform.scale(pygame.image.load('Assets\\'+File_Selected+'3.png').convert_alpha(), Img_Size)
    
    if Dir == '+ve':
        i = 0

        for i in range(9):
            
            screen.blit(Bg,(0,0))

            if sec_Tile_Match or sec_Tile_Click:
                screen.blit(sec_Tile,sec_Tile_rect)

            else:
                screen.blit(Grey_Tile,sec_Tile_rect)
            
            if tert_Tile_Match or tert_Tile_Click:
                screen.blit(tert_Tile, tert_Tile_rect)
            
            else:
                screen.blit(Grey_Tile,tert_Tile_rect)

            if quat_Tile_Match or quat_Tile_Click:
                screen.blit(quat_Tile,quat_Tile_rect)

            else:
                screen.blit(Grey_Tile,quat_Tile_rect)

            if i == 0:

                screen.blit(Grey_Tile, Tile_Rect)

            elif i == 1:
                
                screen.blit(Frame_1, Tile_Rect)

            elif i ==2:    
                
                screen.blit(Frame_2, Tile_Rect)

            elif i == 3:
                
                screen.blit(Frame_3, Tile_Rect)
                
            elif i == 4:
                
                screen.blit(Frame_90_deg, Tile_Rect)

            elif i == 5:    
                
                screen.blit(pygame.transform.flip(Frame_4,True,False), Tile_Rect)

            elif i == 6:    
                
                screen.blit(pygame.transform.flip(Frame_5,True,False), Tile_Rect)

            elif i == 7:    
                
                screen.blit(pygame.transform.flip(Frame_6,True,False), Tile_Rect)

            elif i == 8:

                screen.blit(Tile, Tile_Rect)
        
            pygame.display.update()
            pygame.time.delay(Delay)

    elif Dir == '-ve':
        i = 0

        for i in range(9):

            screen.blit(Bg,(0,0))

            if sec_Tile_Match or sec_Tile_Click:
                screen.blit(sec_Tile,sec_Tile_rect)

            else:
                screen.blit(Grey_Tile,sec_Tile_rect)
            
            if tert_Tile_Match or tert_Tile_Click:
                screen.blit(tert_Tile, tert_Tile_rect)
            
            else:
                screen.blit(Grey_Tile,tert_Tile_rect)

            if quat_Tile_Match or quat_Tile_Click:
                screen.blit(quat_Tile,quat_Tile_rect)

            else:
                screen.blit(Grey_Tile,quat_Tile_rect)

            if i == 0:

                screen.blit(Grey_Tile, Tile_Rect)
            
            elif i == 1:
                
                screen.blit(Frame_4, Tile_Rect)

            elif i == 2:    
                
                screen.blit(Frame_5, Tile_Rect)

            elif i == 3:
                
                screen.blit(Frame_6, Tile_Rect)
                
            elif i == 4:
                
                screen.blit(Frame_90_deg, Tile_Rect)

            elif i ==5:    
                
                screen.blit(pygame.transform.flip(Frame_3,True,False), Tile_Rect)

            elif i ==6:    
                
                screen.blit(pygame.transform.flip(Frame_2,True,False), Tile_Rect)

            elif i ==7:    
                
                screen.blit(pygame.transform.flip(Frame_1,True,False), Tile_Rect)

            elif i == 8:

                screen.blit(Grey_Tile, Tile_Rect)
    
            pygame.display.update()
            pygame.time.delay(Delay)

def Mouse(screen,Bg,Grey_Tile,Tile_1,Tile_1_Rect,Width,Height,Tile_2,Tile_2_Rect, Tile_1_Num,Tile_2_Num,Tile_3_Num,Tile_4_Num, Tile_3,Tile_3_Rect, Tile_4,Tile_4_Rect, Click1, Click2, Click3, Click4, Tile_1_Match,Tile_2_Match,Tile_3_Match,Tile_4_Match):

    Mouse_Pos = pygame.mouse.get_pos()
    Click = pygame.mouse.get_pressed()[0]

    screen.blit(Bg,(0,0))

    if  Tile_1_Match == False:    

        if Tile_1_Rect.collidepoint(Mouse_Pos):
            if Click:
                screen.blit(Tile_1,Tile_1_Rect)
                Click1 = 1
                Flip_animation(screen, Grey_Tile, Tile_1, Tile_1_Num, Tile_1_Rect , Tile_2,Tile_2_Rect,Tile_2_Match,Click2, Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4 , '+ve', Bg)
            
            elif Click1 == 1:
                screen.blit(Tile_1, Tile_1_Rect)
            
            else:
                screen.blit(Grey_Tile, Tile_1_Rect)        

        elif Click1 == 1:
            screen.blit(Tile_1, Tile_1_Rect)

        else:
            screen.blit(Grey_Tile, Tile_1_Rect)

    elif Tile_1_Match == True:
        screen.blit(Tile_1, Tile_1_Rect)
        Click1 = 2
    
    if Tile_2_Match == False:
        if Tile_2_Rect.collidepoint(Mouse_Pos):
            if Click:
                screen.blit(Tile_2, Tile_2_Rect)
                Click2 = 1
                Flip_animation(screen, Grey_Tile, Tile_2, Tile_2_Num, Tile_2_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4, '+ve', Bg)
            
            elif Click2 == 1:
                screen.blit(Tile_2, Tile_2_Rect)
            
            else:
                screen.blit(Grey_Tile, Tile_2_Rect)        

        elif Click2 == 1:
            screen.blit(Tile_2, Tile_2_Rect)

        else:
            screen.blit(Grey_Tile, Tile_2_Rect)

    elif Tile_2_Match == True:
        screen.blit(Tile_2, Tile_2_Rect)
        Click2 = 2
    
    if Tile_3_Match == False:
        if Tile_3_Rect.collidepoint(Mouse_Pos):
            if Click:
                screen.blit(Tile_3, Tile_3_Rect)
                Click3 = 1
                Flip_animation(screen, Grey_Tile, Tile_3, Tile_3_Num, Tile_3_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_4,Tile_4_Rect,Tile_4_Match,Click4, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '+ve', Bg)
            
            elif Click3 == 1:
                screen.blit(Tile_3, Tile_3_Rect)
            
            else:
                screen.blit(Grey_Tile, Tile_3_Rect)        

        elif Click3 == 1:
            screen.blit(Tile_3, Tile_3_Rect)

        else:
            screen.blit(Grey_Tile, Tile_3_Rect)
    
    elif Tile_3_Match == True:
        screen.blit(Tile_3, Tile_3_Rect)
        Click3 = 2

    if Tile_4_Match == False:
        if Tile_4_Rect.collidepoint(Mouse_Pos):
            if Click:
                screen.blit(Tile_4, Tile_4_Rect)
                Click4 = 1
                Flip_animation(screen, Grey_Tile, Tile_4, Tile_4_Num, Tile_4_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '+ve', Bg)
    
            elif Click4 == 1:
                screen.blit(Tile_4, Tile_4_Rect)
            
            else:
                screen.blit(Grey_Tile, Tile_4_Rect)        

        elif Click4 == 1:
            screen.blit(Tile_4, Tile_4_Rect)

        else:
            screen.blit(Grey_Tile, Tile_4_Rect)

    elif Tile_4_Match == True:
        screen.blit(Tile_4, Tile_4_Rect)
        Click4 = 2
    
    return Click1, Click2, Click3, Click4

def Assign_Num(File_Selected,File_Selected_2, Combination_Selected):

    Card1 = File_Selected
    Card2 = File_Selected_2

    if Combination_Selected == (1,2):
            Tile_1_Num = Card1
            Tile_2_Num = Card2
            Tile_3_Num = Card2
            Tile_4_Num = Card1

    elif Combination_Selected == (2,3):
            Tile_1_Num = Card1
            Tile_2_Num = Card1
            Tile_3_Num = Card2
            Tile_4_Num = Card2

    elif Combination_Selected == (1,3):
            Tile_1_Num = Card1
            Tile_2_Num = Card2
            Tile_3_Num = Card1
            Tile_4_Num = Card2
        
    return Tile_1_Num, Tile_2_Num, Tile_3_Num, Tile_4_Num

def Compare(Bg,Grey_Tile, screen, Click1,Click2,Click3,Click4, Combination_Selected, Tile_1,Tile_2,Tile_3,Tile_4, Tile_1_Num,Tile_2_Num,Tile_3_Num,Tile_4_Num, Tile_1_Rect,Tile_2_Rect,Tile_3_Rect,Tile_4_Rect, Tile_1_Match , Tile_2_Match , Tile_3_Match , Tile_4_Match):

    Delay = 700

    if Click1 == 1 and Click4 == 1:

        if Tile_1_Num == Tile_4_Num:
            
            print('Match')
            Tile_1_Match = True
            Tile_4_Match = True
        
        else :
            screen.blit(Tile_1, Tile_1_Rect)
            screen.blit(Tile_4, Tile_4_Rect)
            pygame.display.update()

            pygame.time.delay(Delay)
            Flip_animation(screen, Grey_Tile, Tile_1, Tile_1_Num, Tile_1_Rect , Tile_2,Tile_2_Rect,Tile_2_Match,Click2, Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4 , '-ve', Bg)
            Click1 = 0
            Flip_animation(screen, Grey_Tile, Tile_4, Tile_4_Num, Tile_4_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '-ve', Bg)
            Click4 = 0

    if Click1 == 1 and Click2 ==1:
 
        if Tile_1_Num == Tile_2_Num:
            
            print('Match')
            Tile_1_Match = True
            Tile_2_Match = True
       
        else :
            screen.blit(Tile_1, Tile_1_Rect)
            screen.blit(Tile_2, Tile_2_Rect)
            pygame.display.update()

            pygame.time.delay(Delay)
            Flip_animation(screen, Grey_Tile, Tile_1, Tile_1_Num, Tile_1_Rect , Tile_2,Tile_2_Rect,Tile_2_Match,Click2, Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4 , '-ve', Bg)
            Click1 = 0
            Flip_animation(screen, Grey_Tile, Tile_2, Tile_2_Num, Tile_2_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 ,Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4, '-ve', Bg)
            Click2 = 0

    if Click1 == 1 and Click3 == 1:

        if Tile_1_Num == Tile_3_Num:
            
            print('Match')
            Tile_1_Match = True
            Tile_3_Match = True
                  
        else :
            screen.blit(Tile_1, Tile_1_Rect)
            screen.blit(Tile_3, Tile_3_Rect)
            pygame.display.update()

            pygame.time.delay(Delay)
            Flip_animation(screen, Grey_Tile, Tile_1, Tile_1_Num, Tile_1_Rect , Tile_2,Tile_2_Rect,Tile_2_Match,Click2, Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4 , '-ve', Bg)
            Click1 = 0
            Flip_animation(screen, Grey_Tile, Tile_3, Tile_3_Num, Tile_3_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_4,Tile_4_Rect,Tile_4_Match,Click4, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '-ve', Bg)
            Click3 = 0

    ###############################################
    if Click2 == 1 and Click4 == 1:

        if Tile_2_Num == Tile_4_Num:
            
            print('Match')
            Tile_2_Match = True
            Tile_4_Match = True
       
        else :
            screen.blit(Tile_2, Tile_2_Rect)
            screen.blit(Tile_4, Tile_4_Rect)
            pygame.display.update()

            pygame.time.delay(Delay)
            Flip_animation(screen, Grey_Tile, Tile_2, Tile_2_Num, Tile_2_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 ,Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4, '-ve', Bg)
            Click2 = 0
            Flip_animation(screen, Grey_Tile, Tile_4, Tile_4_Num, Tile_4_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '-ve', Bg)
            Click4 = 0 

    if Click2 == 1 and Click3 ==1:

        if Tile_2_Num == Tile_3_Num:
            
            print('Match')
            Tile_2_Match = True
            Tile_3_Match = True
        
        else :
            screen.blit(Tile_2, Tile_2_Rect)
            screen.blit(Tile_3, Tile_3_Rect)
            pygame.display.update()

            pygame.time.delay(Delay)
            Flip_animation(screen, Grey_Tile, Tile_2, Tile_2_Num, Tile_2_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 ,Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4, '-ve', Bg)
            Click2 = 0
            Flip_animation(screen, Grey_Tile, Tile_3, Tile_3_Num, Tile_3_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_4,Tile_4_Rect,Tile_4_Match,Click4, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '-ve', Bg)
            Click3 = 0

    ###############################################
    if Click3 == 1 and Click4 == 1:

        if Tile_3_Num == Tile_4_Num:
            
            print('Match')
            Tile_3_Match = True
            Tile_4_Match = True
        
        else :
            screen.blit(Tile_3, Tile_3_Rect)
            screen.blit(Tile_4, Tile_4_Rect)
            pygame.display.update()

            pygame.time.delay(Delay)
            Flip_animation(screen, Grey_Tile, Tile_3, Tile_3_Num, Tile_3_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_4,Tile_4_Rect,Tile_4_Match,Click4, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '-ve', Bg)
            Click3 = 0     
            Flip_animation(screen, Grey_Tile, Tile_4, Tile_4_Num, Tile_4_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '-ve', Bg)
            Click4 = 0

    return Click1, Click2 ,Click3 ,Click4 , Tile_1_Match,Tile_2_Match,Tile_3_Match,Tile_4_Match

def Load_Screen(Width,Height): #Loading the window

    screen = pygame.display.set_mode((Width,Height))
    return screen

def Win(Tile_1_Match,Tile_2_Match,Tile_3_Match,Tile_4_Match, screen,Width,Height):

    if Tile_1_Match == Tile_2_Match == Tile_3_Match == Tile_4_Match == True:

        Txt1 = Font2.render('Yay! You Won!', 0, (255,255,255)).convert_alpha()
        Txt1_rect = Txt1.get_rect(center = (Width//2,Height//2))
        screen.blit(Txt1,Txt1_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        return 'Win +ve'

def main():
    if __name__ == '__main__': # If file is internally being executed
        Load_Screen(800,450)

    pygame.mixer.music.set_volume(1)

    pygame.mixer.music.play(-1)

    Width,Height,screen,Bg = Background(1280,720)

    Click1, Click2, Click3, Click4 = 0,0,0,0
    Click_1, Click_2, Click_3, Click_4 = 0,0,0,0

    Tile_1_Match , Tile_2_Match , Tile_3_Match , Tile_4_Match = False,False,False,False

    File_Selected, File_Selected_2, Combination_Selected, Grey_Tile,Tile_1,Tile_1_Rect,Tile_2,Tile_2_Rect, Tile_3,Tile_3_Rect, Tile_4,Tile_4_Rect = Load_Images(Width, Height, screen)
    
    clock = pygame.time.Clock()

    Tile_1_Num, Tile_2_Num, Tile_3_Num, Tile_4_Num = Assign_Num(File_Selected, File_Selected_2, Combination_Selected)

    while True:

        for event in pygame.event.get(): # Handling user input
            
            if event.type == pygame.QUIT: # Handling User input to quit game
                pygame.quit()
                sys.exit() #Safely exits the code

        #Mouse_Pos = pygame.mouse.get_pos()
        
        Click1, Click2, Click3, Click4 = Mouse(screen, Bg, Grey_Tile, Tile_1, Tile_1_Rect, Width, Height, Tile_2, Tile_2_Rect, Tile_1_Num, Tile_2_Num, Tile_3_Num, Tile_4_Num, Tile_3, Tile_3_Rect, Tile_4, Tile_4_Rect, Click1, Click2, Click3, Click4, Tile_1_Match, Tile_2_Match, Tile_3_Match, Tile_4_Match)
        
        Click1, Click2 ,Click3 ,Click4 , Tile_1_Match,Tile_2_Match,Tile_3_Match,Tile_4_Match = Compare(Bg ,Grey_Tile, screen, Click1, Click2, Click3, Click4, Combination_Selected, Tile_1, Tile_2, Tile_3, Tile_4, Tile_1_Num, Tile_2_Num, Tile_3_Num, Tile_4_Num, Tile_1_Rect, Tile_2_Rect, Tile_3_Rect, Tile_4_Rect, Tile_1_Match, Tile_2_Match, Tile_3_Match, Tile_4_Match)
        
        Win_Check = Win(Tile_1_Match, Tile_2_Match, Tile_3_Match, Tile_4_Match,screen,Width,Height)

        pygame.display.update() # refreshes the contents of the screen

        clock.tick(60)

        if Win_Check == 'Win +ve':
            break

if __name__ == '__main__':
    main()
    pygame.quit()