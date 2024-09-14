fp = open("data/list.txt",'r')
for line in fp:
    print (line,end="")
fp.close()

fp1 = open("data/list.txt",'r')
i = 0
for line in fp1:
    i = i+1
    print (i,line,end="")
fp1.close()
print("Tổng số dòng là:", i)