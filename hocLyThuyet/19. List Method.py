ls = ["a","b","r",1,2,5,1,6,8,9,2,4,2,5,2]
# thêm một phần từ vào cuối list
print(ls)
ls1=[]
ls.append(9 ) # chỉ được thêm vào 1 phần từ

print("\n-Thêm một phần từ '9' vào cuối list ")
print(ls)
print(ls1)
print("\n---------------------------------------------------------------")
#Thêm vào một vị trí chỉ định
print("\n-Giá trị trước khi thêm vào")
print(ls)
ls.insert(2,1)
print("-Thêm vào vị trí thứ 2 số 1:")
print("Giá trị sau khi thêm vào")
print(ls)
print("\n---------------------------------------------------------------")
#Xoá 1 phần tử một vị trí chỉ định
print("\n-Giá trị trước khi xoá")
print(ls)
ls.pop(3)
print("-Xoá phần tử tại vị trí thứ 3:")
print("Giá trị sau khi thêm vào")
print(ls)
print("\n---------------------------------------------------------------")
#Đếm số lần xuất hiện của phần tử
print("\n-Đếm số lần xuất hiện của phần tử 2")

ls.count(2)

print("Số lần xuất hiện của 2 là: {}".format(ls.count(2)))