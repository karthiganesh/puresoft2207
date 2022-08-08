def get_odd(ps1):
    s_out = ''
    for i in range(0,len(ps1)-1,2):
        s_out += ps1[i]
    return s_out

def get_az(ps1):
    return ps1[0] + ps1[-1]

get_AZ = lambda s1,i : s1[i] + s1[(i+1)*-1]

#main starts here
s_name = input("Enter your name")
print('output------')
# print(get_odd(s_name))
# print(get_az(s_name))
for j in range(0,len(s_name)//2):
    print(get_AZ(s_name,j))