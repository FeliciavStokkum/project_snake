from pyMatrix import *
import pygame

if __name__ == "__main__":
    import random
    COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
    COLOUR_RED        = (255,   0,   0)
    COLOUR_GREEN      = (  0, 255,   0)
    COLOUR_BLUE       = (  0,   0, 255)
    COLOUR_WHITE      = (255, 255, 255)
    COLOURS = (COLOUR_RED, COLOUR_GREEN,COLOUR_BLUE, COLOUR_WHITE )

    def getRandomPos(maxX, maxY, notX = -1, notY = -1):
        x = random.randint(0,maxX-1)
        y = random.randint(0,maxY-1)
        if x == notX or y == notY:
            return getRandomPos(maxX, maxY, notX, notY)
        return x,y
    
    def change(keys: list, x, y, colour):
        if 27 in keys:	#esc
            game.quit()
        if pygame.K_LEFT in keys:
            x -= 1
        elif pygame.K_RIGHT in keys:
            x += 1
        elif pygame.K_UP in keys:
            y -= 1
        elif pygame.K_DOWN in keys:
            y += 1
        elif ord("c") in keys:
            colour = random.choice(COLOURS)
        return x, y, colour
    
    if True:
        maxX, maxY  = (32,16)
        game = pyMatrix(maxX, maxY, colourBackground = COLOUR_BACKGROUND)        
        posX = maxX // 2
        posY = maxY // 2
        objectX, objectY = getRandomPos(maxX, maxY, posX, posY) 
        moveX, moveY = (1,0)
        colour = COLOUR_RED
#       game.showNeoPixelIndex()
        speed = 10
        counter = 0
        while True:
            keys = game.getPressedKey()
            moveX, moveY, colour = change(keys, moveX, moveY, colour)

            if counter % speed == 0 and game.isPosAllowed(posX + moveX, posY + moveY):
                posX += moveX
                posY += moveY
            if objectX == posX and objectY == posY:
                objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
                
            positions =[ (objectX, objectY, COLOUR_GREEN)
           , (posX, posY, colour)
           , (posX-1, posY, colour)
           , (posX, posY, colour)
           ]
            
            game.drawGame (positions )
            
            counter += 1