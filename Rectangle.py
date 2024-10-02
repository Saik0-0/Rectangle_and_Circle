class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return 'Ширина: ' + str(self.width) + ', высота: ' + str(self.height)

    def __call__(self):
        print(self)

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_intersect(self, obj):
        if self.x + self.width <= obj.x or obj.x + obj.width <= self.x:
            return False
        if self.y + self.height <= obj.y or obj.y + obj.height <= self.y:
            return False
        return True
