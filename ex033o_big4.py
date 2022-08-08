#KG220727 Demo for finding biggest among 4 numbers
class Biggest():
    def run(self):
        n_a = (input("Enter A "))
        n_b = (input("Enter B "))
        n_c = input("Enter C")
        if n_a < n_b and n_a < n_c:
            if n_b < n_c:
                print(n_a,n_b,n_c)
            else:
                print(n_a,n_c,n_b)
        elif n_b <
            print(n_b,n_a)
        print("<end>")

#main starts here
if __name__ == "__main__":
    o_big = Biggest()
    o_big.run()