class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def display(self):
        print('Employee No',self.eno)
        print('Employee Name',self.ename)
        print('Employee sal',self.esal)
        print('Employee Address',self.eaddr)
        print()
e1=Employee(1,'Sunny',10000,'hydrabad')
e2=Employee(2,'Sammy',20000,'mumbai')
e3=Employee(3,'Sun',300000,'pune')
e1.display()
e2.display()
e3.display()