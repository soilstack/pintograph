import math

def setup():
    size(1500, 800)
    noLoop()

#https://py.processing.org/reference/

def circle_linkage(radius, origin, rotation_rate, cycle):
    """
    radius:
    origin: (x,y)
    rotation_rate: cycles per full revolution
    cycle: 
    """
    
    RADIANS_IN_CIRCLE = 2 * math.pi

    pct_rotation = (cycle*1.0 % rotation_rate) / rotation_rate
    radians = RADIANS_IN_CIRCLE * pct_rotation
    print(pct_rotation, radians)
    x_component = radius * math.cos(radians)
    y_component = radius * math.sin(radians)
    pivot = (origin[0]+x_component, origin[1]+y_component)
    return pivot


def draw():
    line(50,50,75,75)
    origin = (width/2,height/2)
    radius = height/3
    rotation_rate = 100
    for cycle in range(45,95,1):
        tip = circle_linkage(radius, origin, rotation_rate, cycle)
        print(cycle, origin[0], origin[1], tip[0], tip[1])
        #line(origin[0], origin[1], tip[0], tip[1])
        circle(tip[0], tip[1], 3)
    
