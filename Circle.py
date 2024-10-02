import math


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return 'Центр круга в точке: ({0}, {1}), радиус круга: {2}'.format(str(self.x), str(self.y), str(self.radius))

    def __call__(self):
        print(self)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * (self.radius ** 2)

    def is_intersect(self, obj):
        d = math.sqrt((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2)
        if abs(self.radius - obj.radius) < d < self.radius + obj.radius:
            return True
        if d == self.radius + obj.radius:
            return True
        if self.x == obj.x and self.y == obj.y:
            return True
        return False
