#kg220728 demo for 'while' loop
c_continue = 'Y'
while c_continue=='Y':
    s_name = input("Enter your name : ")
    print(f"Your name has {len(s_name)} characters\nin Upper case = {s_name.upper()}\n")
    c_continue = input("Continue <Y/N> ?")
