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
 





# def decor(num):
#     def inner():
#         a = num()
#         add = a + 5
#         return add
#     return inner

# def num(): #enhance function without moadifiction
#     return 10

# num = decor(num)
# print(num())

# def decor(num):
#     def inner():
#         a = num()
#         add = a + 5
#         return add
#     return inner
# @decor
# def num(): #enhance function without moadifiction
#     return 10

# print(num())

def decor1(num1):
    def inner():
        b = num1()
        multi = b * 5
        return multi
    return inner

def decor2(num1):
    def inner():
        c = num1()
        multi = c + 5
        return multi
    return inner

def num1():
    return 10

num1 = decor2(decor1(num1))
print(num1())

def decor1(num1):
    def inner():
        b = num1()
        multi = b * 5
        return multi
    return inner

def decor2(num1):
    def inner():
        c = num1()
        multi = c + 5
        return multi
    return inner
@decor2
@decor1
def num1():
    return 10


print(num1())