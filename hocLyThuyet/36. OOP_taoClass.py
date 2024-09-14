class Car:
    #thuộc tính (attributes)
    fuel = "Xăng"
    maxspeed = 150
    #Phương thức (methods)
    def drive(self):
        print("Đang đi với tốc độ",self.maxspeed)
    def drive1(self,maxspeed):
        print("Đang đi với tốc đôk",maxspeed)



polo = Car()
print (polo.fuel)
print (polo.drive())
polo.drive()
print (polo)
tuan = Car()
tuan.drive1(300)
print (tuan)