import pygame
import random
pygame.init()


windowY = 600
rows, cols = 10,10
cubesize = int(windowY/rows)
windowX = windowY * 2 + cubesize

playerBoard =  [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]

AIBoard =  [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

# colors
black = (0,0,0)
green = (0,255,0)
# Set up the drawing window
screen = pygame.display.set_mode([windowX, windowY])

def drawBoards():
    #draws board 1 
    for i in range(0, int(windowX/2), cubesize):
        # print(i)
        pygame.draw.line(screen, black, (i,0),(i, windowX), width = 3)
        pygame.draw.line(screen, black, (0,i),(int(windowX/2 - cubesize/2), i), width = 3)

    #draws board 2
    for i in range (int(windowX/2 + cubesize/2), windowX, cubesize):
        pygame.draw.line(screen, black, (i,0),(i,windowX), width = 3)
    for i in range(0, windowY, cubesize):
        pygame.draw.line(screen, black, (int(windowX/2+cubesize/2),i),(windowX, i), width = 3)

    
# def generateShips(playerboard, AIBoard):
#     boats = 5
#     while boats > 0:
#         verthorz = random.randint(1,2)
#         if verthorz == 1:
#             leftRight = random.randint(1,2)
#             #right
#             if leftRight == 1:
#                 startpos = random.randint(4,6)
#                 for i in range(0,boats):
#                     playerboard[startpos][i]
#                     pygame.draw.rect(screen, green, (startpos*cubesize, startpos*cubesize, cubesize, cubesize))
                    
#             #left
#             if leftRight == 2:
#                 pass
#         if verthorz == 2:
#             updown = random.randint(1,2)
#             if updown == 1:
#                 pass
#             if updown == 2:
#                 pass
        
#         boats -= 1

def 

def updateFrame():
    screen.fill((255, 255, 255))
    drawBoards()
    generateShips(playerBoard, AIBoard)
    

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updateFrame()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()