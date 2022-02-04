#access using loop
#for
str1 = "yuvraj"
n = len(str1)
print(n)
for c in str1:
    print(c)

for i in range(n):
    print(i,"-",str1[i])


#While Loop
str2 = 'Bagale'
n = len(str2)
print(n)
i = 0
while i < n:
    print(i,'-',str2[i])
    i+=1