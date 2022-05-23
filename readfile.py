file = open('file.txt', 'r')
f = file.readlines()
print(f)

newList=[]
for line in f:
    if line[:-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)

print(newList)

newList1 = []
for line in f:
    newList1.append(line.strip())
print(newList1)    