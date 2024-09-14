#Ví dụ: clip bài 28 lt tu Zổ den Hẻo

def tong (*data):
    t = 0
    for item in data:
        t = t + item
    return t

ketqua = tong(20)
print ("Kết quả là: ", ketqua)

ketqua1 = tong(10,30,50)
print ("Kết quả là: ", ketqua1)

#ví dụ tính các tỏng trong list ([50,32,85,90],[45,69,15,36,],[-15,69,-25,63])

def tong1(*data):
    kq =[]
    for item in data:
        t = 0
        for i in item:
            t= t+i
        kq.append(t)
    return kq

kq2 = tong1([50,32,85,90],[45,69,15,36,],[-15,69,-25,63])
print("Tổng kết quả trong list là: ", kq2)

