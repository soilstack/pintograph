x1,y1,x2,y2 = (100,100,200,200)
chunk = 10

def setup():
    size(800, 500)
    frameRate(10)

def draw():
    global x2

    background(255)
    line(x1,y1,x2,y2)
    x2 += chunk
