#KG220726 Demo for Simple Interest calculation
class Interest():
    def run(self):
        try:
            s_name = input("Borrower Name ")
            n_principal = float(input("Principal Amount "))
            n_year = float(input("Number of Years "))
            n_rate = 7.2
            if n_year < 4:
                n_rate = 9.4
            elif n_year < 6:
                n_rate = 8.3
            n_si = n_principal * n_year * n_rate / 100.0
            s_output = f"Principal={n_principal:10.2f}\nRate={n_rate:10.2f}\nYear={n_year:10.2f}\nSimple Interest = {n_si:10.2f}"
            print(s_output)
            print("Completed Successfully")
        except Exception as e:
            print(f"Error {str(e)}")

#main stats here
if __name__ == "__main__":
    o_int = Interest()
    o_int.run()
