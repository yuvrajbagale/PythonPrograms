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

print("+++++++++++++++++++Comma Seprater++++++++++++++++++++++++")
price = 1234567890
print(f"{price:,}")
print("+++++++++++++++++++++Under Score+++++++++++++++++++++++++++++")
print(f"{price:_}")

#variable
name1 = "yuvraj"
age1 = 27
print(f"My Name is {name1} and age is {age1}")

#expreationce
print(f"{10*8}")

a = 50
b = 3
print(f"{a/b:.2f}")

#tuple
value = (10,20)
print(f"{value[0],value[1]}")

#dic
data = {"rahul":200000,"akshay":3000000}
print(f"{data['rahul']:d} {data['akshay']:d}")
