li = [1,2,3,4,5,6]
do_dai_li = len(li)

#độ dài cảu chuổi
print (type(li))
print (len(li))
print("- Độ dài của list li là: " + str(do_dai_li))

#Lấy theo vị trí phần tử trong list
print ("\n- Vị trí thứ 4 của chuổi Li là: " + str(li[4]))
#print ("Vị trí thứ 4 của list Li là: " + str(li[4]))

'Trường hợp vị trí lấy ra ngoài vị trí của list sẽ báo lỗi'

#Nối 2 list lại với nhau:
list1 = [1,3,5,7]
list2 = [2,4,6,8]
list1_2 = list1 + list2
print("\n- Chuổi mới sau khi nối chuổi là")
print(list1_2)

#2 2 list hiện tại
list1_x2 = list1 * 2 
print("\n- List mới sau khi nhân 2 là:")
print(list1_x2)
# cập nhật , thay đổi giá trị theo vị trí cho trước

list4 = [1,2,3,4,6,9 ,4,56,76]
# thay đổi vị 4(giá trị 6 thành 15)
print("\n- Chuổi gốc:")
print(list4)
list4[4]=15
print("\n- Thay đổi vị 4(giá trị 6 thành 15):")
print(list4)

#Lấy các thành phần trong list theo vị trí
print("\n-Lấy các thành phần trong list theo vị trí")
list_lay_giatri = list4[2:6]
print("\t +List lấy ra là:")
print(list_lay_giatri)


