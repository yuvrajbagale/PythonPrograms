# a-z
# 0-9
# . _ time 1
# @ time 1
# . 2,3
#email validaion Program using regex
#yuvraj@gmail.com
import re
email_conditons="^[a-z]+[\._]?[a-z 0-9]+[@]\w[.]\w{2,3}$"
user_email=input('enter Your email: ')
if re.search(email_conditons,user_email):
    print("\n Right Email")
else:
    print("\n Wrong Email")