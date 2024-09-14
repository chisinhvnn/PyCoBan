name ="Vũ Quốc Tuấn"
old  = "26"
s = "Tôi tên là: " + name + " và tuổi của tôi: " + old
print(s)

#cách viết theo kiểu format
s_format = "Tôi tên là: {} và tuổi của tôi là : {}".format("Vũ Quốc Tuấn","26")
print("kết quả sau khi dùng thuộc tính format:")
print(s_format)
#hoạc 
s_format1 = "Tôi tên là: {0} và tuổi của tôi là : {1}".format("Vũ Quốc Tuấn","26")
print("\n kết quả sau khi dùng thuộc tính format 1:")
print(s_format1)
#hoạc 
s_format2 = "Tôi tên là: {0} và tuổi của tôi là : {1}".format(name,old)
print("\n kết quả sau khi dùng thuộc tính format 2:")
print(s_format2)
#hoạc 
s_format3 = "tuổi của tôi là : {1} và tôi tên là: {0} ".format(name,old)
print("\n kết quả sau khi dùng thuộc tính format 3:")
print(s_format3)

#Khi dùng với list, tuple
ds = ["Cơm tấm","Bún bò", "Xôi"]
mm = "Các món ăn tại nhà hàn của chúng tôi là: {2}; {0}; {1}".format(*ds)  #lưu ý: Phải có dấu * trước ds
print("\n Kết quả khi kết hợp với list")
print(mm)

print("\n @@@@@@@@@@@@@@@@một số kiểu format".upper()) #

tt = "HOC ONLINE"

chuoi = '{:<20}'.format(tt)
print("Kết quả là: " + chuoi)

chuoi1 = '{:-<20}'.format(tt)
print("\nVới chuỗi HOC ONLINE:\n Kết quả khi dùng cú pháp:\n '{':-<20'}'.format(tt):    " + chuoi1)
chuoi3 = '{:->20}'.format(tt)
print("\nVới chuỗi HOC ONLINE:\n Kết quả khi dùng cú pháp:\n '{':->20'}'.format(tt):    "  + chuoi3)
chuoi4 = '{:@>20}'.format(tt)
print("\nVới chuỗi HOC ONLINE:\n Kết quả khi dùng cú pháp:\n '{':@<20'}'.format(tt):    "  + chuoi4)
chuoi5 = '{:-^20}'.format(tt)
print("\nVới chuỗi HOC ONLINE:\n Kết quả khi dùng cú pháp:\n '{':-^20'}'.format(tt):    " + chuoi5)
chuoi6 = '{:^20}'.format(tt)
print("\nVới chuỗi HOC ONLINE:\n Kết quả khi dùng cú pháp:\n '{':^20'}'.format(tt):    " + chuoi6)

#lưu ý khi truyền số vào hàm format

s = "Số thứ tự : {0:d}".format(12)  #d chính là diceme

#format định dạng số 
price = 2000000
print("{:,}".format(price))
print("{:'.'}".format(price))