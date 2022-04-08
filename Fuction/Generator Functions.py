# Generation Function:

# Generator is a Function which is responsible to generate a sequrence of values.
# We Can write generator function just like ordinary function, but it uses yaild keyworld to return values.
# yield <-- generator function --> A Sequence of Values

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

