#KG220727 Check the strength of password
class CheckPassword():
    def run(self):
        s_pwd = input("Enter your password")
        n_has_more=1
        if len(s_pwd)<8:
            n_has_more=0
        n_has_lower=0
        n_has_special=0
        for x in s_pwd:
            if not x.isalnum():
                n_has_special=1
            if x.islower():
                n_has_lower=1
        n_strong=1
        if (n_has_more==0):
            print("Less than 8 character")
            n_strong=0
        if (n_has_lower==0):
            print("No lower case")
            n_strong=0
        if (n_has_special==0):
            print("No special characters")
            n_strong=0
        if n_strong==1:
            print("Strong password")
        else:
            print("Weak password")

#main starts here
if __name__ == "__main__":
    o_pc = CheckPassword()
    o_pc.run()