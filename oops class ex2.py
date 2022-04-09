class Student:

    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.marks=mark

    def talk(self):
        print('Hello My name is',self.name)
        print('my age is',self.age)
        print('and my marks is',self.marks)
s1=Student('Yuvraj',28,101)
s1.talk()
print('\n')
s2=Student('Ravi',102,95)
s2.talk()