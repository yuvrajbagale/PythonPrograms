l1=[(1,2,3)]
l2=([1,2,3,[4,5],6])
l2.append(7)
l2[3].append(6)
l2[3][1] = 'akshay'
l2[3][2] = 'Bagale'
#del l2[3][0]
l2[3].remove(4)
print(l2)
l1.append(4)
l1.extend([4,5,6])
del l1[1]
print(l1)