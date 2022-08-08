#KG220801 Demo for List
set_odd_days = {'Mon','Wed','Fri','Sun'}
set_even_days = {'Tue','Thu','Sat','Sun'}
set_all_days = set_odd_days.union(set_even_days)
print(set_all_days)
print(set_odd_days.intersection(set_even_days))
lst_stu = ['aaa','bbb','ccc','ddd','aaa','eee','bbb','aaa']
print(len(lst_stu),lst_stu)
set_stu = set(lst_stu)
print(len(set_stu),set_stu)