from Program_init import Hover_color_change
from Memory_cards.Program_init import *
from Memory_cards.Emoji import *

game = 'mmc' 

Path_addn = 'Memory_cards\\'

def Background(screen,Bg_img, Width, Height):
    Bg =  pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\Bg\\'+Bg_img+'.jpg').convert_alpha(),(Width,Height))
    #screen =Load_Screen(Width, Height)#Loading background onto the window
    screen.blit(Bg,(0,0))
    
    return Width,Height,Bg

def Select_File(L):

    #L = ['Cards 1\\Green_Card','Cards 1\\Red_Card']
    File_Selected = random.sample(L, 1)[0]
    if File_Selected == L[0]:
        File_Selected_2 = L[1]

    else:
        File_Selected_2 = L[0]
    
    return File_Selected, File_Selected_2 

def Load_Images(Width,Height,screen,File_Selected,File_Selected_2):
    
    L2 = [(1,2),(2,3),(1,3)]
    Combination_Selected = random.sample(L2,1)[0]

    Img_Size = (100,140)

    if Combination_Selected == (1,2): # Elents in same column are same
        
        Tile_1 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'.png').convert_alpha(), Img_Size)
        Tile_1_Rect = Tile_1.get_rect(center = (Width//3,Height//3))

        Tile_2 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected_2+'.png').convert_alpha(), Img_Size)
        Tile_2_Rect = Tile_2.get_rect(center = (2*Width//3,Height//3))

        Tile_3 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected_2+'.png').convert_alpha(),Img_Size)
        Tile_3_Rect = Tile_3.get_rect(center = (2*Width//3,2*Height//3))

        Tile_4 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'.png').convert_alpha(),Img_Size)
        Tile_4_Rect = Tile_4.get_rect(center = (Width//3,2*Height//3))

    elif Combination_Selected == (2,3): # Elements in same row are same 
        
        Tile_1 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'.png').convert_alpha(),Img_Size)
        Tile_1_Rect = Tile_1.get_rect(center = (Width//3,Height//3))

        Tile_2 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'.png').convert_alpha(), Img_Size)
        Tile_2_Rect = Tile_2.get_rect(center = (2*Width//3,Height//3))

        Tile_3 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected_2+'.png').convert_alpha(), Img_Size)
        Tile_3_Rect = Tile_3.get_rect(center = (2*Width//3,2*Height//3))

        Tile_4 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected_2+'.png').convert_alpha(),Img_Size)
        Tile_4_Rect = Tile_4.get_rect(center = (Width//3,2*Height//3))

    elif Combination_Selected == (1,3): # Diagonal elements are same
        
        Tile_1 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'.png').convert_alpha(), Img_Size)
        Tile_1_Rect = Tile_1.get_rect(center = (Width//3,Height//3))

        Tile_2 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected_2+'.png').convert_alpha(), Img_Size)
        Tile_2_Rect = Tile_2.get_rect(center = (2*Width//3,Height//3))

        Tile_3 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'.png').convert_alpha(), Img_Size)
        Tile_3_Rect = Tile_3.get_rect(center = (2*Width//3,2*Height//3))

        Tile_4 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected_2+'.png').convert_alpha(), Img_Size)
        Tile_4_Rect = Tile_4.get_rect(center = (Width//3,2*Height//3))    

    Grey_Tile = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\White_Card.png').convert_alpha(), Img_Size)


    return Combination_Selected, Grey_Tile, Tile_1,Tile_1_Rect , Tile_2,Tile_2_Rect , Tile_3,Tile_3_Rect , Tile_4,Tile_4_Rect

def Flip_animation(screen, Grey_Tile, Tile , File_Selected, Tile_Rect, sec_Tile, sec_Tile_rect, sec_Tile_Match,sec_Tile_Click , tert_Tile, tert_Tile_rect , tert_Tile_Match, tert_Tile_Click,  quat_Tile, quat_Tile_rect  , quat_Tile_Match ,quat_Tile_Click , Dir , Bg):
    
    Img_Size = (100,140)
    File_Selected_w = 'White_Card'
    Delay = 12

    Frame_1 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\White_Card1.png').convert_alpha(), Img_Size)
    Frame_2 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\White_Card2.png').convert_alpha(), Img_Size)
    Frame_3 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\White_Card3.png').convert_alpha(), Img_Size)

    Frame_90_deg = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\90_Deg.png').convert_alpha(), Img_Size)

    Frame_4 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'1.png').convert_alpha(), Img_Size)
    Frame_5 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'2.png').convert_alpha(), Img_Size)
    Frame_6 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'3.png').convert_alpha(), Img_Size)

    Frame_7 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'4.png').convert_alpha(), Img_Size)
    Frame_8 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'5.png').convert_alpha(), Img_Size)
    Frame_9 = pygame.transform.scale(pygame.image.load(Path_addn + 'Assets\\'+File_Selected+'6.png').convert_alpha(), Img_Size)
    
    L_Positive = [Grey_Tile, Frame_1, Frame_2, Frame_3, Frame_90_deg, Frame_9, Frame_8, Frame_7 , Tile] 
    L_Negative = [Tile, Frame_4, Frame_5, Frame_6, pygame.transform.flip(Frame_3,True,False), pygame.transform.flip(Frame_2,True,False), pygame.transform.flip(Frame_1,True,False), Grey_Tile]
    
    def Anim(L):

        def Blit_Other_Tiles(Match,Click,Tile,Tile_rect):

            if Match or Click:
                screen.blit(Tile,Tile_rect)

            else:
                screen.blit(Grey_Tile,Tile_rect)

        for Surface in L:

            screen.blit(Bg,(0,0))

            Blit_Other_Tiles(sec_Tile_Match,sec_Tile_Click,sec_Tile,sec_Tile_rect)
            Blit_Other_Tiles(tert_Tile_Match,tert_Tile_Click,tert_Tile,tert_Tile_rect)
            Blit_Other_Tiles(quat_Tile_Match,quat_Tile_Click,quat_Tile,quat_Tile_rect)
            
            screen.blit(Surface, Tile_Rect)

            pygame.display.update()
            pygame.time.delay(Delay)
    
    if Dir == '+ve':
        Anim(L_Positive)

    elif Dir == '-ve':
        Anim(L_Negative)

