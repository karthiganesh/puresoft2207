import psycopg2
import getpass
import pandas as pd 

#establishing the connection
s_db='***'
s_user='***'
s_pwd = getpass.getpass()
s_host = getpass.getpass()
conn = psycopg2.connect(
   database=s_db, user=s_user, password=s_pwd, host=s_host
)

df = pd.read_sql('select * from "App1_product"', con=conn)
print(df)
print(df.describe())

#Closing the connection
conn.close()
