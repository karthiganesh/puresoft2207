#kg220728 demo for user defined functions

def parse_name_odd(ps_name): #function definition
    try:
        s_out = ''
        for i in range(0,len(ps_name),2):
            s_out += ps_name[i]
        print(s_out)
    except Exception as e:
        print(f'Error {str(e)}')

def parse_name_even(ps_name): #function definition
    try:
        s_out = ''
        for i in range(1,len(ps_name),2):
            s_out += ps_name[i]
        print(s_out)
    except Exception as e:
        print(f'Error {str(e)}')


#main starts
print("Start of Main function")
s1 = input("Enter a name ")
parse_name_even(s1)   # calling function parse_name defined in line 4
parse_name_odd(s1)
print("Completed.")