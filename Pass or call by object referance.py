# def val(lst):
#     print("IFBA:", lst, id(lst))
#     lst.append(4)
#     print("IFAA:", lst, id(lst))
    
# lst = [1, 2, 3]
# print("BCF:", lst, id(lst))
# val(lst)
# print("ACF:", lst, id(lst))

#
def val(list1):
    print("IFBA:",list1, id(list1))
    list1=[11,22,33]
    print("IFAA:", list1, id(list1))
    
list1=[1,2,3]
print("BCF:", list1,id(list1))
val(list1)
print("ACF:", list1, id(list1))
