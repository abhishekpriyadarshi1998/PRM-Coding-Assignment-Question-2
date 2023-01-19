class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validate_triangle(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            print("Valid Triangle")
        else:
            print("Invalid Triangle")


class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def validate_rectangle(self):
        if self.l == self.b:
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")


x = list(map(int, input().split()))
t = Triangle(x[0], x[1], x[2])
t.validate_triangle()
p = list(map(int, input().split()))
r = Rectangle(p[0], p[1])
r.validate_rectangle()