import Loan
#KG220801 Demo for Dictionary

def process_loan(dct):
    p = dct['Principal']
    n = dct['Year']
    r = dct['Rate']
    si = p * n * r / 100.0
    print(si)

dct_b = {'Borrower':'bbbb','Principal':22222,'Year':2,'LoanType':'EMI','Rate':8.2}
o_b = Loan.Loan(dct_b)
o_b.show()
print('Function')
process_loan(dct_b)
