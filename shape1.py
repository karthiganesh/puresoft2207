#KG220727 Demo for getting choice and run selected class
class Square():
    def run(self):

        try:
            n_a = float(input("Enter side "))
        except ValueError:
            print(f"Wrong {n_a} value entered")
        except Exception as e8:
            print(f'Error {str(e8)}')

        try:
            n_area = n_a * n_a
        except ValueError:
            print(f"Wrong Area")
        except Exception as e8:
            print(f'Error {str(e8)}')

        print(f"Area of Square = {n_area:10.2f}")

class Rectangle():
    def run(self):
        try:
            n_len = float(input("Enter Length "))
            n_wid = float(input("Enter Width "))
            n_area = n_len * n_wid
            print(f"Area of Rectangle = {n_area:10.2f}")
        except Exception as e18:
            print(f'Error {str(e18)}')

class Circle():
    def run(self):
        try:
            n_rad = float(input("Enter Radius "))
            n_area = 3.1417 * n_rad ** 2
            print(f"Area of Circle = {n_area:10.2f}")
        except Exception as e27:
            print(f'Error {str(e27)}')


#main starts here
if __name__ == "__main__":
    try:
        n_choice = input("Enter your choice ")
        if n_choice == 'S':
            o_shp = Square()
        elif n_choice == 'R':
            o_shp = Rectangle()
        elif n_choice == 'C':
            o_shp = Circle()
        o_shp.run()
    except Exception as e42:
        print(f'Error {str(e42)}')
