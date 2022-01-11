import pygame

screen = pygame.display.set_mode((1280,720))

def Fish():
    import Dnd.Dnd_2 as L1
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

    L1.DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4)

def Ball():
    import Dnd.Dnd_2 as L1
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

    L1.DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4)

def Book():
    import Dnd.Dnd_2 as L1
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

    L1.DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4)

def Elephants():
    import Dnd.Dnd_3 as L2
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

    L2.DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4,im5,xy5,im6,xy6)

def Shapes():
    import Dnd.Dnd_3 as L2
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

    L2.DND(screen,bg,im1,xy1,im2,xy2,im3,xy3,im4,xy4,im5,xy5,im6,xy6)

if __name__ == '__main__':
    Fish()
    Ball()
    Book()
    Elepahants()
    Shapes()