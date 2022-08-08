import shape

class Rectangle(shape.Shape):
    def __init__(self,pn_l=0.0,pn_w=0.0):
        super().__init__('Rectangle',0.0,0.0)
        self.n_length = pn_l
        self.n_width = pn_w

    def calc(self):
        self.n_area = self.n_length * self.n_width
        self.n_perimeter = 2 * (self.n_length + self.n_width)

    def getdata(self):
        self.n_length = float(input("Length of Rectangle"))
        self.n_width = float(input("Width of Rectangle"))

    def show(self):
        self.calc()
        print(f"""
            ------RECTANGLE------
            Length    = {self.n_length:8.2f}
            Width     = {self.n_width:8.2f}
            Area      = {self.n_area:8.2f}
            Perimeter = {self.n_perimeter:8.2f}
            """)
    