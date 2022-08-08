import Loan
#kg220801 class Loan with dictionary as argument to constructor
class EMI(Loan.Loan):   #class EMI is inherited from class Loan
    def __init__(self, pdct):
        super().__init__(pdct)
        self.n_tenure = pdct['Tenure']
        self.n_emi = 0.0

    def calc(self):
        super().calc()
        n1 = (1 + self.n_rate) ** self.n_year
        self.n_emi = self.n_principal * self.n_rate * ( n1 / (n1 - 1))

    def show(self):
        self.calc()
        super().show()
        print(f'EMI = {self.n_emi/self.n_tenure}')

#main starts
if __name__ == '__main__':
    dct = {'Borrower':'AAA','Principal':1111,'Year':2,'Tenure':24}
    o_emi1 = EMI(dct)
    o_emi1.show()