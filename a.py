import os

# --- CLASS CHO CÂU 5 ---
class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb, phu_cap, thuong):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = int(luong_cb)
        self.phu_cap = int(phu_cap)
        self.thuong = int(thuong)

    def tong_thu_nhap(self):
        return self.luong_cb + self.phu_cap + self.thuong

# --- CÁC HÀM GIẢI QUYẾT TỪNG CÂU ---

def cau_1():
    print("\n--- CÂU 1 ---")
    try:
        n = int(input("Nhập số nguyên N: "))

        # 1.2 Kiểm tra chia hết cho 5
        if n % 5 == 0:
            print(f"{n} có chia hết cho 5.")
        else:
            print(f"{n} không chia hết cho 5.")

        # 1.3 In các số chia hết cho 5 <= N
        if n > 0:
            result = [str(i) for i in range(n + 1) if i % 5 == 0]
            print(f"Các số chia hết cho 5 từ 0 đến {n}: {', '.join(result)}")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

def tinh_tong_de_quy(n):
    if n == 1:
        return 1
    return n + tinh_tong_de_quy(n - 1)

def cau_2():
    print("\n--- CÂU 2 ---")
    while True:
        try:
            n = int(input("Nhập số nguyên n (n > 0): "))
            if n > 0:
                break
            print("Vui lòng nhập n > 0.")
        except ValueError:
            print("Lỗi nhập liệu.")

    print(f"Tổng các số nguyên từ 1 đến {n} là: {tinh_tong_de_quy(n)}")

def cau_3():
    print("\n--- CÂU 3 ---")
    s = input("Nhập chuỗi ký tự: ")

    # 3.2 Đếm số ký tự là số
    dem_so = sum(1 for char in s if char.isdigit())
    print(f"Số ký tự là chữ số trong chuỗi: {dem_so}")

    # 3.3 Xóa khoảng trắng và in hoa
    # replace(" ", "") xóa toàn bộ khoảng trắng, upper() viết hoa
    s_moi = s.replace(" ", "").upper()
    print(f"Chuỗi sau khi xử lý: {s_moi}")

def cau_4():
    print("\n--- CÂU 4 ---")
    try:
        n = int(input("Nhập số phần tử của mảng: "))
        arr = []
        tong_am = 0

        print("Nhập các phần tử:")
        for i in range(n):
            val = int(input(f"Phần tử thứ {i}: "))
            arr.append(val)
            if val < 0:
                tong_am += val

        # 4.2 Tổng âm
        print(f"Tổng tất cả các số nguyên âm: {tong_am}")

        # 4.3 Sắp xếp nổi bọt (Bubble Sort) và in các bước
        print("Quá trình sắp xếp nổi bọt (tăng dần):")
        # Copy mảng để không ảnh hưởng dữ liệu gốc nếu cần dùng lại
        sort_arr = arr.copy()

        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if sort_arr[j] > sort_arr[j + 1]:
                    sort_arr[j], sort_arr[j + 1] = sort_arr[j + 1], sort_arr[j]
                    swapped = True

            # In kết quả sau mỗi bước (vòng lặp ngoài)
            print(f"Bước {i + 1}: {sort_arr}")

    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def cau_5():
    print("\n--- CÂU 5 ---")
    filename = "danhsachnv.txt"
    ds_nv = []

    try:
        n = int(input("Nhập số lượng nhân viên: "))

        # 5.2 Nhập thông tin
        for i in range(n):
            print(f"Nhập thông tin NV thứ {i+1}:")
            ma = input("Mã NV: ")
            ten = input("Họ tên: ")
            luong = int(input("Lương cơ bản: "))
            phu = int(input("Phụ cấp: "))
            thuong = int(input("Thưởng: "))
            ds_nv.append(NhanVien(ma, ten, luong, phu, thuong))

        # 5.3 Ghi vào file
        with open(filename, "w", encoding="utf-8") as f:
            for nv in ds_nv:
                # Ghi định dạng: Ma,Ten,Luong,PhuCap,Thuong (cách nhau bởi dấu phẩy hoặc xuống dòng)
                f.write(f"{nv.ma_nv},{nv.ho_ten},{nv.luong_cb},{nv.phu_cap},{nv.thuong}\n")

        print(f"Đã ghi danh sách vào file {filename}")

        # 5.4 Đọc file và tìm max
        if not os.path.exists(filename):
            print("Không tìm thấy file để đọc.")
            return

        ds_doc_duoc = []
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    ds_doc_duoc.append(NhanVien(parts[0], parts[1], parts[2], parts[3], parts[4]))

        if ds_doc_duoc:
            # Tìm nhân viên có tổng thu nhập cao nhất
            # Dùng hàm max với key là method tong_thu_nhap
            nv_best = max(ds_doc_duoc, key=lambda x: x.tong_thu_nhap())

            print("--- NHÂN VIÊN CÓ THU NHẬP CAO NHẤT ---")
            print(f"Mã NV: {nv_best.ma_nv}")
            print(f"Họ tên: {nv_best.ho_ten}")
            print(f"Tổng thu nhập: {nv_best.tong_thu_nhap()}")

    except ValueError:
        print("Lỗi nhập liệu số.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# --- CÂU 6: MENU ---
def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Câu 1 (Số nguyên N)")
        print("2. Câu 2 (Đệ quy tính tổng)")
        print("3. Câu 3 (Xử lý chuỗi)")
        print("4. Câu 4 (Mảng & Bubble Sort)")
        print("5. Câu 5 (Nhân viên & File)")
        print("0. Thoát")
        print("==========================")

        chon = input("Chọn chức năng (0-5): ")

        if chon == '1': cau_1()
        elif chon == '2': cau_2()
        elif chon == '3': cau_3()
        elif chon == '4': cau_4()
        elif chon == '5': cau_5()
        elif chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
