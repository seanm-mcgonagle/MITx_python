# classes
#__init__ is a special method, which initializes some data attributes


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff + sq)**0.5


""" 
self: paramter to refer to an instance of the class
__init__ special method to create an instance
x, y: what data initializes a Coordinate object
"""
c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(c.x)
print(origin.x)
print(origin.y)
print(c)
