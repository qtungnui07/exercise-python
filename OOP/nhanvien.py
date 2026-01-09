# --- PHẦN 1: TẠO KHUÔN MẪU (CLASS) ---

class NhanVien:
    def __init__(self, ten, ma_nv):
        # 1. TÍNH ĐÓNG GÓI (Encapsulation)
        # Dùng 2 dấu gạch dưới (__) để bảo vệ dữ liệu, không cho sửa bậy từ bên ngoài
        self.ten = ten
        self.__ma_nv = ma_nv 

    def get_ma_nv(self):
        return self.__ma_nv

    # 2. TÍNH TRỪU TƯỢNG (Abstraction)
    # Đây là hành động chung, nhưng chưa biết tính thế nào (để con tự định nghĩa)
    def tinh_luong(self):
        pass 
    
    def in_thong_tin(self):
        return f"NV: {self.ten} (Mã: {self.__ma_nv})"


# 3. TÍNH KẾ THỪA (Inheritance)
# Class con kế thừa từ class NhanVien
class NhanVienFullTime(NhanVien):
    def __init__(self, ten, ma_nv, luong_cung):
        super().__init__(ten, ma_nv) # Gọi hàm khởi tạo của cha
        self.luong_cung = luong_cung

    # 4. TÍNH ĐA HÌNH (Polymorphism)
    # Cùng tên hàm 'tinh_luong' nhưng cách tính khác (Lương cứng)
    def tinh_luong(self):
        return self.luong_cung


class NhanVienPartTime(NhanVien):
    def __init__(self, ten, ma_nv, so_gio_lam, luong_mot_gio):
        super().__init__(ten, ma_nv)
        self.so_gio_lam = so_gio_lam
        self.luong_mot_gio = luong_mot_gio

    # 4. TÍNH ĐA HÌNH (Polymorphism)
    # Cùng tên hàm 'tinh_luong' nhưng cách tính khác (Giờ * Giá)
    def tinh_luong(self):
        return self.so_gio_lam * self.luong_mot_gio


# --- PHẦN 2: CHƯƠNG TRÌNH QUẢN LÝ (SỬ DỤNG LIST) ---

# Tạo danh sách chứa nhân viên (List quản lý Objects)
cong_ty = []

# Thêm nhân viên vào List
nv1 = NhanVienFullTime("Nguyễn Văn A", "FT001", 10000000) # Lương 10tr
nv2 = NhanVienPartTime("Trần Thị B", "PT002", 50, 200000) # Làm 50h, 200k/h

cong_ty.append(nv1)
cong_ty.append(nv2)

# Duyệt list để tính lương cho cả công ty
print("--- BẢNG LƯƠNG THÁNG ---")
for nv in cong_ty:
    # Ở đây ta không cần quan tâm là FullTime hay PartTime
    # Ta chỉ cần gọi .tinh_luong(), Python tự biết cách tính cho từng người
    tong_luong = nv.tinh_luong()
    print(f"{nv.in_thong_tin()} - Lương nhận: {tong_luong:,} VNĐ")