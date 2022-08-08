#KG220727 Demo for getting choice and run selected class
class Square():
    def run(self):
        n_a = float(input("Enter side "))
        n_area = n_a * n_a
        print(f"Area of Square = {n_area:10.2f}")

class Rectangle():
    def run(self):
        n_len = float(input("Enter Length "))
        n_wid = float(input("Enter Width "))
        n_area = n_len * n_wid
        print(f"Area of Rectangle = {n_area:10.2f}")

class Circle():
    def run(self):
        n_rad = float(input("Enter Radius "))
        n_area = 3.1417 * n_rad ** 2
        print(f"Area of Circle = {n_area:10.2f}")

#main starts here
if __name__ == "__main__":
    n_choice = int(input("Enter your choice "))
    if n_choice == 1:
        o_shp = Square()
    elif n_choice == 2:
        o_shp = Rectangle()
    else:
        o_shp = Circle()
    o_shp.run()