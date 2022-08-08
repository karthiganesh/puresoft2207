#kg220801 class Loan with dictionary as argument to constructor
class Loan():
    def __init__(self,pdct):
        self.s_name = pdct['Borrower']
        self.n_principal = pdct['Principal']
        self.n_year = pdct["Year"]
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

def print_loans(plst_loans):
    print('--------------------- ABC Bank ----------------------------')
    print('Loan applications')
    print('------------------------------------------------------------')
    print(f'Borrower\tPrincipal\tYear\tRate\tInterest')
    print('------------------------------------------------------------')
    n_total_int = 0.0
    #line
    for ln in plst_loans:
        ln.calc()
        n_total_int += ln.n_si
        #line
        print(f'{ln.s_name}\t\t{ln.n_principal:8.2f}\t{ln.n_year:2d}\t{ln.n_rate:5.1f}\t{ln.n_si:8.2f}')
    print('---------------------------------------------------------')
    print(f"Total Interest : {n_total_int:10.2f}")
    #line
    print('---------------------------------------------------------')
