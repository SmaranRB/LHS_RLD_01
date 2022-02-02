def Maze():

	import pygame
	import random
	import time
	import sys
	import Memory_cards.MySQL_connector as MySQL

	#Initialising the screen-------------------------------
	width, height = 1280,720
	screen = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()
	GameTimeList = []

	#reactions---------------------------------------------------
	GoodJob = pygame.image.load('Maze_Assets\\GoodJob.png')
	#GoodJob = pygame.transform.scale(GoodJob,(width, height))
	Font = pygame.font.SysFont('Kristen ITC', 80)
	
	BB = Font.render("<-", True, (255,255,255))
	BBR = BB.get_rect(center = (1280-60,40))
	
	#for level in range(40,45):
	pygame.init()
	StarTime = time.time()
	#Initialising the sprite
	sprite_size = width//30
	sprite_img = pygame.image.load('Maze_Assets\\sprite.jpg')
	sprite_img = pygame.transform.scale(sprite_img,(sprite_size, sprite_size))

	sprite_rect = sprite_img.get_rect(topleft = (0,0))
	sprite_rect_finalpt = sprite_img.get_rect(bottomright = (width,height))

	level = 40

	for level in range(40,45):
		pygame.init()
		StarTime = time.time()

		#Initialising the sprite
		sprite_size = width//30
		sprite_img = pygame.image.load('Maze_Assets\\sprite.jpg')
		sprite_img = pygame.transform.scale(sprite_img,(sprite_size, sprite_size))
		sprite_rect = sprite_img.get_rect(topleft = (0,0))
		sprite_rect_finalpt = sprite_img.get_rect(bottomright = (width,height))

		def draw_sprite():
			screen.blit(sprite_img,sprite_rect)
			screen.blit(sprite_img,sprite_rect_finalpt)

		#Initialising the blocks
		block_size = sprite_size
		x,y = block_size, block_size
		block_img = pygame.image.load('Maze_Assets\\Blocks.jpg')
		block_img = pygame.transform.scale(block_img,(block_size,block_size))
		list_of_rects = []

		def blocks(lst):
			global block_rect
			for coordinates in lst:
				block_rect = block_img.get_rect(center = coordinates)
				screen.blit(block_img, block_rect)
				list_of_rects.append(block_rect)

		def random_block_generator():
			random_list = []
			for i in range(level):
				x = list(range(100,width-100, block_size+10))
				y = list(range(0,height,block_size))
				x,y  = random.choice(x), random.choice(y)
				random_list.append((x, y))
			return random_list

		l = random_block_generator()
		run = True
		click = False
		while run:
			mx,my = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:		#To Quit pygame completely
					EndTime = time.time()
					run = False
					sys.exit()
					
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						if sprite_rect.collidepoint((mx,my)) == True:
							click = True

				elif event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						click = False
					if BBR.collidepoint(mx,my):
						exec(open('Games.py').read())
						run=False
						break

				elif event.type == pygame.MOUSEMOTION:
					if click:
						sprite_rect.centerx = mx
						sprite_rect.centery = my

				#Initial point and final point collision check
				if sprite_rect.colliderect(sprite_rect_finalpt):
					yay = pygame.mixer.Sound('Maze_Assets\\YAY!.mp3')
					yay.play()
					run = False
					screen.blit(GoodJob,(0,0))
					pygame.display.update()
					EndTime = time.time()
					GameTime = round(EndTime - StarTime,3)
					GameTimeList.append(GameTime)
					clock.tick(0.3)
					pygame.mouse.set_pos([0,0])


				#Collision with the yellow blocks
				for i in list_of_rects:
					if sprite_rect.colliderect(i) == True:
						sprite_rect.topleft = (0,0)
						click = False


			#Mouse-Inactive outside the window
			if mx==0 or my == 0 or mx>width or my>height:
				click = False
					

			screen.fill((0,0,0))			
			draw_sprite()
			blocks(l)
			screen.blit(BB, BBR)

			pygame.display.update()
			clock.tick(240)
	#pygame.quit()

	game = 'maz'
	t_time = sum(GameTimeList)
	MySQL.push_data(game, t_time)

Maze()