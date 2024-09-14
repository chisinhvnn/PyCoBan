#Baif 1: Viết một vòng lặp chạy từ 1 đến 100 và chia thành 10 dòng
print ("In kết quả bài 1 \n")
for i in range(1,101):
    print(i, end=" ")
    if i % 10 == 0:
        print("")
#Bài 2: Viết 1 vòng lặp từ 0 đến 200, chỉ in ra số chẵn. Xây dựng thành 10 dòng và ắp xếp thành các cột thẳng hàng        
#Cách 1
print("\n In bài 2 \n")

for i in range(1,201):
    if i % 2 == 0:
        print("{:>3}".format(str(i)), end=" ")
        if i % 20 == 0:
            print(" ")
#bai 3: Xây dựng hàm kiểm tra số nguyên tố, nếu là số nguyên tố thì True, khong trả về False

def soNguyeto(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(soNguyeto(20))
def songuyento2(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
print(songuyento2(45))
print(songuyento2(47))

#Bài 4: Xây dựng hàm chạy từ 1 đên 1000 và in ra các số nguyên tôn và xuất ra các cột đèu nhau
print("Bài 4")
dem = 0
for i in range(1,1001):
    
    if i>=2:
        if songuyento2(i)==True:
            dem += 1
            print("{:>3}".format(str(i)), end="  ")
            if dem % 10 == 0:
                print(" ")
# Bài 5. Viết hàm chuyển đổi đội F sang độ C
print("Bài 5")
def chuyendoiCsangF(t):
    return (t * 1.8) + 32
def chuyendoiFsangC(f):
    return (f - 32)/ 1.8 

print("32 độc C chuyển qua độ F là:" + str(chuyendoiCsangF(32)))
print("45 độc F chuyển qua độ C là:" + str(chuyendoiFsangC(45)))

#Bài 7. Viết hàm chuyển đổi 1 list Km sang M
km =[10,20,30,40,50]


for k in km:
    m = k * 1000
    print("{} Km chuyển đổi thành M là: {:,}".format(k,m))

#bài 8: Áp dụng tính chất đệ quy để xây dựng giai thừa
def giaithua(n):
    if n<1:
        return 
    else:
        for i in range(1,n):
            n=n*i
        return n
print(giaithua(5))
print(giaithua(1))
print(giaithua(0))
print(1*2*3*4*5)