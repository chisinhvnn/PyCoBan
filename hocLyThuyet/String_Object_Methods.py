name = "vu quoc tuan  *    "
#In chữ chữ cái viét hoa đầu tiên trong chuỗi
print ("Viết chữ đầu tien in hoa: " + name.capitalize())

#In hoa toàn bộ chữ cái viét hoa
print ("In hoa toàn bộ chữ cái viét hoa: "+ name.upper())
 
# in toàn bộ chữ in thường
print ("in toàn bộ chữ in thường: " + name.lower())

#Chuyển chữ hoa thành thường, chữ thường thành hoa
print ("Chuyển chữ hoa thành thuonng và ngược lại: " + name.swapcase())
#Thêm vào chuỗi ký tự * sao cho độ dài chuỗi bằng 20 (bao gồm ký tự gốc)
print ("Thêm vào cuối cùng chuỗi ký tự 8 sao cho độ dài chuỗi bằng 20 (bao gồm ký tự gốc); " + name.ljust(20,"8"))
print (len(name.ljust(20, "8")))
print ("Thêm vào đầu tiên chuỗi ký tự 8 sao cho độ dài chuỗi bằng 20 (bao gồm ký tự gốc); " + name.rjust(20,"8"))
print (len(name.rjust(20, "8")))
#Huỷ bỏ khoản trắng bên trái
print("Huỷ bỏ khoản trắng bên trái: "+name.lstrip())
print ("Kiểm tra kết quả (so sánh độ dài chuỗi gốc)")
print (len(name))
print (len(name.lstrip()))
print ("Xoá ký tự bên trái cuối cùng cho trước; kết quả: " + name.lstrip("*") + " so sánh Chuỗi gốc: " + name)

#Huỷ bỏ khoản trắng bên phải
name1 ="  *   học    bài đi   "
print("Huỷ bỏ khoản trắng bên phải: "+name.rstrip() )
print ("Kiểm tra kết quả (so sánh độ dài chuỗi gốc)")
print (len(name1))
print (len(name1.rstrip()))
print ("Xoá ký tự bên trái cuối cùng cho trước; kết quả: " + name.rstrip("*") + "so sánh Chuỗi gốc: " + name1)


#Xoá khoản trăng 2 đầu
print("Xoá khoangr trắng: " +name1.strip() + "so sánh chuỗi gốc: "  + name1 + name1) 