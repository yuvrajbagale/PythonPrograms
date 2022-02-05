#Nested function
def disp():
    def show():
        print("show functions")
    print("Disp function")
    show()
disp()

#Nested Function with return statment
def disp():
    def show():
        return "show function"
    result = show() + " Disp Function"
    return result
a = disp()
print(a)