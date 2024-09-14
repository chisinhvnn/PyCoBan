#Dung dữ liệu đọc tới đâu
f = open("data/Write.txt","r")

fpos = f.tell()
print ("Dọc tới vị trí",fpos)

line = f.readline()
print ("Done", end="")
fpos = f.tell()
print ("Dọc tới vị trí",fpos)

line = f.readline()
print ("Done", end="")
fpos = f.tell()
print ("Dọc tới vị trí",fpos)

line = f.readline()
print ("Done", end="")

#(Đọc tới vị trí chỉ định)
print (" ----" *4500)
print ("Đọc tới vị trí chỉ định")
f.seek(0)
print ("'"*50)
data = f.read()
print (len(data))
print (data)

