#pass a function as parameters
def disp(sh):
    print("disp function " + sh())
def show():
    return "show fuction"

disp(show)