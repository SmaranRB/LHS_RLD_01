# ----- SQL Data retrieval -----

def main():
   import mysql.connector as m
   import pygame
   import sys
   import Program_init as Init

   width = 1280
   height = 720

   Server = m.connect( host='localhost', user='root', passwd=Init.passwd, db='autism')
   cs = Server.cursor()
   game = "select t_time from user1 where game = '%s' order by date desc limit 5"

   '''_dnd = cs.execute(game%'dnd')
   dnd = cs.fetchall()
   _mmc = cs.execute(game%'mmc')
   mmc = cs.fetchall()
   _maz = cs.execute(game%'maz')
   maz = cs.fetchall()'''

   #print(dnd,mmc,maz)

   def vals(Name, Str):
      com = cs.execute(game%Name)
      List = cs.fetchall()
      #print(List)
      out = "Previous 5 timings of {}\n".format(Str)
      try:
         for i in range(5):
            out += "\n{} seconds".format(List[i][0])
      except:
         out += "\nNo data available."
      return out

   '''print(vals('dnd','Drag and Drop Game :'))
   print(vals('mmc','Memory Cards Game :'))
   print(vals('maz','Maze game :'))'''

   # ----- Python window -----

   pygame.init()
   run = True

   while run:

      mx, my = pygame.mouse.get_pos() #  MOUSE co-ordinates   
      screen = pygame.display.set_mode((1280,720))
      screen.blit(pygame.transform.scale(pygame.image.load('FrontPage\\5.png').convert_alpha(),(1280, 720)),(0,0))

      Font_Head = pygame.font.Font('Memory_cards\\Fonts\\Quicksand\\Quicksand-Bold.otf',70)
      screen.blit(Font_Head.render("Progress Report", 1, Init.Green) , (Font_Head.render("Progress Report", 1, Init.White).get_rect(center = (width//2,height//8))))

      out1_ = vals('dnd','Drag and Drop Game :')
      out1 = out1_.split('\n')
      for i in range(0, len(out1)*20, 20):
         screen.blit( Init.Font4.render(out1[i//20], 1, Init.White) , (width//6, 200 + i) )

      out2_ = vals('mmc','Memory Cards Game :')
      out2 = out2_.split('\n')
      for i in range(0, len(out2)*20, 20):
         screen.blit(  Init.Font4.render( out2[i//20], 1, Init.White) , (7*width//13, 200 + i) )

      out3_ = vals('maz','Maze Game :')
      out3 = out3_.split('\n')
      for i in range(0, len(out3)*20, 20):
         screen.blit( Init.Font4.render( out3[i//20], 1, Init.White) , (width//6, 3*height//5 + i) )

      out4_ = vals('obc','Obstacle Course :')
      out4 = out4_.split('\n')
      for i in range(0, len(out4)*20, 20):
         screen.blit( Init.Font4.render( out4[i//20], 1, Init.White) , (7*width//13, 3*height//5 + i) )
      
      Back_Button = Init.Hover_color_change(Init.Back_txt, Init.Back_Button_Rect)
      screen.blit(Back_Button, Init.Back_Button_Rect)

      pygame.display.update()

      for event in pygame.event.get():

         if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

         elif event.type == pygame.MOUSEBUTTONDOWN:
            if Init.Back_Button_Rect.collidepoint(mx,my):
               exec(open('Games.py').read())

main()