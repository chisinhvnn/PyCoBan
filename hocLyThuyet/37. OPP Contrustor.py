class Student:
    def __init__(self, name, age) :
        print( "name: ", name,"Tuổi: ",age)
    def __str__(self) :
        return ("----------------------------------")
tuan = Student("Vũa Quốc Tuấn",26)
print (tuan)


