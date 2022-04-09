class Student:
    '''devoloped by yuvi'''
    def __init__(self):
        self.name="yuvraj"
        self.age=28
        self.mark=80
        
    def talk(self):
        print('hello i am:',self.name)
        print('My age is:',self.age)
        print('My marks is:',self.mark)
        
s=Student()
print(s.name)
print(s.age)
s.talk()