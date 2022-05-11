try:
    x=int(input("Enter the number: "))
    y=int(input("Enter the number: "))
    print(x/y)
except ZeroDivisionError:
    print("Can't Divide with zero")
except ValueError:
    print("Please provide integer value only")
    