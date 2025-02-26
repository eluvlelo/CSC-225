"""
Write a definition for a class named Circle with 
attributes center and radius, where center is a Point 
object and radius is a number.

Instantiate a Circle object that represents a circle 
with its center at (150, 100) and radius 75.

Write a function named point_in_circle that takes a 
Circle and a Point and returns True if the Point lies 
in or on the boundary of the circle.

Write a function named rect_in_circle that takes a 
Circle and a Rectangle and returns True if the 
Rectangle lies entirely in or on the boundary of 
the circle.

Write a function named rect_circle_overlap that 
takes a Circle and a Rectangle and returns True if 
any of the corners of the Rectangle fall inside the 
Circle. Or as a more challenging version, return True 
if any part of the Rectangle falls inside the Circle.
"""


# class Point:
#     """Represents a point in 2-D space.

#     attributes: x, y
#     """
# class Rectangle:
#     '''Represents a rectangle
    
#     Attributes: bottom-left corner, upper-right corner
#     '''
    
# class Circle:
#     """Represents a circle.

#     Attributes: center, radius
#     """

# def distance_between_points(p1, p2):
#     """Computes the distance between two Point objects.

#     p1: Point
#     p2: Point

#     returns: float
#     """
#     dx = p1.x - p2.x
#     dy = p1.y - p2.y
#     dist = (dx**2 + dy**2)**0.5
#     return dist

# def point_in_circle(point, circle):
#     """Checks if points lies within or on circle

#     point: Point object
#     circle: Circle object
#     """
    
#     d = distance_between_points(point, circle.center)
#     if d <= circle.radius:
#         return d
#     return False
    
    

# def rect_in_circle(rect, circle):
#     """Checks if entire rectangle lies within circle.
    
#     rect: Rectangle object
#     circle: Circle object
#     """ 
#     width = rect.tr.x - rect.bl.x
#     length = rect.tr.y - rect.bl.y
    
#     corner = rect.bl
#     print('(' + str(corner.x) + ',' + str(corner.y) + ')')
#     print('Distance between points:', distance_between_points(corner, circle.center))
#     if not point_in_circle(corner, circle):
#         return False
#     corner.y += length
#     print('(' + str(corner.x) + ',' + str(corner.y) + ')')
#     print('Distance between points:', distance_between_points(corner, circle.center))
#     if not point_in_circle(corner, circle):
#         return False
#     corner.x += width
#     print('(' + str(corner.x) + ',' + str(corner.y) + ')')
#     print('Distance between points:', distance_between_points(corner, circle.center))
#     if not point_in_circle(corner, circle):
#         return False
#     corner.y -= length
#     print('(' + str(corner.x) + ',' + str(corner.y) + ')')
#     print('Distance between points:', distance_between_points(corner, circle.center))
#     if not point_in_circle(corner, circle):
#         return False
#     return True

# def rect_circle_overlap(rect, circle):
#     """Checks if entire rectangle overlaps circle.
    
#     rect: Rectangle object
#     circle: Circle object
#     """ 
#     width = rect.tr.x - rect.bl.x
#     length = rect.tr.y - rect.bl.y
    
#     corner = rect.bl
#     print('(' + str(corner.x) + ',' + str(corner.y) + ')')
#     print('Distance between points:', distance_between_points(corner, circle.center))
#     if point_in_circle(corner, circle):
#         return True
#     corner.y += length
#     print('(' + str(corner.x) + ',' + str(corner.y) + ')')
#     print('Distance between points:', distance_between_points(corner, circle.center))
#     if point_in_circle(corner, circle):
#         return True
#     corner.x += width
#     print('(' + str(corner.x) + ',' + str(corner.y) + ')')
#     print('Distance between points:', distance_between_points(corner, circle.center))
#     if point_in_circle(corner, circle):
#         return True
#     corner.y -= length
#     print('(' + str(corner.x) + ',' + str(corner.y) + ')')
#     print('Distance between points:', distance_between_points(corner, circle.center))
#     if point_in_circle(corner, circle):
#         return True
#     return False
    
#point = Point()
#point.x = int(input(' Point x-coord: '))
#point.y = int(input('Point y-coord: '))
#print('Point', end=' ')
#print('(' + str(point.x) + ',' + str(point.y) + ')')

#circle = Circle()
#circle.center = Point()
#circle.center.x = int(input('center x-coord: '))
#circle.center.y = int(input('center y-coord: '))
#circle.radius = int(input('radius: '))
#print('Center', end=' ')
#print('(' + str(circle.center.x) + ',' + str(circle.center.y) + ')')

#print('Is point in circle:', point_in_circle(point, circle))

