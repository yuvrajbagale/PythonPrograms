class Student:

    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
        print('Hello My name is:',self.name)
        print('My rollno is:',self.rollno)
        print('My marks is:',self.marks)

s=Student("Yuvraj",100,90)
s.talk()
print('\n')
#self - self is pyhton provided implicit variable always pointing to current object.
#By using self we can access object related variables(instance varibales) and objects releted methods(instance methods)

s2=Student('ravi',102,98)
s2.talk()


