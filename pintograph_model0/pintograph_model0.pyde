import math

def setup():
    size(1000, 800)
    noLoop()

#https://py.processing.org/reference/

def circle_linkage(radius, origin, rotation_rate, cycle, degree_offset=0):
    """
    radius:
    origin: (x,y)
    rotation_rate: cycles per full revolution
    cycle: 
    degree_offset:  offset the arm by n-Degrees 
    """
    
    RADIANS_IN_CIRCLE = 2 * math.pi

    pct_rotation = (cycle*1.0 % rotation_rate) / rotation_rate
    radians = (RADIANS_IN_CIRCLE * pct_rotation) + math.radians(degree_offset)
    #print(pct_rotation, radians)
    x_component = radius * math.cos(radians)
    y_component = radius * math.sin(radians)
    pivot = (origin[0]+x_component, origin[1]+y_component)
    return pivot



def pen_position(P0, P1, L1, L2):
    """
    P0:  (x,y) position of point 0
    P1:  (x,y) position of point 1
    L1:  length of arm 1
    L2:  length of arm 2
    """
    
    d = math.sqrt((P1[0]-P0[0])**2 + (P1[1]-P0[1])**2) 
    #print(f"d: {d:.2f}")
    
    a = (L1**2 + d**2 - L2**2)/(2*d)
    #print(f"a: {a:2f}")
    
    h = math.sqrt(L1**2 - a**2)
    #print(f"h: {h:.2f}")
    
    b = math.sqrt(L2**2 - h**2)
    #print(f"b: {b:.2f}")
    
    _x2 = P0[0] + (a/d)*(P1[0]-P0[0])
    _y2 = P0[1] + (a/d)*(P1[1]-P0[1])
    P2 = (_x2,_y2)
    #print(f"P2: {P2}")
    
    _x3a = P2[0] - h*(P1[1]-P0[1])/d
    _y3a = P2[1] + h*(P1[0]-P0[0])/d
    P3a = (_x3a, _y3a)
    #print(f"P3a: {P3a}")
    
    
    _x3b = P2[0] + h*(P1[1]-P0[1])/d
    _y3b = P2[1] - h*(P1[0]-P0[0])/d
    P3b = (_x3b, _y3b)
    #print(f"P3b: {P3b}")
     
    return P3a
    

def draw():
    #line(50,50,75,75)
    #origin = (width/2,height/2)
    #radius = height/3
    
    left_radius=100
    left_origin=(200,200)
    left_rotation_rate = 21*10
    left_degree_offset = 180

    right_radius=140
    right_origin=(600,200)
    right_rotation_rate = 23*10
    right_degree_offset =0

    L1 = 240
    L2 = 400
    
    # Short Arms sanity check
    combined_arm_length = L1 + L2
    center_center = math.sqrt(  (right_origin[0]-left_origin[0])**2 + (right_origin[1]-left_origin[1])**2   )
    try:
        assert combined_arm_length >= (center_center + left_radius + right_radius)
    except AssertionError:
        print("arms too short to span wheels")
        print("combined_arm_length "+str(combined_arm_length))
        print("center_center + left_radiud + right_radius "+str(center_center + left_radius + right_radius))
        raise Exception
        
    # Triangle Inequality Far Check
    c = L1
    a = L2
    b = (center_center + right_radius + left_radius)
    try:
        assert a+b > c, "far check: a+b > c fail"
        assert a+c > b, "far check: a+c > b fail"
        assert b+c > a, "far check: b+c > a fail"
    except AssertionError:
        print("a "+ str(a))
        print("b "+ str(b))
        print("c "+ str(c))

        
    # Triangle Inequality Near Check
    c = L1
    a = L2
    b = (center_center - right_radius - left_radius)
    try:
        assert a+b > c, "far check: a+b > c fail"
        assert a+c > b, "far check: a+c > b fail"
        assert b+c > a, "far check: b+c > a fail"
    except AssertionError:
        print("a "+ str(a))
        print("b "+ str(b))
        print("c "+ str(c))
               
                                
                
    initial_pen = None
    
    for cycle  in range(0,150000,1):
        left_tip = circle_linkage(left_radius, left_origin, left_rotation_rate, cycle, left_degree_offset)
        right_tip = circle_linkage(right_radius, right_origin, right_rotation_rate, cycle, right_degree_offset)

        circle(left_tip[0], left_tip[1], 3)
        circle(right_tip[0], right_tip[1], 3)

        pen = pen_position(left_tip, right_tip, L1, L2)
        
        #circle(pen[0], pen[1], 3)
        point(pen[0], pen[1], )
        
        if initial_pen is None:
            print("initial pen location: ")
            print(pen)
            initial_pen = pen
    
    print("final pen location: ")
    print(pen)
