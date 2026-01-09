import os

class HocSinh:
    def __init__(self, ma_hs, ho_ten, toan, van, anh):
        self.ma_hs = ma_hs
        self.ho_ten = ho_ten
        self.toan = float(toan)
        self.van = float(van)
        self.anh = float(anh)
        # Tính tổng điểm ngay khi khởi tạo hoặc khi đọc file
        self.tong_diem = (self.toan + self.van) * 2 + self.anh
        self.giai_thuong = ""

    def __str__(self):
        return f"{self.ma_hs},{self.ho_ten},{self.toan},{self.van},{self.anh}"

# --- 1. Hàm nhập danh sách học sinh ---
def nhap_danh_sach():
    danh_sach = []
    while True:
        try:
            n_str = input("Nhập số lượng học sinh (n): ")
            n = int(n_str)
            if n > 0: break
            print("Số lượng phải > 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    print("\nLƯU Ý NHẬP LIỆU: Nhập theo cấu trúc: [Mã] [Họ Tên] [Toán] [Văn] [Anh]")
    print("Ví dụ: SV01 Nguyen Van An 8.5 7.0 9.0")
    print("-" * 50)

    for i in range(n):
        while True:
            try:
                line = input(f"Nhập HS thứ {i + 1}: ").strip()
                # Tách chuỗi dựa trên khoảng trắng
                parts = line.split()

                # Kiểm tra phải có ít nhất 5 thành phần (Mã + Tên(ít nhất 1 chữ) + 3 điểm)
                if len(parts) < 5:
                    print("Lỗi: Nhập thiếu thông tin. Vui lòng nhập lại.")
                    continue

                # 1. Lấy 3 phần tử cuối làm điểm
                try:
                    anh = float(parts[-1])
                    van = float(parts[-2])
                    toan = float(parts[-3])
                except ValueError:
                    print("Lỗi: 3 giá trị cuối cùng phải là số (điểm).")
                    continue
                
                # Kiểm tra điểm hợp lệ 0-10
                if not (0 <= toan <= 10 and 0 <= van <= 10 and 0 <= anh <= 10):
                    print("Lỗi: Điểm phải nằm trong khoảng 0-10.")
                    continue

                # 2. Lấy phần tử đầu làm Mã
                ma_hs = parts[0]

                # 3. Lấy các phần tử ở giữa làm Tên (nối lại bằng dấu cách)
                # Cắt từ chỉ số 1 đến chỉ số -3 (không bao gồm -3)
                ho_ten = " ".join(parts[1:-3])

                # Tạo đối tượng và thêm vào danh sách
                hs = HocSinh(ma_hs, ho_ten, toan, van, anh)
                danh_sach.append(hs)
                break # Nhập thành công, thoát vòng lặp while để sang HS tiếp theo

            except Exception as e:
                print(f"Dữ liệu nhập không hợp lệ: {e}. Vui lòng nhập lại.")

    return danh_sach

# --- 2. Ghi file ---
def ghi_file(danh_sach, ten_file="danhsachhs.txt"):
    try:
        with open(ten_file, "w", encoding="utf-8") as f:
            for hs in danh_sach:
                f.write(str(hs) + "\n")
        print(f"\n=> Đã ghi {len(danh_sach)} học sinh vào file {ten_file}")
    except Exception as e:
        print("Lỗi khi ghi file:", e)

# --- 3. Đọc file ---
def doc_file(ten_file="danhsachhs.txt"):
    danh_sach = []
    if not os.path.exists(ten_file):
        print("File không tồn tại!")
        return []
    
    try:
        with open(ten_file, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 5:
                    hs = HocSinh(data[0], data[1], data[2], data[3], data[4])
                    danh_sach.append(hs)
        print(f"=> Đã đọc {len(danh_sach)} học sinh từ file.")
        return danh_sach
    except Exception as e:
        print("Lỗi khi đọc file:", e)
        return []

# --- 4. Logic So sánh (Để dùng trong Insertion Sort) ---
def nho_hon(hs1, hs2):
    """
    Trả về True nếu hs1 'thua' hs2 (cần xếp sau hs2).
    Tiêu chí: Tổng điểm -> Toán -> Văn -> Thứ tự nhập (đã mặc định ổn định).
    """
    if hs1.tong_diem != hs2.tong_diem:
        return hs1.tong_diem < hs2.tong_diem
    if hs1.toan != hs2.toan:
        return hs1.toan < hs2.toan
    if hs1.van != hs2.van:
        return hs1.van < hs2.van
    return False # Nếu bằng hết thì giữ nguyên (ưu tiên thứ tự nhập)

# --- 5. Thuật toán Insertion Sort ---
def insertion_sort_hoc_sinh(danh_sach):
    # Sắp xếp giảm dần theo tiêu chí
    for i in range(1, len(danh_sach)):
        key = danh_sach[i]
        j = i - 1
        
        # Di chuyển các phần tử có rank thấp hơn key về phía sau
        # Logic: Nếu danh_sach[j] < key (theo tiêu chí priority) thì đẩy j xuống
        while j >= 0 and nho_hon(danh_sach[j], key):
            danh_sach[j + 1] = danh_sach[j]
            j -= 1
        danh_sach[j + 1] = key
    return danh_sach

# --- 6. Xếp giải ---
def xep_giai(danh_sach):
    # Quy định số lượng giải
    co_cau = [
        (1, "Giải Đặc Biệt"),
        (2, "Giải Nhất"),
        (4, "Giải Nhì"),
        (6, "Giải Ba"),
        (10, "Giải Khuyến Khích")
    ]
    
    idx = 0
    n = len(danh_sach)
    
    for so_luong, ten_giai in co_cau:
        count = 0
        while count < so_luong and idx < n:
            danh_sach[idx].giai_thuong = ten_giai
            idx += 1
            count += 1
            
    # Những người còn lại không có giải (mặc định string rỗng hoặc ghi chú)
    while idx < n:
        danh_sach[idx].giai_thuong = "Không đạt giải"
        idx += 1

# --- 7. Hàm Main ---
def main():
    # 1. Nhập và Ghi file
    ds_ban_dau = nhap_danh_sach()
    ghi_file(ds_ban_dau)
    
    # 2. Đọc lại từ file để xử lý
    ds_hoc_sinh = doc_file()
    
    if not ds_hoc_sinh:
        return

    # 3. Tìm và in học sinh có điểm cao nhất
    max_diem = -1
    for hs in ds_hoc_sinh:
        if hs.tong_diem > max_diem:
            max_diem = hs.tong_diem
            
    print(f"\n--- HỌC SINH CÓ TỔNG ĐIỂM CAO NHẤT ({max_diem} điểm) ---")
    for hs in ds_hoc_sinh:
        if hs.tong_diem == max_diem:
            print(f"Mã: {hs.ma_hs} - Tên: {hs.ho_ten} - Tổng: {hs.tong_diem}")

    # 4. Sắp xếp Insertion Sort
    insertion_sort_hoc_sinh(ds_hoc_sinh)
    
    # 5. Xếp giải
    xep_giai(ds_hoc_sinh)
    
    # 6. In kết quả cuối cùng
    print("\n" + "="*75)
    print(f"{'MÃ HS':<10} {'HỌ TÊN':<20} {'TỔNG ĐIỂM':<10} {'TOÁN':<6} {'VĂN':<6} {'GIẢI THƯỞNG'}")
    print("="*75)
    for hs in ds_hoc_sinh:
        print(f"{hs.ma_hs:<10} {hs.ho_ten:<20} {hs.tong_diem:<10.2f} {hs.toan:<6} {hs.van:<6} {hs.giai_thuong}")
    print("="*75)

if __name__ == "__main__":
    main()