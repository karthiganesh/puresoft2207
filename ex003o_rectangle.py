#KG220726 Demo for Area of Rectangle
class Rectangle():
    def run(self):  #all methods in a class must self as first parameters
        try:
            print('line 5',__name__)
            n_length = float(input("Length "))
            n_width = float(input("Width "))
            n_area = n_length * n_width
            print("Area ",n_area)
            print("Completed Successfully")
        except Exception as e:
            print("Error",str(e))

def sample_funct():
    print('line15',__name__)

#main starts here
if __name__ == "__main__":   #use this line to indicate main entry point for your program
    print('line 19',__name__)
    o_rect1 = Rectangle()
    o_rect1.run()
    sample_funct()
