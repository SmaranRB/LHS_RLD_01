import pygame
import sys
pygame.init()


# ----- Images ----- #

def image(screen,img,x,y,w,h):
   screen.blit(img, (x-w//2, y-h//2))

def image2(screen,img,xxx,yyy):
   screen.blit(img, (xxx, yyy))


# ----- Moving Algorithm ----- #

def move(screen,bg, img,w,h,x,y,xx,yy,n,img_,x_,y_,w_,h_ , cl):

   img2,x12,y12,img4,x22,y22 = n
   click1, click2 = cl
   click1 = click2 = False
   
   xd = xx - x  # X - DISTANCE
   yd = yy - y  # Y - DISTANCE
   xs=1         # SIGN OF XD
   ys=1         # SIGN OF YD

   while (xs!=0) and (ys!=0):
      xd = xx - x
      yd = yy - y

      screen.fill((0,0,0))
      screen.blit(bg,(0,0))
      
      image2(screen,img2,x12,y12)
      image2(screen,img4,x22,y22)
      image(screen,img,x,y,w,h) # primary object
      image(screen,img_,x_,y_,w_,h_)

      x+=xd*0.05
      y+=yd*0.05

      pygame.display.update()

      if xd<0:
         xs = -xd//1
      else:
         xs = xd//1
      if yd<0:
         ys = -yd//1
      else:
         ys = yd//1


# ----- Main ----- #

def DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4):


   # ----- values ----- #
   
   x11,y11 = xy1
   x12,y12 = xy2
   x21,y21 = xy3
   x22,y22 = xy4

   xb11,yb11 = xy1
   xb21,yb21 = xy3

   img1 = pygame.image.load(im1)
   img2 = pygame.image.load(im2)
   img3 = pygame.image.load(im3)
   img4 = pygame.image.load(im4)

   w11,h11 = img1.get_width(),img1.get_height()
   w12,h12 = img2.get_width(),img2.get_height()
   w21,h21 = img3.get_width(),img3.get_height()
   w22,h22 = img4.get_width(),img4.get_height()

   n = img2,x12,y12,img4,x22,y22 # ref for move()
   
   run = True
   click1 = False
   click2 = False
   click = (click1,click2)


   while run:
      
      count = 0
      pygame.time.Clock().tick(60)
      
      for event in pygame.event.get():


         # ----- INITIALISING ----- #
         
         screen.fill((0,0,0))
         screen.blit(bg,(0,0))
         #image12
         image2(screen,img2,x12,y12)
         #image22
         image2(screen,img4,x22,y22)

         Font = pygame.font.SysFont('Kristen ITC', 80)
         BB = Font.render("<-", True, (255,255,255))
         BBR = BB.get_rect(center = (60,40))
         screen.blit(BB, BBR)         
         
         mx, my = pygame.mouse.get_pos() #  MOUSE co-ordinates


         # ----- WINDOW QUIT ----- #

         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

      
         # ----- CLICK ----- #

         elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
               if (x11 - w11//2 <= mx <= x11 + w11//2) and (y11 - h11//2 <= my <= y11 + h11//2): # Click ON image
                  click1 = True
               if (x21 - w21//2 <= mx <= x21 + w21//2) and (y21 - h21//2 <= my <= y21 + h21//2): # Click ON image
                  click2 = True
               if BBR.collidepoint(mx,my):
                  exec(open('Games.py').read())
                  run=False
                  break


         # ----- NOT CLLICK ----- #

         elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
               click1 = False
               click2 = False


            # 1               

            if (x12 <= x11 <= x12 + w12) and (y12 <= y11 <= y12 + h12): # If image is in hitbox
               move (screen,bg , img1,w11,h11, x11//1 , y11//1 , x12 + w12//2 , y12 + h12//2 , n , img3,x21,y21,w21,h21 , click)
               x11 = x12 + w12/2
               y11 = y12 + h12/2

               count += 1 # PROGRESS UPDATE

            elif (x11//1 , y11//1) != (xb11//1 , yb11//1): # Returning back to original position
               move(screen,bg  , img1,w11,h11, x11//1 , y11//1 , xb11 , yb11 , n , img3,x21,y21,w21,h21 , click)
               x11 = xb11
               y11 = yb11

               count -= 1 # REGRESS UPDATE


            # 2

            if (x22 <= x21 <= x22 + w22) and (y22 <= y21 <= y22 + h22): # If image is in hitbox
               move (screen,bg  , img3,w21,h21, x21//1 , y21//1 , x22 + w22//2 , y22 + h22//2 , n , img1,x11,y11,w11,h11 , click)
               x21 = x22 + w22/2
               y21 = y22 + h22/2

               count += 1 # PROGRESS UPDATE

            elif (x21//1 , y21//1) != (xb21//1 , yb21//1): # Returning back to original position
               move(screen,bg  , img3,w21,h21, x21//1 , y21//1 , xb21 , yb21 , n , img1,x11,y11,w11,h11 , click)
               x21 = xb21
               y21 = yb21

               count -= 1 # REGRESS UPDATE


         # ----- dragging ----- #
         elif event.type == pygame.MOUSEMOTION:

            if click1:
               x11=mx
               y11=my
            if click2:
               x21=mx
               y21=my


         # ----- INITIALIZATION 2 ----- #

         #image11
         image(screen,img1,x11,y11,w11,h11)
         #image21
         image(screen,img3,x21,y21,w21,h21)
         
         pygame.display.update()


         # ----- GOAL CHECK ----- #

         if count == 2:
            
            fimg = pygame.transform.scale(pygame.image.load('.\Dnd\Resources\smiley.png').convert_alpha(), (100,100))
            screen.blit(fimg, (590,310))
            pygame.display.update()
            pygame.time.delay(2000)

            run = False

         else:
            continue
            print(count)