def Mouse(screen,Bg,Grey_Tile,Tile_1,Tile_1_Rect,Width,Height,Tile_2,Tile_2_Rect, Tile_1_Num,Tile_2_Num,Tile_3_Num,Tile_4_Num, Tile_3,Tile_3_Rect, Tile_4,Tile_4_Rect, Click1, Click2, Click3, Click4, Tile_1_Match,Tile_2_Match,Tile_3_Match,Tile_4_Match):

    Mouse_Pos = pygame.mouse.get_pos()
    Click = pygame.mouse.get_pressed()[0]

    screen.blit(Bg,(0,0))

    def Fn(Tile , Tile_Num, Tile_Rect,Tile_Match,Tile_Click, sec_Tile, sec_Tile_rect, sec_Tile_Match,sec_Tile_Click , tert_Tile, tert_Tile_rect , tert_Tile_Match, tert_Tile_Click,  quat_Tile, quat_Tile_rect  , quat_Tile_Match ,quat_Tile_Click):
        
        if  Tile_Match == False:    

            if Tile_Rect.collidepoint(Mouse_Pos):
                if Click:
                    screen.blit(Tile, Tile_Rect)
                    Tile_Click = 1
                    #Flip_animation(screen, Grey_Tile, Tile_1, Tile_1_Num, Tile_1_Rect , Tile_2,Tile_2_Rect,Tile_2_Match,Click2, Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4 , '+ve', Bg)
                    Flip_animation(screen, Grey_Tile, Tile, Tile_Num, Tile_Rect, sec_Tile, sec_Tile_rect, sec_Tile_Match, sec_Tile_Click, tert_Tile, tert_Tile_rect, tert_Tile_Match, tert_Tile_Click, quat_Tile, quat_Tile_rect, quat_Tile_Match, quat_Tile_Click, '+ve', Bg)

                elif Tile_Click == 1:
                    screen.blit(Tile, Tile_Rect)
                
                else:
                    screen.blit(Grey_Tile, Tile_Rect)        

            elif Tile_Click == 1:
                screen.blit(Tile, Tile_Rect)

            else:
                screen.blit(Grey_Tile, Tile_Rect)

        elif Tile_Match == True:
            screen.blit(Tile, Tile_Rect)
            Tile_Click = 2

        return Tile_Click

    Click1 = Fn(Tile_1, Tile_1_Num, Tile_1_Rect, Tile_1_Match, Click1, Tile_2, Tile_2_Rect, Tile_2_Match, Click2, Tile_3, Tile_3_Rect,Tile_3_Match, Click3, Tile_4, Tile_4_Rect, Tile_4_Match, Click4 )
    Click2 = Fn(Tile_2, Tile_2_Num, Tile_2_Rect, Tile_2_Match, Click2, Tile_1, Tile_1_Rect, Tile_1_Match, Click1, Tile_3, Tile_3_Rect,Tile_3_Match, Click3, Tile_4, Tile_4_Rect, Tile_4_Match, Click4 )
    Click3 = Fn(Tile_3, Tile_3_Num, Tile_3_Rect, Tile_3_Match, Click3, Tile_2, Tile_2_Rect, Tile_2_Match, Click2, Tile_1, Tile_1_Rect,Tile_1_Match, Click1, Tile_4, Tile_4_Rect, Tile_4_Match, Click4 )
    Click4 = Fn(Tile_4, Tile_4_Num, Tile_4_Rect, Tile_4_Match, Click4, Tile_2, Tile_2_Rect, Tile_2_Match, Click2, Tile_3, Tile_3_Rect,Tile_3_Match, Click3, Tile_1, Tile_1_Rect, Tile_1_Match, Click1 )

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

    def Check(Tile , Tile_Num, Tile_rect, Tile_Match, Tile_Click , Tile2 , Tile2_Num, Tile2_rect, Tile2_Match, Tile2_Click , tert_Tile, tert_Tile_rect , tert_Tile_Match, tert_Tile_Click,  quat_Tile, quat_Tile_rect  , quat_Tile_Match ,quat_Tile_Click):

        if Tile_Click == Tile2_Click == 1:

            if Tile_Num == Tile2_Num:

                Tile_Match = True
                Tile2_Match = True
                Display_Emoji(screen)
                pygame.time.delay(500)
            
            else :
                screen.blit(Tile, Tile_rect)
                screen.blit(Tile2, Tile2_rect)
                pygame.display.update()

                pygame.time.delay(Delay)
                #Flip_animation(screen, Grey_Tile, Tile_1, Tile_1_Num, Tile_1_Rect , Tile_2,Tile_2_Rect,Tile_2_Match,Click2, Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_4, Tile_4_Rect,Tile_4_Match,Click4 , '-ve', Bg)
                Flip_animation(screen, Grey_Tile, Tile, Tile_Num, Tile_rect, Tile2, Tile2_rect, Tile2_Match, Tile2_Click, tert_Tile, tert_Tile_rect, tert_Tile_Match, tert_Tile_Click, quat_Tile, quat_Tile_rect, quat_Tile_Match, quat_Tile_Click, '-ve', Bg)
                Tile_Click = 0
                #Flip_animation(screen, Grey_Tile, Tile_4, Tile_4_Num, Tile_4_Rect , Tile_1,Tile_1_Rect,Tile_1_Match,Click1 , Tile_3,Tile_3_Rect,Tile_3_Match,Click3, Tile_2, Tile_2_Rect,Tile_2_Match,Click2, '-ve', Bg)
                Flip_animation(screen, Grey_Tile, Tile2, Tile2_Num, Tile2_rect, Tile, Tile_rect, Tile_Match, Tile_Click, tert_Tile, tert_Tile_rect, tert_Tile_Match, tert_Tile_Click, quat_Tile, quat_Tile_rect, quat_Tile_Match, quat_Tile_Click, '-ve', Bg)
                Tile2_Click = 0

        return Tile_Match,Tile2_Match,Tile_Click,Tile2_Click

    Tile_1_Match, Tile_2_Match, Click1, Click2 = Check(Tile_1, Tile_1_Num, Tile_1_Rect, Tile_1_Match, Click1, Tile_2, Tile_2_Num, Tile_2_Rect, Tile_2_Match, Click2, Tile_3, Tile_3_Rect, Tile_3_Match, Click3, Tile_4, Tile_4_Rect, Tile_4_Match, Click4)
    Tile_1_Match, Tile_3_Match, Click1, Click3 = Check(Tile_1, Tile_1_Num, Tile_1_Rect, Tile_1_Match, Click1, Tile_3, Tile_3_Num, Tile_3_Rect, Tile_3_Match, Click3, Tile_2, Tile_2_Rect, Tile_2_Match, Click2, Tile_4, Tile_4_Rect, Tile_4_Match, Click4)
    Tile_1_Match, Tile_4_Match, Click1, Click4 = Check(Tile_1, Tile_1_Num, Tile_1_Rect, Tile_1_Match, Click1, Tile_4, Tile_4_Num, Tile_4_Rect, Tile_4_Match, Click4, Tile_3, Tile_3_Rect, Tile_3_Match, Click3, Tile_2, Tile_2_Rect, Tile_2_Match, Click2)
    
    Tile_2_Match, Tile_3_Match, Click2, Click3 = Check(Tile_2, Tile_2_Num, Tile_2_Rect, Tile_2_Match, Click2, Tile_3, Tile_3_Num, Tile_3_Rect, Tile_3_Match, Click3, Tile_1, Tile_1_Rect, Tile_1_Match, Click1, Tile_4, Tile_4_Rect, Tile_4_Match, Click4)
    Tile_2_Match, Tile_4_Match, Click2, Click4 = Check(Tile_2, Tile_2_Num, Tile_2_Rect, Tile_2_Match, Click2, Tile_4, Tile_4_Num, Tile_4_Rect, Tile_4_Match, Click4, Tile_3, Tile_3_Rect, Tile_3_Match, Click3, Tile_1, Tile_1_Rect, Tile_1_Match, Click1)
    
    Tile_3_Match, Tile_4_Match, Click3, Click4 = Check(Tile_3, Tile_3_Num, Tile_3_Rect, Tile_3_Match, Click3, Tile_4, Tile_4_Num, Tile_4_Rect, Tile_4_Match, Click4, Tile_2, Tile_2_Rect, Tile_2_Match, Click2, Tile_1, Tile_1_Rect, Tile_1_Match, Click1)

    return Click1, Click2 ,Click3 ,Click4 , Tile_1_Match,Tile_2_Match,Tile_3_Match,Tile_4_Match

