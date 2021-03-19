class Rectangle:
   def __init__(self, width, length):
       self.width = width
       self.length = length

   def area(self):
       return self.width * self.length 

   def perimeter(self):
       return 2 * (self.width + self.length)

   def print_info(self):
       print("Rectangle info: ")
       return f"Area - {self.area()}\nPerimeter - {self.perimeter()}\nWidth - {self.width}\nLength - {self.length}"


if __name__ == "__main__":
   L = Rectangle(7, 3)
   print(L.print_info())




