# Genarater To first n number

def firstn(num):
    n=1
    while n <=num:
        yield n
        n+=1
values =firstn(7)
for x in values:
    print(x)

# We can covertor Generator to list as follows
values=firstn(5)
l1=list(values)
print(l1)