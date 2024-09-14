class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("Chào bạn tôi tên là: " , self.name,"tuổi của tôi là: " , self.age)
    
asia = Person("Vũ Anh Tuấn",26)
asia.info()

class Student(Person):
    def __init__(self, name, age,lop ):
        Person.__init__(self, name,age)
        self.lop = lop

    def infoLop(self):
        print("Lop của bạn là: " , self.lop)
hs1 = Student("Nguyen Đại Ca", 28,"9/9")

hs1.infoLop()
hs1.info()

