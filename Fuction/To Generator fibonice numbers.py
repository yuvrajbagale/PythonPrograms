#fibonnace serires
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=fib()
for x in f:
    if x>10:
        break
    print(x)