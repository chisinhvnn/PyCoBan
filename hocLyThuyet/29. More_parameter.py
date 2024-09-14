def dienthoai(**data):
    tt = 0
    for ten, gia in data.items():
        row ="{:20} {:10}".format(ten,gia)
        print(row)
        tt = tt + gia
    return tt

tinh_tong_tien = dienthoai(Iphone=10000000, Samsung=8000000, Xiaomi=6000000)
print("-"*30)
print("{:20} {:10}".format("Tổng cộng: ",tinh_tong_tien))
print("-"*30)
print("Tính tổng (n1,n2,n3;*data1,**data2)")
print( "t1 = n1 =n2+n3, \nt2= data1, \nt3= data2")
                
'''
Tính tổng (n1,n2,n3;*data1,**data2)
t1 = n1 =n2+n3
t2= data1
t3 = data2
'''

def tinh_tong(n1,n2,n3,*n, **data):
    t1 =t2=t3=0
    t1= n1+n2+n3
    for item in n:
        t2 = t2+item
    for k,v in data.items():
        t3 = t3+v
    t =[t1,t2,t3]
    return t
k3 = tinh_tong(6,9,8,15,26,8,6,3,36,t=50,y = 80,v = 90)
print("Ví du: Tính tổng: (6,9,8,15,26,8,6,3,36,t=50,y = 80,v = 90) là: ",k3)