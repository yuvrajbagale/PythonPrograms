class Student:

    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
        # print('My name is ',self.name)

    def talk(self):
        print('My Name Is a:',self.name)
        print('And My rollno is:',self.rollno)
        print('marks is:',self.marks)

s1=Student('yuvraj',100,60)
s1.talk()