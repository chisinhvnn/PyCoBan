BUFFERSIZE = 250000 #TẠO BIẾN XÁC ĐỊNH DUNG LƯỢNG, SỐ LẦN MỖI LẦN GHI
rFile = open("data/list.txt","r")
wFilie = open("data/Write.txt","w")

buffer = rFile.read(BUFFERSIZE)
i = 0
while (len(buffer) ):
    i = i+1
    wFilie.write(buffer)
    print (i,"{} byte".format(len(buffer)))
    buffer = rFile.read(BUFFERSIZE)
print ("Done")
rFile.close()
wFilie.close()