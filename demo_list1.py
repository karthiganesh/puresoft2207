import ex015o3_interest
#KG220801 Demo for List
if 1==0:
    lst_days = []
    c_repeat = 'Y'
    while c_repeat == 'Y':
        s_day = input("enter Weekday")
        lst_days.append(s_day)
        c_repeat = input("Repeat <Y/N> ? ")
    print(lst_days)

def print_loans(plst_loans):
    print('------- ABC Bank---------')
    print('Loan applications')
    print('------------------------------------')
    print(f'Borrower\tPrincipal\tYear\tRate\tInterest')
    print('------------------------------------')
    for ln in plst_loans:
        ln.calc()
        print(f'{ln.s_name}\t\t{ln.n_principal:8.2f}\t{ln.n_year:2d}\t{ln.n_rate:5.1f}\t{ln.n_si:8.2f}')
    print('------------------------------------')

if 1==1:
    lst_loans = []
    c_repeat = 'Y'
    while c_repeat == 'Y':
        try:
            s_borrower = input("Borrower Name ")
            n_pri = float(input("Principal Amount "))
            n_year = int(input("Number of Years "))
            lst_loans.append(ex015o3_interest.Interest(s_borrower,n_pri, n_year))
            c_repeat = input("Repeat <Y/N> ? ")
        except Exception as e:
            print(f'Error {str(e)}')
    for ln in lst_loans:
        ln.show()
    print_loans(lst_loans)