n1 = int(input('Enter 1st No: '))
n2 = int(input('Enter 2st No: '))
n3 = int(input('Enter 3st No: '))
if n1<n2 and n2<n3:
    print('samllest Number',n1)
elif n2<n3:
    print('smallest Number',n2)
else:
    print('smallest number',n3)