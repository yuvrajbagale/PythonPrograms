#Nested if else statment in python
a = 5
b = 2
c = 6
d = 3
if a>b:
    print("a is greater than b")
    if c>d:
        print("c is greater than d")
    else:
        print("d is greater than c")
else:
    print("b is greater than a")
print("Rest of the Code")