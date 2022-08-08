#kg220728 demo for 'for' loop
# for i in range(0,50,5):
#     print(f'{i:2.0f} x 4 = {i*4:3.0f}')

# n_tbl = int(input('Table for ? '))
# n_count = int(input("Table rows ? "))
# for i in range(1,n_count):
#     print(f'{i:2.0f} x {n_tbl:2d} = {i*n_tbl:3.0f}')

s_name = input("Enter your name : ")
print("Your name split by character")
for x in s_name:
    if x == 'a' or x=='i' or x=='o' or x=='u' or x=='e':
        break
    print(x.upper())
else:
    print("Completed")