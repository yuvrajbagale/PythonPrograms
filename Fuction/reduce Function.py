# Reduce function
# Reduce() function reduces sequence of elements into a single elements by applying the specified function.
# Reduce(function,sequnece)
# Reduce() function presentin functions module and hence we should write important statement

from functools import*
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)

# Eg1
result1 = reduce(lambda x,y:x*y,l)
print(result1)

# Eg2.
from functools import *
result2=reduce(lambda x,y:x+y,range(1,101))
print(result2)

