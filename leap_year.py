def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
        leap=True
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    
    return leap

year = 1900
print(is_leap(year))