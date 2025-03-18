import pgzrun

WIDTH = 400
HEIGHT = 400

def draw():
    screen.fill("blue")
    rec = Rect((200,200),(50,50))
    rec.center = 200,200
    screen.draw.rect(rec,"green")

    rec2 = Rect((350,300),(70,50))
    rec2.center = 350,300
#   screen.draw.rect(rec2,"red")
    screen.draw.filled_rect(rec2,"red")

pgzrun.go()