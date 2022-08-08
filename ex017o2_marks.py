#KG220726 Demo for Marksheet program
s_school_name = 'National Public School, New Delhi'
class Staff():
    def __init__(self,ps_name,ps_job):   #self is equivalent to this in java/c++
        self.s_name = ps_name
        self.s_job = ps_job

    def show(self):
        print("Staff Data")
        print(f"Name={self.s_name}\nJob={self.s_job}")

class Student():
    def __init__(self,ps_rg='', ps_nm='', pn_s1=0, pn_s2=0, pn_s3=0, pn_s4=0, pn_s5=0):   #constructors
        self.s_regno = ps_rg
        self.s_name = ps_nm
        self.n_sub1 = pn_s1
        self.n_sub2 = pn_s2
        self.n_sub3 = pn_s3
        self.n_sub4 = pn_s4
        self.n_sub5 = pn_s5

    def input(self):
        self.s_regno = input("Enter Regn No ")
        self.s_name = input("Enter Student Name ")
        self.n_sub1 = int(input("Enter Subject 1 "))
        self.n_sub2 = int(input("Enter Subject 2 "))
        self.n_sub3 = int(input("Enter Subject 3 "))
        self.n_sub4 = int(input("Enter Subject 4 "))
        self.n_sub5 = int(input("Enter Subject 5 "))

    def show(self):
        global s_school_name
        n_total = self.n_sub1 + self.n_sub2 + self.n_sub3 + self.n_sub4 + self.n_sub5
        s_result='Pass'            
        if self.n_sub1 < 40 or self.n_sub2<40 or self.n_sub3<40 or self.n_sub4<40 or self.n_sub5<40 :
            s_result='Fail'
        print("------------Student Marksheet-----------------------")
        print(f'School : {s_school_name}')
        print(f"Name : {self.s_name}\t\tReg.No : {self.s_regno}")
        print('====================================================')
        print(f"Sub 1 : {self.n_sub1}")
        print(f"Sub 2 : {self.n_sub2}")
        print(f"Sub 3 : {self.n_sub3}")
        print(f"Sub 4 : {self.n_sub4}")
        print(f"Sub 5 : {self.n_sub5}")
        print('====================================================')
        print(f"Total = {n_total:6.2f}\t\tResult = {s_result}")
        print('====================================================')

#main starts here
if __name__ == "__main__":
    try:
        o_stu1 = Student('111','aaaa',11,12,13,14,15)   #calls the __init__ method in class
        o_stu1.show()
        o_stu2 = Student('222','bbbbb',41,42,43,44,45)
        o_stu2.show()
        o_stu3 = Student('333','CCCCC',54,65,76,87,56)
        o_stu3.show()
        o_stu4 = Student('444')  #instantiating an object
        n_age = 35  #initializing variable
        o_stu4.input()
        o_stu4.show()
        o_stf1 = Staff("Maruthi", "Principal")
        o_stf1.show()
        print("Completed Successfully.")
    except Exception as e43:
        print(f'Error {str(e43)}')

