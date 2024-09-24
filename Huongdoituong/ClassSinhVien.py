class sinhvien():
    def __init__(self, MaSv,ten,quequan ) -> None:
        self.MaSV= MaSv
        self.ten = ten
        self.quequan = quequan

sv1 = sinhvien("MS001", "Hoa", "ha tinh")
sv2 = sinhvien("MS002","Binh", "Hue")
sv3 = sinhvien("MS003","Lan", "Da nang")

print("ten sinh vien 1: {} quen quan {}".format(sv1.ten, sv1.quequan))
print("Que quan cua 3 sinh vien la: {}, {}, {}".format(sv1.quequan,sv2.quequan,sv3.quequan))




  


