
from Dnd.Dnd_2 import *

screen = pygame.display.set_mode((1280,720))
bg = pygame.image.load('.\Dnd\Resources\ocean.jpg')

# image 1
im1 = ".\Dnd\Resources\Fish1.png"  # OBJECT 
xy1 = (800,400) # BASE CO-ORDS
im2 = ".\Dnd\Resources\Fish2.png"  # IMAGE
xy2 = (200,70) # TARGET CO-ORDS

# image 2
im3 = ".\Dnd\Resources\Fish3.png"  # OBJECT
xy3 = (800,140) # BASE CO-ORDS
im4 = ".\Dnd\Resources\Fish4.png"  # IMAGE
xy4 = (200,330) # TARGET CO-ORDS

DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4)

