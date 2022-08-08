#KG220726 Demo for Marksheet program
class Student():
    def run(self):
        try:
            s_regno = input("Enter Regn No ")
            s_name = input("Enter Student Name ")
            n_sub1 = int(input("Enter Subject 1 "))
            n_sub2 = int(input("Enter Subject 2 "))
            n_sub3 = int(input("Enter Subject 3 "))
            n_sub4 = int(input("Enter Subject 4 "))
            n_sub5 = int(input("Enter Subject 5 "))
            n_total = n_sub1 + n_sub2 + n_sub3 + n_sub4 + n_sub5
            s_result='Pass'            
            if n_sub1 < 40 or n_sub2<40 or n_sub3<40 or n_sub4<40 or n_sub5<40 :
                s_result='Fail'
            print(f"Total = {n_total:3.0f}\nResult={s_result}")
            # print("Total=",n_total)
            # print("Result=",s_result)
            print("Completed Successfully.")
        except Exception as e15:
            print(f'Error {str(e15)}')

#main starts here
if __name__ == "__main__":
    o_stu1 = Student()
    o_stu1.run()