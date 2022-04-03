from pickletools import TAKEN_FROM_ARGUMENT1


s=input("Enter the given string: ")
print(s[::-1])

s1=input("Enter the string:")
print(''.join(reversed(s1)))

s2 = input('enter the string: ')
i=len(s2)-1
target=''
while i>=0:
    target=target+s2[i]
    i=i-1
print(target)