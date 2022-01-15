n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
n3=int(input('Enter thread number:'))
if n1>n2 and n1>n3:
    print("Biggest number",n1)
elif n2>n3:
    print("Biggest Number",n2)
else:
    print("Bigesst number",n3)