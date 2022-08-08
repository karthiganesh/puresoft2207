#kg220729 demo for string functions
s_name = input("Enter your name ")
print(s_name.capitalize())
c_repeat = True
while c_repeat:
    n_age = input("Enter Your age")
    if n_age.isnumeric():
        c_repeat=False
    else:
        print("Please enter valid Age as a Number")
print(f"Welcome {s_name}, your age is {n_age.zfill(6)}")
s_days = input("Exercise done on (weekdays separated by comma)")
lst_exd = s_days.split(',')
print(lst_exd)
for x in lst_exd:
    print(x)

