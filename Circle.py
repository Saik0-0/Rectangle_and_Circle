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

    def intersect_square(self, obj):
        if not self.is_intersect(obj):
            return False
        d = math.sqrt((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2)
        if d <= abs(self.radius - obj.radius):
            return math.pi * (min(self.radius, obj.radius) ** 2)

        sqr1 = self.radius ** 2 * math.acos((d ** 2 + self.radius ** 2 - obj.radius ** 2) / (2 * d * self.radius))
        sqr2 = obj.radius ** 2 * math.acos((d ** 2 + obj.radius ** 2 - self.radius ** 2) / (2 * d * obj.radius))
        sqr3 = 0.5 * math.sqrt((-d + self.radius + obj.radius) * (d + self.radius - obj.radius) * (d - self.radius + obj.radius) * (d + self.radius + obj.radius))

        return sqr1 + sqr2 - sqr3
