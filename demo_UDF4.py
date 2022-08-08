#kg220728 demo for user defined functions

def parse_name(ps_name, pn_pos=0): #function definition
    try:
        s_out = ''
        for i in range(pn_pos,len(ps_name),2):
            s_out += ps_name[i]
        return s_out
    except Exception as e:
        print(f'Error {str(e)}')

#main starts
print("Start of Main function")
s1 = input("Enter a name ")
s_out1 = parse_name(s1)   # calling function parse_name defined in line 4
s_out2 = parse_name(s1,1)
print(s_out1, s_out2)
print("Completed.")