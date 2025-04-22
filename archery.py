import pgzrun
import random
WIDTH = 400
HEIGHT = 400

def draw():
    rad = 50
    for x in range(5):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        screen.draw.filled_circle((200,200),rad,(r,g,b))
        rad = rad - 10

pgzrun.go()