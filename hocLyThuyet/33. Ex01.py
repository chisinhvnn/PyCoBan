#Bài tập: Đế số ký tự xuất hiện bao nhiêu luần trong list


def countChar(*data):
    dic = {}
    for item in data:
        for i in item:
            i = i.upper()
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
    return dic

kq = countChar("Tuấn","Tèo","Tun")
print(kq)

def myRange(*thamso):
    start = length = step = 0
            