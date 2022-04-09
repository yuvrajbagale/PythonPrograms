class Student:
    def __init__(self):
        self.name="Yuvraj Bagale."
        self.city="koradgoan."
        self.pincode=414102
    def talk(self):
        print('My Name is:',self.name)
        print('My City is:',self.city)
        print('My are pin code is:',self.pincode)

s=Student()
# print(s.name)
# print(s.city)
# print(s.pincode)
s.talk()
