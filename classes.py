class Coordinate(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return self.name + ": <" + str(self.x) + "," + str(self.y) + ">"


c = Coordinate("c", 5, 3)
origin = Coordinate("origin", 0, 0)

print("distance from %s to %s is" % (c.name, origin.name), c.distance(origin))
print("print __str__ method at work:\n", c)
