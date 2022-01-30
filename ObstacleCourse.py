def OBC():
    import pygame
    import random
    import time
    import sys
    import Memory_cards.MySQL_connector as MySQL

    StartTime  = time.time()

    #Iniitialisation-------------------------------------------------------------
    width, height = 1280,720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # #audio
    # audio = pygame.mixer.music.load(r'Obstacle_Course_Assets\Sound1.mp3')
    # pygame.mixer.music.play(-1)

    #background---------------------------------------------------------------------
    bg = pygame.image.load('Obstacle_Course_Assets\\Bg Image 1.png').convert_alpha()
    bg_img = pygame.transform.scale(bg, (width, height))
    bg_x = 0

    def bg_animation():
        nonlocal bg_x         
        screen.fill((0,0,0))            #Clear Screen
        screen.blit(bg_img, (bg_x,0))   
        screen.blit(bg_img, (bg_x+width,0))
        bg_x -= 3
        if bg_x <= -width:              #If the leftbg rouches the border, set bg to initial position
            bg_x = 0
        
    #Sprite-------------------------------------------------------------------------
    xsize,ysize = 104,127
    x_pos, y_pos = width/10,550
    sprite_list = [
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__000.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__001.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__002.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__003.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__004.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__005.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__006.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__007.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__008.png").convert_alpha(),
        pygame.image.load(r"Obstacle_Course_Assets\Sprite animations\Run__009.png").convert_alpha()
    ]
    Jumpsprite = pygame.image.load(r'Obstacle_Course_Assets\Sprite animations\Jump__005.png').convert_alpha()
    sprite_yspeed =0
    sprite_count = 0

    def sprite_y_movements():
        nonlocal sprite_yspeed
        sprite_yacceleration = 0.2
        sprite_yspeed += sprite_yacceleration
        sprite_rect.centery += sprite_yspeed
        if sprite_rect.centery >= 550:         #To prevent sprite from going further down
            sprite_yspeed = 0
            sprite_rect.centery = 550
        y_pos = sprite_rect.centery 

    #ScreenBoundary Collisions-----------------------------------------------------
    def window_collision():
        nonlocal sprite_yspeed
        if sprite_rect.centery <= 0:
            sprite_yspeed = 1

    #Obstacles--------------------------------------------------------------------------
    block = pygame.image.load(r'Obstacle_Course_Assets\barrier.png')
    block = pygame.transform.scale(block, (75,200))
    block_list = []
    load_new_pipe = pygame.USEREVENT
    pygame.time.set_timer(load_new_pipe, 1500)      #A timer to add new blocks

    def random_block():
        block_y = random.randrange(0,550)
        block_rect = block.get_rect(center = (width+10,block_y))
        return block_rect

    def draw_block():
        for i in block_list:
            screen.blit(block, i)
            i.centerx -= 3

    #Collision with obstacle and game over----------------------------------------
    Oops = pygame.image.load(r'Obstacle_Course_Assets\EmojiOops.png').convert_alpha()
    def collsion_sprite_block():
        nonlocal run
        nonlocal EndTime
        for i in block_list:
            if sprite_rect.colliderect(i):
                #screen.fill((255,255,255))
                EndTime = time.time()
                screen.blit(Oops, (0,0))
                Oops_audio = pygame.mixer.Sound(r'Obstacle_Course_Assets\Oops.mp3')
                Oops_audio.play()
                pygame.display.update()
                Game = 'obc'
                MySQL.push_data(Game, round(EndTime - StartTime,3))
                clock.tick(0.3)
                run = False
                
    #Mainloop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EndTime = time.time()
                run = False
                sys.exit()

            if event.type == pygame.KEYDOWN:        #for Jump
                if event.key == pygame.K_SPACE:
                    sprite_yspeed = -10
                    jumpsound = pygame.mixer.Sound(r'Obstacle_Course_Assets/Jump.mp3')
                    jumpsound.play()

            if event.type == load_new_pipe:         #add the rects after a specific time
                block_list.append(random_block())
        
        bg_animation()

        #Animation - Sprite-------
        sprite = pygame.transform.scale(sprite_list[int(sprite_count)], (xsize,ysize))
        sprite_rect = sprite.get_rect(center = (x_pos,y_pos))
        sprite_count+=0.25
        if sprite_count == len(sprite_list):
            sprite_count = 0
        
        if sprite_rect.centery < 550:
            sprite = pygame.transform.scale(Jumpsprite, (xsize,ysize))
            #clock.tick(140)

        screen.blit(sprite, sprite_rect)
        sprite_y_movements()
        window_collision()
        draw_block()
        collsion_sprite_block()
        y_pos = sprite_rect.centery
        pygame.display.update()
        clock.tick(120)

OBC()