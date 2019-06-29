import pygame
from random import randint

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen = pygame.display.set_mode([600,600])
pygame.display.set_caption("Snake")

#snakeIcon = pygame.image.load("snake.png") #Code only useful if snake.png is present
#pygame.display.set_icon(snakeIcon)

#pointSound = pygame.mixer.Sound("ticTac.ogg") #Code only useful if ticTac.ogg is present

Done = False
clock = pygame.time.Clock()

snk = [[300,300]]
snkDir = 0 # 0 is north, 1 is east, 2 is south, 3 is west
counter = 0
length = 1
isEaten = True
alreadyPressed = False

def OOB():
    if snk[-1][0] < 0:
        return True
    elif snk[-1][0] >= 600:
        return True
    if snk[-1][1] < 0:
        return True
    elif snk[-1][1] >= 600:
        return True

while not Done:
    alreadyPressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Done = True
            if event.key == pygame.K_UP and snkDir != 2 and alreadyPressed == False:
                snkDir = 0
                alreadyPressed = True
            if event.key == pygame.K_DOWN and snkDir != 0 and alreadyPressed == False:
                snkDir = 2
                alreadyPressed = True
            if event.key == pygame.K_RIGHT and snkDir != 3 and alreadyPressed == False:
                snkDir = 1
                alreadyPressed = True
            if event.key == pygame.K_LEFT and snkDir != 1 and alreadyPressed == False:
                snkDir = 3
                alreadyPressed = True

    screen.fill([50,50,50])

    if isEaten:
        ticTac = [randint(5, 55)*10, randint(5, 55)*10]
        isEaten = False
    pygame.draw.rect(screen,[150,150,150],[ticTac[0],ticTac[1],10,10],0)
    pygame.draw.rect(screen,[255,255,255],[ticTac[0]+2,ticTac[1]+2,6,6],0)

    if snkDir == 0:
        snk.append([snk[-1][0],snk[-1][1]-10])
    elif snkDir == 1:
        snk.append([snk[-1][0]+10,snk[-1][1]]) #0+10
    elif snkDir == 2:
        snk.append([snk[-1][0],snk[-1][1]+10]) #1+10
    elif snkDir == 3:
        snk.append([snk[-1][0]-10,snk[-1][1]]) #0-10
    if snk[-1] == ticTac:
        length += 1
        #pointSound.play() #Code only useful if ticTac.ogg is present
        isEaten = True
    if len(snk) > length:
        snk.pop(0)
    if OOB():
        print("""
        You Died...
        """)
        print("""
        You Scored: """, length-1, """ points.
        """)
        Done = True
    for segment in snk:
        pygame.draw.rect(screen,[100,200,200],[segment[0],segment[1],10,10],0)
        pygame.draw.rect(screen,[150,255,255],[segment[0]+2,segment[1]+2,6,6],0)
        if snk[-1] == segment and segment is not snk[-1]: #snk[-1] == segment checks value, segment is not snk[-1] shows that the current segment isn't the actual snk[-1]
            print("""
            You Died...
            """)
            print("""
            You Scored: """, length-1, """ points.
            """)
            Done = True

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
