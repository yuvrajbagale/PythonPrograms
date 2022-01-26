n = int(input("Enter The Number: "))
for i in range(n+1):
    if i>1:
        for k in range(2,i):
            if i%k==0:
                pass
                break
        else:
            print(i)