#KG220727 Demo for finding biggest among 4 numbers
class Biggest():
    def run(self):
        n_a = (input("Enter A "))
        n_b = (input("Enter B "))
        n_c = (input("Enter C "))
        n_d = (input("Enter D "))
        if n_a >= n_b and n_a >= n_c and n_a >= n_d:
            print(f"A is the biggest {n_a}")
        elif n_c >= n_a and n_c >= n_b and n_c >= n_d:
            print(f"C is the biggest {n_c}")
        elif n_b >= n_a and n_b >= n_c and n_b >= n_d:
            print(f"B is the biggest {n_b}")
        elif n_d >= n_a and n_d >= n_b and n_d >= n_c:
            print(f"D is the biggest {n_d}")
        print("<end>")

#main starts here
if __name__ == "__main__":
    o_big = Biggest()
    o_big.run()