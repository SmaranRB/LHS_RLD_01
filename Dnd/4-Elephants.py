
import Dnd.Dnd_3 as DND3

screen = pygame.display.set_mode((1280,720))
bg = pygame.image.load('.\Dnd\Resources\elebg.jpg')

# image 1
im1 = ".\Dnd\Resources\Ele1.png"  # OBJECT 
xy1 = (900,175) # BASE CO-ORDS
im2 = ".\Dnd\Resources\Ele2.png"  # IMAGE
xy2 = (285,360) # TARGET CO-ORDS

# image 2
im3 = ".\Dnd\Resources\Ele3.png"  # OBJECT
xy3 = (900,380) # BASE CO-ORDS
im4 = ".\Dnd\Resources\Ele4.png"  # IMAGE
xy4 = (260,510) # TARGET CO-ORDS

# image 3
im5 = ".\Dnd\Resources\Ele5.png"  # OBJECT
xy5 = (900,550) # BASE CO-ORDS
im6 = ".\Dnd\Resources\Ele6.png"  # IMAGE
xy6 = (235,100) # TARGET CO-ORDS

DND3.DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4,im5,xy5,im6,xy6)
