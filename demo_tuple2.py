import ex015o3_interest
#KG220801 Demo for List
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

#main starts here
tup_loans = ()
c_repeat = 'Y'
while c_repeat == 'Y':
    try:
        s_borrower = input("Borrower Name ")
        n_pri = float(input("Principal Amount "))
        n_year = int(input("Number of Years "))
        tup_loans.append(ex015o3_interest.Interest(s_borrower,n_pri, n_year))
        c_repeat = input("Repeat <Y/N> ? ")
    except Exception as e:
        print(f'Error {str(e)}')
print_loans(tup_loans)