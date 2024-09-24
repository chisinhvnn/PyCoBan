class dangNhap:
    def __init__(self,username,password) :
        self.username = username
        self.password = password
    def login(self, username, password):
        if self.username == username and self.password ==password:
            return "Đăng nhập thành công"
        else:
            return "tên đăng nhập hoặc mật khẩu không đúng"