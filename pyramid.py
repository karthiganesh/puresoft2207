class Pyramid():
    def __init__(self,pn=5):
        self.n = pn

    def pyramid1(self):
        for i in range(0,self.n):
            for j in range(0,i+1):
                print("*",end='')
            print("\r")

    def pyramid2(self):
        k = 2 * self.n - 2
        for i in range(0, self.n):
            for j in range(0, k):
                print(end=" ")
            k = k - 2
            for j in range(0, i+1):
                print("* ",end="")
            print("\r")

#main
if __name__ == "__main__":
    o_a = Pyramid(10)
    o_a.pyramid1()
    o_a.pyramid2()
    try:
        a = '\u8749'
        print(a)
        b = '3434' + 353
    except ArithmeticError:
        print("Please check your expressions")
    except UnicodeError:
        print("Unable to process unicode")
    except ValueError:
        print("Given value is not applicable for this context")

