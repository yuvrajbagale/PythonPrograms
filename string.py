#Creating String
str1 = 'goood morning'#single quetes
str2 = "Yuvraj"# double quote
str3 = '''Hello Yuvraj  how was your day fine....!!@ ''' #triple quotes
print(str1)
print(str2)
print(str3)
# single and double
str4 = 'hello "yuvraj" good morning, your day is goning'
print(str4)

#Mermory allocation
str5 = "yuvraj"#same address
str6 = "yuvraj"#same address
print(id(str5))
print(id(str6))
str7 = "python"
print(id(str7))

#
str8 = 'yuvraj' # remove grabage collectores
print("str8=", id(str8))
str8 = 'python'
print("str8= ",id(str8))

#INDEX ACCESSING WITH INDEXING
str9 = "yuvraj"
print(str9[0])
print(str9[1])
print(str9[2])
print(str9[3])
print(str9[4])
print(str9[5])

print("Negative indexing")
print(str9[-1])
print(str9[-2])
print(str9[-3])
print(str9[-4])
print(str9[-5])
print(str9[-6])
print(str9[::-1])
print(str9[3:])
print(str9[0:3])

#str9.casefold()
print(str9.casefold())

#str9.upper()
print(str9.upper())

#lower case sring
str10 = "HEY YUVRAJ"
print(str10.lower())


