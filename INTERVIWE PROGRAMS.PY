#Dignoal 
n=[[10,20,30],[40,50,60],[70,80,99]]
x=0
y=0
for i in range(len(n)):
    x=x+n[i][i]
    y=y+n[len(n)-1-i][i]
print(x)
print(y)      
# x=0
# y=0
# print(n)

# for r in n:
#     print(r)

# for i in range(len(n)):
#     x=x+n[i][i]
#     y=y+n[len(n)-1-i][i]
# print(x)
# print(y)      
  
       
# # n=[1,2,3,4,5,6,8,9,10]
# for i in range(1,10):
#     if i!=n:
#         print(i) 

# def find_missing_number(n):
#     """
#     Find the missing number in a list of numbers.
#     """
#     # Your code here
#     n.sort()
#     for i in range(len(n)):
#         if n[i]!=i+1:
#             return i+1
#     return len(n)+1     

