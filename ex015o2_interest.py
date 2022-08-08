#KG220726 Demo for Simple Interest calculation
class Interest():
    def __init__(self,ps_nm='',pn_p=0,pn_n=0):
        self.s_name = ps_nm
        self.n_principal = pn_p
        self.n_year = pn_n
        self.n_si = 0
        self.n_rate = 7.2
        if self.n_year < 4:
            self.n_rate = 9.4
        elif self.n_year < 6:
            self.n_rate = 8.3

    def calc(self):
        self.n_si = self.n_principal * self.n_year * self.n_rate / 100.0

    def show(self):
        try:
            self.calc()
            s_output = f"""
            Principal       = {self.n_principal:10.2f}
            Rate            = {self.n_rate:10.2f}
            Year            = {self.n_year:10.2f}
            Simple Interest = {self.n_si:10.2f}"""
            print(s_output)
        except Exception as e:
            print(f"Error {str(e)}")

#main stats here
if __name__ == "__main__":
    n_count = int(input("How many borrowers ? "))
    for i in range(1,n_count+1):
        s_name = input("Borrower : ")
        n_p = float(input("Principal : "))
        n_n = int(input("Year  : "))
        o_int = Interest(s_name,n_p,n_n)
        o_int.show()
