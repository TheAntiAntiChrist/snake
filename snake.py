import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode([600,600])
pygame.display.set_caption("Snake")

#snakeIcon = pygame.image.load("snake.png") #Code only useful if snake.png is present
#pygame.display.set_icon(snakeIcon)

Done = False
clock = pygame.time.Clock()

snk = [[300,300]]
snkDir = 0 # 0 is north, 1 is east, 2 is south, 3 is west
counter = 0
length = 1
isEaten = True

def OOB():
    if snk[-1][0] < 0:
        snk[-1][0] = 600
    elif snk[-1][0] > 600:
        snk[-1][0] = 0
    if snk[-1][1] < 0:
        snk[-1][1] = 600
    elif snk[-1][1] > 600:
        snk[-1][1] = 0

while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Done = True
            if event.key == pygame.K_UP and snkDir != 2:
                snkDir = 0
            elif event.key == pygame.K_DOWN and snkDir != 0:
                snkDir = 2
            if event.key == pygame.K_RIGHT and snkDir != 3:
                snkDir = 1
            elif event.key == pygame.K_LEFT and snkDir != 1:
                snkDir = 3

    screen.fill([50,50,50])

    if isEaten:
        ticTac = [randint(5, 55)*10, randint(5, 55)*10]
        isEaten = False
    pygame.draw.rect(screen,[150,150,150],[ticTac[0],ticTac[1],10,10],0)
    pygame.draw.rect(screen,[255,255,255],[ticTac[0]+2,ticTac[1]+2,6,6],0)

    OOB()
    if snkDir == 0:
        snk.append([snk[-1][0],snk[-1][1]-10])
    if snkDir == 1:
        snk.append([snk[-1][0]+10,snk[-1][1]]) #0+10
    if snkDir == 2:
        snk.append([snk[-1][0],snk[-1][1]+10]) #1+10
    if snkDir == 3:
        snk.append([snk[-1][0]-10,snk[-1][1]]) #0-10
    if snk[-1] == ticTac:
        length += 1
        isEaten = True
    if len(snk) > length:
        snk.pop(0)
    for segment in snk:
        pygame.draw.rect(screen,[100,200,200],[segment[0],segment[1],10,10],0)
        pygame.draw.rect(screen,[150,255,255],[segment[0]+2,segment[1]+2,6,6],0)
        if snk[-1] == segment and segment is not snk[-1]: #snk[-1] == segment checks value, segment is not snk[-1] shows that the current segment isn't the actual snk[-1]
            print("""
            You Died...
            """)
            print("""
            You Scored: """, length, """ points.
            """)
            Done = True

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
