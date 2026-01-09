class TaiKhoan:
    def __init__(self):
        self.__so_du = 0  # 2 dấu gạch dưới là private (riêng tư)

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"Đã nạp {so_tien}. Số dư mới: {self.__so_du}")
        else:
            print("Số tiền không hợp lệ")

tk = TaiKhoan()
tk.nap_tien(100) 
# print(tk.__so_du) # Lỗi! Bạn không thể truy cập trực tiếp biến private từ bên ngoài.