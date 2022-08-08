#kg220728 demo for user defined functions

def parse_name(ps_name):
    for i in range(0,len(ps_name),2):
        print(ps_name[i])

#main starts
if __name__ == '__main__':
    print("Start of Main function")
    s1 = input("Enter a name ")
    parse_name(s1)   # calling function parse_name defined in line 4
    print("Completed.")