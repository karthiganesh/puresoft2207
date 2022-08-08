import pandas as pd

df = pd.read_csv('stu.csv')
n_total_sub1 = 0
n_total_sub2 = 0
n_total_sub3 = 0
n_total_sub4 = 0
n_total_sub5 = 0
try:
    for idx,stu in df.iterrows():
        print('idx=',idx)
        print(stu)
        n_total_sub1 += stu['Sub1']
        n_total_sub2 += stu['Sub2']
        n_total_sub3 += stu['Sub3']
        n_total_sub4 += stu['Sub4']
        n_total_sub5 += stu['Sub5']
except AttributeError:
    print("Looks like your CSV file does not have column Sub6")
print(f'Sub1 Total={n_total_sub1}')
print(f'Sub2 Total={n_total_sub2}')
print(f'Sub3 Total={n_total_sub3}')
print(f'Sub4 Total={n_total_sub4}')
print(f'Sub5 Total={n_total_sub5}')
print(df.describe())
df.plot.bar(x='Sub1',y='Sub2')