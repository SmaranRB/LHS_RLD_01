from Program_init import *

#Header
Header_Button = Font.render('<Name of app>', True, (255,255,255))
Header_Button_Rect = Header_Button.get_rect(center = (width//2,height//10)) 

#Drag and Drop
Games_txt = 'Games'
Games_Button = Font2.render(Games_txt, True, White)
Games_Button_Rect = Games_Button.get_rect(center = (width//2,5*height//10))

#Maze
Settings_txt = 'Progress Report'
Settings_Button = Font2.render(Settings_txt, True, White)
Settings_Button_Rect = Settings_Button.get_rect(center = (width//2,6*height//10))

#Music
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

#Mainloop

fade(width, height,bg)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()

            #Mouseclicks and buttons
            if Games_Button_Rect.collidepoint(mx, my) == True:
                exec(open('Games.py').read())
            elif Settings_Button_Rect.collidepoint(mx, my) == True:
                exec(open('Progress_Report.py').read())
    '''
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    bg_image = pygame.transform.scale(pygame.image.load('FrontPage\\'+bg).convert_alpha(),(width, height))
    '''
    Games_Button = Hover_color_change(Games_txt, Games_Button_Rect)
    Settings_Button = Hover_color_change(Settings_txt, Settings_Button_Rect)
    
    #Displaying text
    screen.blit(bg_image,(0,0))
    screen.blit(Header_Button, Header_Button_Rect)
    screen.blit(Games_Button, Games_Button_Rect)
    screen.blit(Settings_Button, Settings_Button_Rect)
    pygame.display.update()