
import Dnd.Dnd_3 as DND3

screen = pygame.display.set_mode((1280,720))
bg = pygame.image.load('.\Dnd\Resources\eboard.jpg')

# image 1
im1 = ".\Dnd\Resources\Crcl1.png"  # OBJECT 
xy1 = (800,350) # BASE CO-ORDS
im2 = ".\Dnd\Resources\Crcl2.png"  # IMAGE
xy2 = (300,100) # TARGET CO-ORDS

# image 2
im3 = ".\Dnd\Resources\Tr1.png"  # OBJECT
xy3 = (800,550) # BASE CO-ORDS
im4 = ".\Dnd\Resources\Tr2.png"  # IMAGE
xy4 = (300,300) # TARGET CO-ORDS

# image 3
im5 = ".\Dnd\Resources\Sq1.jpg"  # OBJECT
xy5 = (800,150) # BASE CO-ORDS
im6 = ".\Dnd\Resources\Sq2.jpg"  # IMAGE
xy6 = (300,500) # TARGET CO-ORDS

DND3.DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4,im5,xy5,im6,xy6)
