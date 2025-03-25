import pgzrun
import random
WIDTH = 400
HEIGHT = 400
def draw():
    wid = 400
    hei = 150
    for x in range(30):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rec1 = Rect((400,200),(wid,hei))
        rec1.center = 200,200
        screen.draw.rect(rec1,(r,g,b))
        wid = wid - 10
        hei = hei + 10
    screen.draw.text("hi",(200,200),color = "green")

pgzrun.go()