import Loan
#kg220801 class Loan with dictionary as argument to constructor
class OD(Loan.Loan):   #class EMI is inherited from class Loan
    def __init__(self, pdct):
        super().__init__(pdct)
        self.n_rate = 3.2
        if self.n_year < 4:
            self.n_rate = 4.2
        elif self.n_year < 6:
            self.n_rate = 3.7

#main starts
if __name__ == '__main__':
    dct = {'Borrower':'AAA','Principal':1111,'Year':2}
    o_emi1 = OD(dct)
    o_emi1.show()
    o_loan = Loan.Loan(dct)
    o_loan.show()