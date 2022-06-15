list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
op={}
for i in range(len(list1)):
    for j in range(len(list2)):
        if i==j:
            op[list1[i]]=list2[j]
print(op)