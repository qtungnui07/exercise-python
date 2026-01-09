# class Cho:
#     def keu(self):
#         return "Gâu gâu"

# class Meo:
#     def keu(self):
#         return "Meo meo"

# dong_vat = [Cho(), Meo()]

# for dv in dong_vat:
#     print(dv.keu()) # Cùng gọi hàm keu() nhưng kết quả khác nhau
    
    
    
    
# Khai báo lớp SinhVien
class SinhVien:
    def __init__(self, ma_sv, ho_ten, tuoi, que_quan):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.que_quan = que_quan


ds_sv = []  # Danh sách sinh viên

option = int(input("Nhập lựa chọn (1: Thêm SV, 2: Hiển thị SV 19 tuổi): "))

# ================== OPTION 1 ==================
if option == 1:
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\nSinh viên {i + 1}:")
        ma_sv = input("Nhập mã sinh viên: ")
        ho_ten = input("Nhập họ tên: ")
        tuoi = int(input("Nhập tuổi: "))
        que_quan = input("Nhập quê quán: ")

        sv = SinhVien(ma_sv, ho_ten, tuoi, que_quan)
        ds_sv.append(sv)

    # Lưu vào file
    with open("thongtinSV.txt", "w", encoding="utf-8") as f:
        for sv in ds_sv:
            f.write(f"{sv.ma_sv},{sv.ho_ten},{sv.tuoi},{sv.que_quan}\n")

    print("\n✅ Đã lưu thông tin sinh viên vào thongtinSV.txt")


# ================== OPTION 2 ==================
elif option == 2:
    print("\n📌 Danh sách sinh viên 19 tuổi:")
    with open("thongtinSV.txt", "r", encoding="utf-8") as f:
        for line in f:
            ma_sv, ho_ten, tuoi, que_quan = line.strip().split(",")
            if int(tuoi) == 19:
                print(f"Mã SV: {ma_sv} | Họ tên: {ho_ten} | Tuổi: {tuoi} | Quê quán: {que_quan}")

else:
    print("❌ Lựa chọn không hợp lệ")
