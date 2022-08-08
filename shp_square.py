import shape

class Square(shape.Shape):
    def __init__(self,pn_s=0.0):
        super().__init__('Square',0.0,0.0)
        self.n_side = pn_s

    def calc(self):
        self.n_area = self.n_side ** 2
        self.n_perimeter = 4 * self.n_side
    def getdata(self):
        self.n_side = float(input("Side of Square"))

    def show(self):
        self.calc()
        print(f"""
            -----SQUARE------
            Side      = {self.n_side:8.2f}
            Area      = {self.n_area:8.2f}
            Perimeter = {self.n_perimeter:8.2f}
            """)
    