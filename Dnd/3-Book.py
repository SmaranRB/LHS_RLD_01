
from Dnd.Dnd_2 import *

screen = pygame.display.set_mode((1280,720))
bg = pygame.image.load('.\Dnd\Resources\class.jpg')

# image 1
im1 = ".\Dnd\Resources\Book1.png"  # OBJECT 
xy1 = (870,175) # BASE CO-ORDS
im2 = ".\Dnd\Resources\Book2.png"  # IMAGE
xy2 = (400,100) # TARGET CO-ORDS

# image 2
im3 = ".\Dnd\Resources\Book3.png"  # OBJECT
xy3 = (870,375) # BASE CO-ORDS
im4 = ".\Dnd\Resources\Book4.png"  # IMAGE
xy4 = (400,300) # TARGET CO-ORDS

DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4)
