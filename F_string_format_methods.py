# Integer
print("******** Integer ********")
num = 15
print(f"{num}")				# Treated as String becoz no type mention
print(f"{num:d}")
print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")			# Left align
print(f"{num:*<5d}")		# Left align with fill
print(f"{num:*>5d}")		# Right align with fill
print(f"{num:^5d}")			# Center align
print(f"{num:*^5d}")		# Center align with fill

# Float
print("******** Float ********")
num = 15.65
price = 15.65123456789
print(f"{num}")				# Treated as String becoz no type mention
print(f"{num:f}")
print(f"{num:8f}")			# 15.650000
print(f"{price:.20f}")
print(f"{num:8.3f}")
print(f"{num:+8.2f}")
print(f"{num:<8.2f}")		# Left align
print(f"{num:*<8.2f}")		# Left align with fill
print(f"{num:*>8.2f}")		# Right align with fill
print(f"{num:^8.2f}")		# Center align
print(f"{num:*^8.2f}")		# Center align with fill

#String
print("******** String ********")
name = "yuvraj"
print(f"{name}")
print(f"{name:s}")
print(f"{name:8s}")
print(f"{name:<8}")
print(f"{name:*<8}")
print(f"{name:>8}")
print(f"{name:*>8s}")
print(f"{name:^8s}")
print(f"{name:*^8s}")

print("******** Truncating String ********")
name = "yuvrajbagale"
print(f"{name:.3s}")
print(f"{name:8.3s}")
print(f"{name:*<8.3s}")
print(f"{name:>8.3s}")
print(f"{name:*>8.3s}")
print(f"{name:^8.3s}")
print(f"{name:*^8.3s}")

# Thousand Separator
price = 1234567890
print(f"{price:,}")
print(f"{price:_}")

#Variable
name = "Rahul"
age= 62
print(f"My name is {name} and age {age}")

# Expression
print(f"{10*8}")

# Expressing a Percentage
a = 50
b = 3
print(f"{a/b:.2%}")

# Accessing arguments� items
value = (10, 20)
print(f"{value[0]} {value[1]}")

# Format with Dict
data = {'rahul': 2000, 'sonam': 3000}
print(f"{data['rahul']:d} {data['sonam']:d}")

# Calling Function
name= "yuvraj"
print(f"{name}")
print(f"{name.upper()}")

# Using object created from class
#print(f"{obj.name}")

# Curly Braces
print(f"{10}")
print(f"{{10}}")

# Date and Time
from datetime import datetime
today = datetime(2019, 10, 5)
print(f"{today}")
print(f"{today:%d-%b-%Y}")
print(f"{today:%d/%b/%Y}")
print(f"{today:%b/%d/%Y}")
print(f"{today:%b %d, %Y}")

# Datetime Directive https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior

