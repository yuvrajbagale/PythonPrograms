#Write a Program to Enter Name and Percentage Marks in a Dictionary and Display Information on the Screen
rec={}
n=int(input("Enter number of students:"))
i=1
while i<=n:
    name=input("Enter student name: ")
    marks=input("Enter % of marks of student: ")
    rec[name]=marks
    i=i+1
print("name of students","\t","% of marks")
for x in rec:
    print("\t\t",x,"\t",rec[x])
