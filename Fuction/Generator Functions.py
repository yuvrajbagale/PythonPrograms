# Generator Function -
# Generator is a function which responsible to generator sqeunce of values.
# We can write generator functions just like ordinary function but it uses yield keyword to return values.
# Generator --> yield --> A Sequence Of Values

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
for x in g:
    print(x)