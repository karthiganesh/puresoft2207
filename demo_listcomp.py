lst_mon = ['jan,31','feb,28','mar,31','apr,30','may,21','jun,30','jul,31','aug,31','sep,30','oct,31','nov,30','dec,31']
print(lst_mon)
lst_31days_mon = []
print("using for")
for mn in lst_mon:
    if "31" in mn:
        lst_31days_mon.append(mn)
print(lst_31days_mon)
print("After list comprehension")
lst_new = [ mn for mn in lst_mon if "31" in mn ]
print(lst_new)