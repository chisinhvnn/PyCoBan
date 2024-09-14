li =[]
for item in range(10):
    li.append(item**2)
print(li)
print("\n------------------------------------------------------")

#Cách khác tối ưu
print("Cách khác tối ưu")
li1 = []
li1 = [item**2 for item in range(10)]
print("Cách khác {}".format(li1))
print("\n------------------------------------------------------")

#Lấy số chẵn
print("Lấy số chẵn")
so_chan = []
for item in li1:
    if item %2==0:
        so_chan.append(item)
print("List của số chẵn là:{}".format(so_chan))
print("\n------------------------------------------------------")
#Tối ưu
print("Cách khác tối ưu")
so_chan1 = [item for item in li1 if item %2==0]
print(so_chan1)


print("\n------------------------------------------------------")
#Ví dụ 3
print("Ví dụ 3")
la = [1,2,3]
lb=[2,4,6]
lc = []
for x in la:
    for y in lb:
        lc.append((x,y))
print(lc)
#Tối ưu
print("Cách khác tối ưu")
lc2 = [(x,y) for x in la for y in lb]
print(lc2)
