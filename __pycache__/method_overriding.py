class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x *self.y
class circle(shape):
      def __init__(self,radius):
        self.radius=radius
        super().__init__(self.radius,self.radius)

      def area(self):
        return 3.14 *super().area()

a=shape(3,4)
print(a.area())
b=circle(9)
print(b.area())
