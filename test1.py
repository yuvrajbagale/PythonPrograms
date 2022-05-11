from posixpath import sep


def even_or_odd(num):
    if num%2==0:
        return "the number {} is Even".format(num)
    else:
        return "the number {} is Odd".format(num)
    
print(even_or_odd(24))
lst=[1,2,3,4,5,6,7,8,9]
print(list(map(even_or_odd,lst)))

