std = {"hs1":"Tuân","hs2":"Teo","hs3":"Tý"}
print (std)

#Đếm số phần tử trong Dic
s = 0
s = len(std)
print (s)
print ("-------------------------------------------------------")

#Xoá một phần tử ở vị trí index
del std["hs2"]
print ("Xoá một phần tử trong Dic: del std['hs2']")
print (std)
print ("-------------------------------------------------------")

#Lấy giá trị của Key
std.keys()
print ("\n-Lấy các key trong Dic: std.keys() ")
print (std.keys())
print ("-------------------------------------------------------")

#Lấy giá trị Value
std.values()
print ("\n-Lấy các Value trong Dic: std.values()")
print (std.values())

#Lấy kEy và value: 
i = std.items()
#Lấy Key và value
print ("\n-Lấy Key vàValue trong Dic: item")
for item in i:
    print (item)
print ("-------------------------------------------------------")
#Lấy Key
print ("\n-Lấy các key trong Dic: item[0] ")
for item in i:
    print (item[0])
print ("-------------------------------------------------------")
#Lấy Value
print ("\n-Lấy các Value trong Dic: item[1]")
for item in i:
    print (item[1])

print ("-------------------------------------------------------")
#Có thể tạo Dci như sau:
print("Có thể tạo Dci như sau: diem = dict(A= 10,B = 7,C =8,D=6)")
diem = dict(A= 10,B = 7,C =8,D=6)
type(diem)
print ("Kết quả: {}".format(diem))
print ("-------------------------------------------------------")

#Sau khi tạo Dic, chuyển thành List
list(diem)
print ("\n-Sau khi tạo Dic, chuyển thành List: list(diem)")
print("Kết quả: {}".format(diem))

print ("-------------------------------------------------------")
#Có thể tạo Dic như sau:
print("Có thể tạo Dic như sau: resuts = {x:x**2 for x in range(10)}")
resuts = {x:x**2 for x in range(10)} #lưu ý: Dic phải có dấu : (x:x); không có dấu : sẽ ra kiểu Set
print("kết quả:{} ".format(resuts))