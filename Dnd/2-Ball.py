
from Dnd.Dnd_2 import *

screen = pygame.display.set_mode((1280,720))
bg = pygame.image.load('.\Dnd\Resources\ground.jpg')

# image 1
im1 = ".\Dnd\Resources\Ball1.png"  # OBJECT 
xy1 = (800,240) # BASE CO-ORDS
im2 = ".\Dnd\Resources\Ball2.png"  # IMAGE
xy2 = (300,450) # TARGET CO-ORDS

# image 2
im3 = ".\Dnd\Resources\Ball3.png"  # OBJECT
xy3 = (800,470) # BASE CO-ORDS
im4 = ".\Dnd\Resources\Ball4.png"  # IMAGE
xy4 = (270,150) # TARGET CO-ORDS

DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4)
