class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square

    def __add__(self, other):
        r1_r2_square = self.get_square() + other.get_square()
        another_width = 2
        another_height = r1_r2_square // 2
        return Rectangle(another_width, another_height)

    def __mul__(self, n):
        n_width = self.width * n
        n_height = self.height
        return Rectangle(n_width, n_height)

    def __str__(self):
        return f"{self.width}, {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'