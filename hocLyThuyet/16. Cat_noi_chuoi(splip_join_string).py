s = "Người đứng đầu Chính phủ Việt Nam chia sẻ vinh dự được phát biểu tại ICWA, nơi nhiều sáng kiến, ý tưởng về đối ngoại của Ấn Độ đã được khởi xướng, đặc biệt tại ngôi nhà Sapru, nơi chứng kiến nhiều sự kiện lịch sử trọng đại. Nổi bật là hội nghị \
    quan hệ châu Á lần thứ nhất năm 1947, đặt nền móng cho sự ra đời của Phong trào không liên kết sau này."
print (s)

# cắt chuổi theo khoản trắng
kq = s.split()
print("kết quả sau khi cắt chuổi với khoảng trắng là: ")
print(kq)


#cắt chuổi dứa vào ký tự biết trước
kq1 = s.split("nhiều")
print("kết quả sau khi cắt chuổi với ký được là")
print(kq1)

# cắt dựa vào ký tự cho trước và số lần cắt chuối 
                    # (đây là ví dụ để cắt từ 1 đến 3 lần)

k = 0
for i in kq:
    if i == "nhiều":
        k=k+1
print(k) 
kq2 = s.split("nhiều", 1)
print("kết quả sau khi cắt chu��i với ký và số lần cắt 1 là")
print(kq2)
kq3 = s.split("nhiều", 2)
print("kết quả sau khi cắt chu��i với ký và số lần cắt 2 là")
print(kq3)

#nối chuối
gop_chuoi=" "
gop_chuoi=gop_chuoi.join(kq)
print("kết quả sau khi gộp chuỗi")
print(gop_chuoi)