#rect = Rectangle()
#rect.bl = Point()
#rect.bl.x = int(input('Rect bottom left x-coord: '))
#rect.bl.y = int(input('Rect bottom left y-coord: '))
#rect.tr = Point()
#rect.tr.x = int(input('Rect upper right x-coord: '))
#rect.tr.y = int(input('Rect upper right y-coord: '))

#circle = Circle()
#circle.center = Point()
#circle.center.x = int(input('Circle center x-coord: '))
#circle.center.y = int(input('Circle center y-coord: '))
#circle.radius = int(input('radius: '))
#print('Center', end=' ')
#print('(' + str(circle.center.x) + ',' + str(circle.center.y) + ')')

#print('Is rectangle in circle: ', rect_in_circle(rect, circle))

#rect = Rectangle()
#rect.bl = Point()
#rect.bl.x = int(input('Rect bottom left x-coord: '))
#rect.bl.y = int(input('Rect bottom left y-coord: '))
#rect.tr = Point()
#rect.tr.x = int(input('Rect upper right x-coord: '))
#rect.tr.y = int(input('Rect upper right y-coord: '))

#circle = Circle()
#circle.center = Point()
#circle.center.x = int(input('Circle center x-coord: '))
#circle.center.y = int(input('Circle center y-coord: '))
#circle.radius = int(input('radius: '))
#print('Center', end=' ')
#print('(' + str(circle.center.x) + ',' + str(circle.center.y) + ')')

#print('Rectangle overlaps circle: ', rect_circle_overlap(rect, circle))

# print()
# print()
#using inheritance?


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    
class Circle:
    """Represents a circle.

    Attributes: center, radius
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Rectangle:
    '''Represents a rectangle
    
    Attributes: bl:bottom-left corner, tr:top-right corner
    '''
    def __init__(self, bl, tr):
        self.bl = bl
        self.tr = tr

def print_point(p):
    print('(' + str(p.x) + ',' + str(p.y) + ')')

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = (dx**2 + dy**2)**0.5
    return dist

def point_in_circle(point, circle):
        """Checks if points lies within or on circle.

        point: Point object
        circle: Circle object
        """
        d = distance_between_points(point, center)
        if d <= radius:
            print('distance:', d)
            return True
        print('distance:', d)
        return False

def rect_in_circle(rect, circle):
    """Checks if entire rectangle lies within circle.
    """ 
    width = rect.tr.x - rect.bl.x
    length = rect.tr.y - rect.bl.y
            
    corner = rect.bl
    print_point(rect.bl)
    if not point_in_circle(corner, center):
        return False
    corner.y += length
    print_point(corner)
    if not point_in_circle(corner, circle):
        return False
    corner.x += width
    print_point(corner)
    if not point_in_circle(corner, circle):
        return False
    corner.y -= length
    print_point(corner)
    if not point_in_circle(corner, circle):
        return False
    return True
    
def rect_circle_overlap(rect, circle):
    """Checks if entire rectangle lies within circle.
    """ 
    width = rect.tr.x - rect.bl.x
    length = rect.tr.y - rect.bl.y
    
    corner = rect.bl
    print_point(rect.bl)
    if point_in_circle(corner, center):
        return True
    corner.y += length
    print_point(corner)
    if point_in_circle(corner, circle):
        return True
    corner.x += width
    print_point(corner)
    if point_in_circle(corner, circle):
        return True
    corner.y -= length
    print_point(corner)
    if point_in_circle(corner, circle):
        return True
    return False

print('Circle')
center = Point(150, 100)
radius = 75
circle = Circle(center, radius)
print('center:', end=' ')
print_point(center)
print('radius:',  radius)
print()

point = Point(int(input('point-x: ')), int(input('point-y: ')))
print_point(point)
print()
 
print('Is point in circle?')
print((point_in_circle(point, circle)))
print()

bottomleft = Point(int(input('Rect bottom left x: ')), int(input('Rect bottom right y: ')))
upperright = Point(int(input('Rect upper left x: ')), int(input('Rect upper right y: ')))
rectangle = Rectangle(bottomleft, upperright)
print('bottom left corner: ')
print_point(bottomleft)
print('top right corner: ')
print_point(upperright)
print()

print('Is rectangle in circle?')
print((rect_in_circle(rectangle, circle)))
print()

bottomleft = Point(int(input('Rect bottom left x: ')), int(input('Rect bottom right y: ')))
upperright = Point(int(input('Rect upper left x: ')), int(input('Rect upper right y: ')))
rectangle = Rectangle(bottomleft, upperright)
print('bottom left corner: ')
print_point(bottomleft)
print('top right corner: ')
print_point(upperright)
print() 

print('Does rectangle overlap circle?')
print((rect_circle_overlap(rectangle, circle)))
print()

