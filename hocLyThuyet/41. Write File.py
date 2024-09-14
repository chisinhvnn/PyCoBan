fp = open("data/Write.txt","w")
fp.write("Tuan")
fp.write("\n")
fp.write("Đuc")
fp.write("\n")
fp.write("Vu")
fp.write("\n")
fp.close()

# cpy từ file anyf sang file khác

rFile = open("data/list.txt","w")
wFile = open("data/write.txt","w")
# for line in rFile:
#     print (line,file=wFile,end= "")
for i in range(5500):
    print ("hohohoh bihbibibibibibibibibibibu"*i,file=rFile,end= "")
rFile.close()
wFile.close()