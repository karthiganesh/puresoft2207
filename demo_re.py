import re
s1 = 'aaaaa  fla ksdjf 3429323531  lasdkfjas fla ksdjf asfas f aaaaa@email.com laskdjf alskdfj  bbbb@email.com sdkfasjdkfsa 3234329343'
s2 = 'bbbbbbbbbb lksjdflkasf s 2228889991  lasdkfjas fla 1111-444-5555 ksdjf asfas f bbbbba@email.com laskdjf alskdfj  cccccc@email.com sdkfasjdkfsa 2233887744'
#identify name , phone and email id from the above text
re_result = re.search('\d+',s1)
if re_result == None:
    print("Phone number not found")
else:
    print("Phone number found")
print(re.findall('\d+',s1))
print(re.findall('\d\d\d\d-\d\d\d-\d\d\d\d',s2))
print(re.findall('\w+@\w+.com',s2))