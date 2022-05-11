import os
try:
    print("try")
    os._exit(0)
except NameError:
    print("except")
finally:
    print("finally")