# Function Aliasing:
# For  the Exiting function we can give another name, which is nothing but fuction alicing
def wish(name):
    print('Hello',name,'Good Morning!!')
wish('yuvraj')
print(id(wish))
greeting=wish
greeting('akshay')
print(id(greeting))
