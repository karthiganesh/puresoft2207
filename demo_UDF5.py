#kg220728 demo for user defined functions
def parse_name(ps_name, pn_pos=0): #function definition
    try:
        s_out1 = ''
        s_out2 = ''
        for i in range(pn_pos,len(ps_name)-1,2):
            s_out1 += ps_name[i]
            s_out2 += ps_name[i+1]
        return (s_out1, s_out2)
    except Exception as e:
        print(f'Error {str(e)}')

#main starts
print("Start of Main function")
s1 = input("Enter a name ")
s_out1 = parse_name(s1)   # calling function parse_name defined in line 4
print(s_out1)
print("Completed.")