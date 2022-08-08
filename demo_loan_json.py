import Loan
import json

fl_loan=open('loan_app.json')
dct_app = json.load(fl_loan)
lst_loans = []
for ln in dct_app['loan_applications']:
    lst_loans.append(Loan.Loan(ln))
Loan.print_loans(lst_loans)
c_repeat = 'Y'
lst_loans = []
while c_repeat=='Y':
    s_b = input("Borrower")
    n_p = float(input("Principal"))
    n_y = int(input("Year"))
    dct = {'Borrower':s_b,'Principal':n_p,'Year':n_y}
    lst_loans.append({"B":s_b,"P":n_p,"Y":n_y})
    c_repeat = input('Continu <Y/N> ?')
fl_out = open('loan_save.json','w')
json.dump({"app":lst_loans},fl_out)
fl_out.close()