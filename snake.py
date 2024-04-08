from pyMatrix import *
import pygame
import random

if __name__ == "__main__":
    COLOUR_BACKGROUND = (100, 100, 100)
    COLOUR_RED = (255, 0, 0)
    COLOUR_GREEN = (0, 255, 0)
    COLOUR_BLUE = (0, 0, 255)
    COLOUR_WHITE = (255, 255, 255)
    COLOURS = (COLOUR_RED, COLOUR_GREEN, COLOUR_BLUE, COLOUR_WHITE)
    direction = (0, 0)  # Start zonder beweging

    def getRandomPos(maxX, maxY, occupied_positions=[]):
        while True:
            x, y = random.randint(0, maxX - 1), random.randint(0, maxY - 1)
            if (x, y) not in occupied_positions:
                return x, y

    def change(keys: list, colour):
        global direction
        if 27 in keys:  # ESC
            pygame.quit()
            quit()
        if ord("c") in keys:
            colour = random.choice(COLOURS)
        if 1073741905 in keys:  # Down
            direction = (0, 1)
        elif 1073741906 in keys:  # Up
            direction = (0, -1)
        elif 1073741904 in keys:  # Left
            direction = (-1, 0)
        elif 1073741903 in keys:  # Right
            direction = (1, 0)
        return colour

    maxX, maxY = (32, 16)
    game = pyMatrix(maxX, maxY, colourBackground=COLOUR_BACKGROUND, speed=5)
    posX, posY = maxX // 2, maxY // 2
    redPositions = [(posX, posY)]
    colour = COLOUR_RED
    objectX, objectY = getRandomPos(maxX, maxY, redPositions)

    while True:
        keys = game.getPressedKey()
        colour = change(keys, colour)
        dx, dy = direction
        nextPosX, nextPosY = posX + dx, posY + dy

        if game.isPosAllowed(nextPosX, nextPosY):
            if (nextPosX, nextPosY) == (objectX, objectY):
                redPositions.append((objectX, objectY))
                objectX, objectY = getRandomPos(maxX, maxY, redPositions)
            else:
                # Beweeg de hele slang vooruit als er niet gegroeid hoeft te worden.
                if direction != (0, 0):  # Voorkom dat de slang beweegt als er geen richting is ingesteld.
                    redPositions.append((nextPosX, nextPosY))
                    redPositions.pop(0)
            posX, posY = nextPosX, nextPosY

        positions = [(objectX, objectY, COLOUR_GREEN)] + [(x, y, colour) for x, y in redPositions]
        game.drawGame(positions)
