import math

def setup():
    size(1500, 1000)
    noLoop()

#https://py.processing.org/reference/

def get_circle_linkage(radius, origin, rotation_rate, cycle, degree_offset=0):
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


def get_vertex_point(P0, P1, L1, L2, ):
    """
    P0:  (x,y) position of point 0
    P1:  (x,y) position of point 1
    L1:  length of arm 1
    L2:  length of arm 2
    
    returns (P3a, P3b) 
    """
    
    d = math.sqrt((P1[0]-P0[0])**2 + (P1[1]-P0[1])**2) 
    a = (L1**2 + d**2 - L2**2)/(2*d)
    h = math.sqrt(L1**2 - a**2)
    b = math.sqrt(L2**2 - h**2)
    
    _x2 = P0[0] + (a/d)*(P1[0]-P0[0])
    _y2 = P0[1] + (a/d)*(P1[1]-P0[1])
    P2 = (_x2,_y2)
    
    _x3a = P2[0] - h*(P1[1]-P0[1])/d
    _y3a = P2[1] + h*(P1[0]-P0[0])/d
    P3a = (_x3a, _y3a)
    
    _x3b = P2[0] + h*(P1[1]-P0[1])/d
    _y3b = P2[1] - h*(P1[0]-P0[0])/d
    P3b = (_x3b, _y3b)
    
    return (P3a, P3b)
    
    
def extrapolate_pivot(origin_pt, pivot_pt, beam_length):
    """
    return location of point on other side of the pivot
    beam_length: the length of the second half of segment
    """
    
    d = math.sqrt((pivot_pt[0]-origin_pt[0])**2 + (pivot_pt[1]-origin_pt[1])**2)
    #print(d)
    x_unit_component = (pivot_pt[0]-origin_pt[0])/d
    y_unit_component = (pivot_pt[1]-origin_pt[1])/d
    #print(x_unit_component, y_unit_component)
    result_pt = ( (pivot_pt[0]+x_unit_component*beam_length), (pivot_pt[1]+y_unit_component*beam_length) )
    return result_pt

   
   
def draw():
    left_radius=60
    left_origin=(470,200)
    left_rotation_rate = 21*3
    left_degree_offset = 0

    right_radius=110
    right_origin=(730,200)
    right_rotation_rate = 23*120
    right_degree_offset = 0

    L1 = 250
    L2 = 250
    L3 = 100
    L4 = 100
    L5 = 200
    L6 = 200
        
    for cycle  in range(0,10000,1):

        P0 = get_circle_linkage(left_radius, left_origin, left_rotation_rate, cycle, degree_offset=left_degree_offset)
        P1 = get_circle_linkage(right_radius, right_origin, right_rotation_rate, cycle, degree_offset=right_degree_offset)

        P2a,P2b = get_vertex_point(P0, P1, L1, L2, )

        P3 = extrapolate_pivot(origin_pt=P1, pivot_pt=P2a, beam_length=L3)
        P4 = extrapolate_pivot(origin_pt=P0, pivot_pt=P2a, beam_length=L4)

        P_pen = get_vertex_point(P3, P4, L5, L6, )
        
        #print("before circle")
        circle(P0[0], P0[1], 3)
        circle(P1[0], P1[1], 3)
        #print("after circle")
        #print(P_pen[0])
        #print(P_pen[1])
        point(int(P_pen[0][0]), int(P_pen[0][1]), )        
        
        
        
