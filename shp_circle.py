import shape
import math

class Circle(shape.Shape):
    def __init__(self,pn_r=0.0):
        super().__init__('Circle',0.0,0.0)
        self.n_radius = pn_r

    # def calc(self):
    #     self.n_area = math.pi * self.n_radius ** 2
    #     self.n_perimeter = 2 * math.pi * self.n_radius

    def getdata(self):
        self.n_radius = float(input("Radius of Circle"))

    def show(self):
        self.calc()
        print(f"""
            -----CIRCLE--------
            Radius    = {self.n_radius:8.2f}
            Area      = {self.n_area:8.2f}
            Perimeter = {self.n_perimeter:8.2f}
            """)
    