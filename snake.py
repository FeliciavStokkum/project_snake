COMPUTER = False
if COMPUTER:
    from pyMatrix import *
else:
    from machine import Pin
    import neopixel
    PIN_DIN = 28
    PIXELS = 512
    
import random
speed_data = 5
counter = 0
counter_max = 3


COLOUR_BACKGROUND = (0, 0, 0)
COLOUR_RED = (10, 0, 0)
COLOUR_GREEN = (0, 10, 0)
COLOUR_BLUE = (0, 0, 10)
COLOUR_WHITE = (10, 10, 10)
COLOURS = (COLOUR_RED, COLOUR_GREEN, COLOUR_BLUE, COLOUR_WHITE)
direction = (0, 0)  # Start without movement

def getRandomPos(maxX, maxY, occupied_positions=[]):
    while True:
        x, y = random.randint(0, maxX - 1), random.randint(0, maxY - 1)
        if (x, y) not in occupied_positions:
            return x, y

def change(keys: list, colour): # movement keys
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
if COMPUTER:
    game = pyMatrix(maxX, maxY, colourBackground=COLOUR_BACKGROUND, speed=speed_data)
else:
    _np = neopixel.NeoPixel(Pin(PIN_DIN), PIXELS)

posX, posY = maxX // 2, maxY // 2
snake_positions = [(posX, posY)]
colour = COLOUR_RED
objectX, objectY = getRandomPos(maxX, maxY, snake_positions)

while True:
    keys = []#game.getPressedKey()
    colour = change(keys, colour)
    dx, dy = direction
    nextPosX, nextPosY = posX + dx, posY + dy

    if not PositionAllowed(nextPosX, nextPosY, maxX, maxY) or (len(snake_positions) > 1 and checkCollision(nextPosX, nextPosY, snake_positions)):
        print("Game Over! Snake collided with itself")  # Game over message
        print(f'The snake ate {counter} pieces of fruit')
        pygame.quit()
        quit()

    if (nextPosX, nextPosY) == (objectX, objectY): # if fruit is hit
        snake_positions.append((objectX, objectY))
        objectX, objectY = getRandomPos(maxX, maxY, snake_positions)
        game = pyMatrix(maxX, maxY, colourBackground=COLOUR_BACKGROUND, speed=random.randint(1, 20)) # ranodm speed
        counter += 1
        if COLOUR_GREEN == (10, 0, 10): # if paars maak groen fruit
            snake_positions.append((objectX, objectY))
            counter += 1
        COLOUR_GREEN = 0, 10, 0
        if counter >= counter_max: # counter voor paars fruit
            COLOUR_GREEN = 10, 0, 10
            # counter = 0
            counter_max += random.randint(3, 10)
    else:
        if direction != (0, 0):  # If there is a movement direction set
            snake_positions.append((nextPosX, nextPosY))
            snake_positions.pop(0)
    posX, posY = nextPosX, nextPosY

    positions = [(objectX, objectY, COLOUR_GREEN)] + [(x, y, colour) for x, y in snake_positions]
    if COMPUTER:
        game.drawGame(positions)
    else:
        for x,y,color in positions:
            p = x#convert(x,y)
            _np[p] = color
        _np.write()