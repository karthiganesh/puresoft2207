#KG220728 Enhanced the previous program
import math
class Square():
    def __init__(self):
        self.n_side=0

    def run(self):
        self.n_side = float(input("Enter side "))
        self.n_area = self.n_side ** 2
        print(f"Area of Square = {self.n_area:10.2f}")

class Rectangle():
    def __init__(self):
        self.n_length = 0
        self.n_width = 0
        self.n_area = 0

    def run(self):
        self.n_length = float(input("Enter Length "))
        self.n_width = float(input("Enter Width "))
        self.n_area = self.n_length * self.n_width
        print(f"Area of Rectangle = {self.n_area:10.2f}")

class Circle():
    def __init__(self):
        self.n_radius =0.0
        self.n_area = 0.0

    def run(self):
        self.n_radius = float(input("Enter Radius "))
        self.n_area = math.pi * self.n_radius ** 2
        print(f"Area of Circle = {self.n_area:10.2f}")

#main starts here
if __name__ == "__main__":
    n_count = int(input("How many Shapes ? "))
    for x in range(0,n_count):
        n_choice = int(input("Enter your choice <1:Square / 2:Rectangle / 3:Circle> "))
        if n_choice == 1:
            o_shp = Square()
        elif n_choice == 2:
            o_shp = Rectangle()
        else:
            o_shp = Circle()
        o_shp.run()