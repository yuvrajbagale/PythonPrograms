# def decor(fun):
#     def inner():
#         print("if: before enhancing function")
#         fun()
#         print("if: after enhancig function")
#     return inner

# def num():
#     print("We will use this function")
#     print("and will enhance this in decoraotrs")

# result_fun = decor(num)
# result_fun()
 






def decor(fun):
    def inner():
        a = fun()
        add = a + 5
        return add
    return inner

def num1():
    return 10   

result_fun = decor(num1)
print(result_fun)