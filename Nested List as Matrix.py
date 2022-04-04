#Nested List as Matrix - in python we can represent matrix by Using nexted lists.
from traceback import print_tb


n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("Enter Row wise")
for x in n:
    print(x)
    
print("Elements by Matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end='')
    print()