#KG220726 Demo for Simple Interest calculation
class Interest():
    def run(self):
        try:
            s_name = input("Borrower Name ")
            n_principal = float(input("Principal Amount "))
            n_rate = float(input("Rate of Interest "))
            n_year = float(input("Number of Years "))
            n_si = n_principal * n_year * n_rate / 100.0
            s_output = f"Principal={n_principal}\nRate={n_rate}\nYear={n_year}\nSimple Interest = {n_si}"
            print("---------------------------------")
            print(s_output)
            print("*********************************")
            print("Principal=",n_principal,"\nRate=",n_rate,"\nYear=",n_year,"\nSimple Interst = ",n_si)
            print("Completed Successfully")
        except Exception as e:
            print(f"Error {str(e)}")

#main stats here
if __name__ == "__main__":
    o_int = Interest()
    o_int.run()