def Load_Screen(Width,Height): #Loading the window

    screen = pygame.display.set_mode((Width,Height))
    return screen

def Win(Tile_1_Match,Tile_2_Match,Tile_3_Match,Tile_4_Match, screen,Width,Height):

    if Tile_1_Match == Tile_2_Match == Tile_3_Match == Tile_4_Match == True:

        Win_Str_List = ['Nice Job!', 'Great Thinking!', 'Fantastic!']
        Win_Str = random.choice(Win_Str_List)
        Txt1 = Font2.render(Win_Str, 0, (255,255,255)).convert_alpha()
        Txt1_rect = Txt1.get_rect(center = (Width//2,Height//2))
        screen.blit(Txt1,Txt1_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        return 'Win +ve'

def main(L,Bg_img,screen):

    Width,Height,Bg= Background(screen,Bg_img,1280,720)

    Click1, Click2, Click3, Click4 = 0,0,0,0
    Click_1, Click_2, Click_3, Click_4 = 0,0,0,0

    Tile_1_Match , Tile_2_Match , Tile_3_Match , Tile_4_Match = False,False,False,False

    File_Selected, File_Selected_2 = Select_File(L) 
    Combination_Selected, Grey_Tile,Tile_1,Tile_1_Rect,Tile_2,Tile_2_Rect, Tile_3,Tile_3_Rect, Tile_4,Tile_4_Rect = Load_Images(Width, Height, screen,File_Selected,File_Selected_2)
    
    clock = pygame.time.Clock()

    Tile_1_Num, Tile_2_Num, Tile_3_Num, Tile_4_Num = Assign_Num(File_Selected, File_Selected_2, Combination_Selected)

    while True:

        for event in pygame.event.get(): # Handling user input
            
            if event.type == pygame.QUIT: # Handling User input to quit game

                pygame.quit()
                sys.exit() #Safely exits the code

            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mx,my = pygame.mouse.get_pos()
                if Back_Button_Rect.collidepoint(mx, my) == True:
                    exec(open('Games.py').read())

        Back_Button = Hover_color_change(Back_txt, Back_Button_Rect)

        Click1, Click2, Click3, Click4 = Mouse(screen, Bg, Grey_Tile, Tile_1, Tile_1_Rect, Width, Height, Tile_2, Tile_2_Rect, Tile_1_Num, Tile_2_Num, Tile_3_Num, Tile_4_Num, Tile_3, Tile_3_Rect, Tile_4, Tile_4_Rect, Click1, Click2, Click3, Click4, Tile_1_Match, Tile_2_Match, Tile_3_Match, Tile_4_Match)
        
        Click1, Click2 ,Click3 ,Click4 , Tile_1_Match,Tile_2_Match,Tile_3_Match,Tile_4_Match = Compare(Bg ,Grey_Tile, screen, Click1, Click2, Click3, Click4, Combination_Selected, Tile_1, Tile_2, Tile_3, Tile_4, Tile_1_Num, Tile_2_Num, Tile_3_Num, Tile_4_Num, Tile_1_Rect, Tile_2_Rect, Tile_3_Rect, Tile_4_Rect, Tile_1_Match, Tile_2_Match, Tile_3_Match, Tile_4_Match)
        
        Win_Check = Win(Tile_1_Match, Tile_2_Match, Tile_3_Match, Tile_4_Match,screen,Width,Height)

        screen.blit(Back_Button, Back_Button_Rect)

        pygame.display.update() # refreshes the contents of the screen

        clock.tick(100)

        if Win_Check == 'Win +ve':
            break

if __name__ == '__main__':

    Path_addn = ''
    
    screen = Load_Screen(1280,720)
    pygame.mixer.music.play(-1)
    main(['Cards 1\\Green_Card','Cards 1\\Red_Card'],'Bg',screen)
    pygame.quit()