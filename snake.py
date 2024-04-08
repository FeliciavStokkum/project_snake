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
    direction = (0, 0)  # Start without movement

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

    def PositionAllowed(x, y, maxX, maxY):
        # Check if the position is within the screen boundaries
        if x < 0 or x >= maxX or y < 0 or y >= maxY:
            return False
        return True

    def checkCollision(posX, posY, snake_positions):
        # Check if the snake collides with itself
        return (posX, posY) in snake_positions[1:]

    maxX, maxY = (32, 16)
    game = pyMatrix(maxX, maxY, colourBackground=COLOUR_BACKGROUND, speed=5)
    posX, posY = maxX // 2, maxY // 2
    snake_positions = [(posX, posY)]
    colour = COLOUR_RED
    objectX, objectY = getRandomPos(maxX, maxY, snake_positions)

    while True:
        keys = game.getPressedKey()
        colour = change(keys, colour)
        dx, dy = direction
        nextPosX, nextPosY = posX + dx, posY + dy

        if not PositionAllowed(nextPosX, nextPosY, maxX, maxY) or (len(snake_positions) > 1 and checkCollision(nextPosX, nextPosY, snake_positions)):
            print("Game Over! Snake collided with itself")  # Game over message
            pygame.quit()
            quit()

        if (nextPosX, nextPosY) == (objectX, objectY):
            snake_positions.append((objectX, objectY))
            objectX, objectY = getRandomPos(maxX, maxY, snake_positions)
        else:
            if direction != (0, 0):  # If there is a movement direction set
                snake_positions.append((nextPosX, nextPosY))
                snake_positions.pop(0)
        posX, posY = nextPosX, nextPosY

        positions = [(objectX, objectY, COLOUR_GREEN)] + [(x, y, colour) for x, y in snake_positions]
        game.drawGame(positions)