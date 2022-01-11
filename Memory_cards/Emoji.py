import pygame
import random
import sys

Path_addn = 'Memory_cards\\'

def Display_Emoji(screen):

    Width = 1280
    Height = 720

    L = ['Smile1','Smile2','Smile3','Star_Struck']
    E = random.choice(L)

    Img_Size = (200,200)

    Img = pygame.transform.scale(pygame.image.load(Path_addn+'Assets\\Emojis\\'+E+'.png').convert_alpha(), Img_Size)

    Img_Pos1 = (Width-150,Height-120)
    Img_Pos2 = (70,70)

    Img_Rect = Img.get_rect(center = Img_Pos1)

    screen.blit(Img,Img_Rect)
    pygame.display.update()

if __name__ == '__main__':

    screen = pygame.display.set_mode((1280,720))

    while True:

        for event in pygame.event.get(): # Handling user input
            
            if event.type == pygame.QUIT: # Handling User input to quit game
                pygame.quit()
                sys.exit() #Safely exits the code

        pygame.time.Clock().tick(1000)
        Display_Emoji(screen)