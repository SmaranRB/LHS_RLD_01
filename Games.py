from Program_init import *

#Header
Header_Button = Font.render('Autism iLearner', True, (255,255,255))
Header_Button_Rect = Header_Button.get_rect(center = (width//2,height//8)) 

#Drag and Drop
Dnd_txt = 'Drag and Drop'
Dnd_Button = Font2.render('Drag and Drop', True, White)
Dnd_Button_Rect = Dnd_Button.get_rect(center = (width//2,4*height//10))

#Maze
Maze_txt = 'Maze'
Maze_Button = Font2.render("Maze", True, White)
Maze_Button_Rect = Maze_Button.get_rect(center = (width//2,5*height//10))

#Memory Game
Memory_cards_txt = 'Memory Cards'
Memory_cards_Button = Font2.render('Memory Cards', True, White)
Memory_cards_Button_Rect = Memory_cards_Button.get_rect(center = (width//2,6*height//10))

#Obstacle Course
Ob_course_txt = 'Obstacle Course'
Ob_course_Button = Font2.render('Obstacle Course', True, White)
Ob_course_Button_Rect = Ob_course_Button.get_rect(center = (width//2,7*height//10))

#Progress Report
Progress_Image =  pygame.transform.scale(pygame.image.load('FrontPage\\Progress Report Icon.png').convert_alpha(),(60,60))
Progress_txt = 'Bar'
Progress_Button = Font2.render(Progress_txt, True, White)
Progress_Button_Rect = Progress_Button.get_rect(center = (4.15*width//5,19*height//20))

#Demo
Demo_txt = 'Demo'
Demo_Button = Font2.render(Demo_txt, True, White)
Demo_Button_Rect = Demo_Button.get_rect(center = (width//2,19*height//20))

#Quit
Quit_txt = 'Quit'
Quit_Button = Font2.render(Quit_txt, True, Red)
Quit_Button_Rect = Quit_Button.get_rect(center = (width//5,19*height//20))

#MainLoop

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

fade(width, height,bg)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()

            #Mouseclicks and buttons
            if Dnd_Button_Rect.collidepoint(mx, my) == True:
                exec(open('Dnd_main.py').read())

            elif Maze_Button_Rect.collidepoint(mx, my) == True:
                exec(open('Maze.py').read())
            
            elif Memory_cards_Button_Rect.collidepoint(mx, my) == True:
                exec(open('Memory_Cards.py').read())
            
            elif Ob_course_Button_Rect.collidepoint(mx, my) == True:
                pygame.mixer.music.set_volume(0.3)
                exec(open('ObstacleCourse.py').read())
                pygame.mixer.music.set_volume(1)
            
            elif Progress_Button_Rect.collidepoint(mx, my) == True:
                exec(open('Progress_Report.py').read())
            
            elif Demo_Button_Rect.collidepoint(mx,my):
                w.open('https://www.youtube.com/watch?v=x5Udg77RMeY')
            
            elif Quit_Button_Rect.collidepoint(mx, my) == True:
                pygame.quit()
                sys.exit()

    Dnd_Button = Hover_color_change(Dnd_txt, Dnd_Button_Rect)
    Maze_Button = Hover_color_change(Maze_txt, Maze_Button_Rect)
    Memory_cards_Button = Hover_color_change(Memory_cards_txt, Memory_cards_Button_Rect)
    Ob_course_Button = Hover_color_change(Ob_course_txt, Ob_course_Button_Rect)
    Demo_Button = Hover_color_change(Demo_txt, Demo_Button_Rect)
    Quit_Button = Hover_color_change(Quit_txt, Quit_Button_Rect, Red)
    
    #Displaying text
    screen.blit(bg_image,(0,0))
    screen.blit(Header_Button, Header_Button_Rect)
    screen.blit(Dnd_Button, Dnd_Button_Rect)
    screen.blit(Maze_Button, Maze_Button_Rect)
    screen.blit(Memory_cards_Button, Memory_cards_Button_Rect)
    screen.blit(Ob_course_Button, Ob_course_Button_Rect)
    screen.blit(Progress_Image, Progress_Button_Rect)
    screen.blit(Demo_Button, Demo_Button_Rect)
    screen.blit(Quit_Button, Quit_Button_Rect)
    pygame.display.update()