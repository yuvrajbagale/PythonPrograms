#reverse _String
s = input("Enter the some string: ")
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print(target)