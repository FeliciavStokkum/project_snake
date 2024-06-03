import random
from machine import Pin
import neopixel

PIN_DIN = 28
PIXELS = 512
positions = []
for x in range(PIXELS):
    positions.append(x)
    
_np = neopixel.NeoPixel(Pin(PIN_DIN), PIXELS)
def clear():
    for x in positions:
        _np[x] = (0,0,0)
    _np.write()

def showPixel(p, color):
    _np[p] = color
    _np.write()
    
clear()
while True:
    for x in range(PIXELS):
        ran_color1 = random.randint(1,2)
        ran_color2 = random.randint(1,2)
        ran_color3 = random.randint(1,2)
        
        r= random.randint(0, 255)
        g= random.randint(0, 255)
        b= random.randint(0, 255)
        showPixel(x, (ran_color1,ran_color2,ran_color3))

