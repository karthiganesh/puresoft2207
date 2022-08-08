import psycopg2
from tkinter import *
import pandas as pd
import numpy as np
#KG220805 Demo for db operations
class CCDBUI():
    def __init__(self):
        self.window = Tk()
        self.window.title("Welcome to Credit Card Application")
        self.lbl_app_no = Label(self.window, text="Application No")
        self.lbl_working = Label(self.window, text="Work Type")
        self.app_no = Entry()
        self.working = Entry()
        

        self.lbl_app_no.place(y=10,x=10)
        self.app_no.place(y=10,x=100)
        self.lbl_working.place(y=40,x=10)
        self.working.place(y=40,x=100)

class CCDB():
    def __init__(self):
        self.s_db='sgnxrfie'
        self.s_user='sgnxrfie'
        self.s_pwd = 'xLS2nfGGP1aSJyBhg94fXqtqOuKM1MET'
        self.s_host = 'tiny.db.elephantsql.com'
        self.conn = conn = psycopg2.connect(
            database=self.s_db, user=self.s_user, password=self.s_pwd, host=self.s_host)

    def get_cc_info(self,pn_appl_no):
        try:
            df_sel_appl = pd.read_sql(f'select * from "public"."creditcardappl" where "ID"={pn_appl_no}', con=self.conn)
            return df_sel_appl
        except Exception as e:
            print(f'Error {str(e)}')

    def get_total_income(self,ps_inc_type):
        try:
            df_sel_appl = pd.read_sql(f'select sum("AMT_INCOME_TOTAL") from creditcardappl where "NAME_INCOME_TYPE"=\'{ps_inc_type}\'', con=self.conn)
            return df_sel_appl['sum']
        except Exception as e:
            print(f'Error {str(e)}')

    def show_pivot(self, ps_col,out_xls='N'):
        df_cc = pd.read_sql(f'select * from "public"."creditcardappl"', con=self.conn)
        df_out=pd.pivot_table(df_cc,values='CNT_CHILDREN',index=ps_col,columns='NAME_HOUSING_TYPE',aggfunc=np.sum)
        if out_xls != 'N':
            df_out.to_excel(out_xls)
            return 'Stored in '+out_xls
        else:
            return df_out
    
#main starts here
c_repeat='Y'
o_cc = CCDB()
#o_ccui = CCDBUI()
#o_ccui.window.mainloop()
while c_repeat=='Y':
    n_appl = int(input("CC Appl No "))
    s_inc = input("Income Type ")
    s_col = input("Pivot Column")
    df_cc = o_cc.get_cc_info(n_appl)
    n_inc = o_cc.get_total_income(s_inc)
    df_out = o_cc.show_pivot(s_col,'out1.xlsx')
    print("Your result=",df_cc,n_inc)
    print(df_out)
    c_repeat = input("Repeat <Y/N> ?")