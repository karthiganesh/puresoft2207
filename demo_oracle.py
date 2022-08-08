# import the Oracle Python library
import cx_Oracle
import datetime
import pandas as pd
import numpy as np
import getpass

# setting display width for outputs in PyCharm
desired_width = 280
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',30)

# define the login details
p_username = "************"
p_password = getpass.getpass()
p_host = "************"
p_service = "************"
p_port = "1521"

print('--------------------------------------------------------------------------')
print(' Testing the time to extract data from an Oracle Database.')
print('    using different approaches.')
print('---')
# create the connection
con = cx_Oracle.connect(user=p_username, password=p_password, dsn=p_host+"/"+p_service+":"+p_port)

print('')
print(' Test 1: Extracting data using Cursor for different Array sizes')
print('    Array Size = 5, 50, 500, 1000, 2000, 3000, 4000, 5000')
print('')
print('   Starting test at : ', datetime.datetime.now())

beginTime = datetime.datetime.now()
cur_array_size = (5, 50, 500, 1000, 2000, 3000, 4000, 5000)
sql = 'select * from <table> limit 100'

for size in cur_array_size:
    startTime = datetime.datetime.now()
    cur = con.cursor()
    cur.arraysize = size
    results = cur.execute(sql).fetchall()
    print('      Time taken : array size = ', size, ' = ', datetime.datetime.now()-startTime, ' seconds,  num of records = ', len(results))
    cur.close()

print('')
print('   Test 1: Time take = ', datetime.datetime.now()-beginTime)
print('')