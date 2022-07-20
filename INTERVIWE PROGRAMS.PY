#Dignoal 
n=[[10,20,30],[40,50,60],[70,80,99]]
x=0
y=0
# print(n)

# for r in n:
#     print(r)

for i in range(len(n)):
    x=x+n[i][i]
    y=y+n[len(n)-1-i][i]
print(x)
print(y)      
  
       
n=[1,2,3,4,5,6,8,9,10]
for i in range(1,10):
    if i!=n:
        print(i)    