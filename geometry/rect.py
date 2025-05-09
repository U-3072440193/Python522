class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimeter(self):
        return 2 * (self.h + self.w)


print(__name__)
