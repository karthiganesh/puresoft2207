#KG220726 Demo for Area of Rectangle

try:
    n_length = float(input("Length "))
    n_width = float(input("Width "))
    n_area = n_length * n_width
    print("Area ",n_area)
    print("Completed Successfully")
except Exception as e:
    print("Error",str(e))