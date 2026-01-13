import os
class student:
    def __init__(self, idst, name, math, lith, eng):
        self.idst = idst
        self.name = name
        self.math = float(math)
        self.lith = float(lith)
        self.eng = float(eng)
        self.sum3s = (self.math + self.lith) * 2 + self.eng
    def __str__(self):
        return f"{self.idst},{self.name},{self.math},{self.lith},{self.eng}"
def nhap_du_lieu(filename="danhsachhocsinh.txt"):
    try:
        n = int(input("Nhap so luong hs: "))
    except ValueError:
        print("nhap so nguyen")
        return

    with open(filename, "w", encoding="utf-8") as f:
        for i in range(n):
                print(f"hs thu {i+1}")
                idst = input("ma: ")
                name = input("ten: ")
                while True:
                    try:
                        math = float(input("toan: "))
                        if 0 <= math <= 10:
                            break
                        print("0<=x<=10")
                    except ValueError:
                        print("nhap so nguyen so thuc")
                while True:
                    try:
                        lith = float(input("van: "))
                        if 0 <= lith <= 10:
                            break
                        print("0<=x<=10")
                    except ValueError:
                        print("nhap so nguyen so thuc")
                while True:
                    try:
                        eng = float(input("anh: "))
                        if 0 <= eng <= 10:
                            break
                        print("0<=x<=10")
                    except ValueError:
                        print("nhap so nguyen so thuc")
                f.write(f"{idst},{name},{math},{lith},{eng}\n")

def doc_du_lieu(filename="danhsachhocsinh.txt"):
    lst = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                d = line.strip().split(',')
                if len(d) == 5:
                    lst.append(student(d[0], d[1], d[2], d[3], d[4]))
    return lst

def in_danh_sach(lst):
    print(f"{'ma':<10} {'name':<20} {'sum':<10}")
    for s in lst:
        print(f"{s.idst:<10} {s.name:<20} {s.sum3s:<10}")

def timhocsinhdiemthap(lst):
    if not lst: return
    mini = min(s.sum3s for s in lst)
    print(f"tong diem thap nhat")
    for s in lst:
        if s.sum3s == mini:
            print(f"{s.name} - {s.sum3s}")
    print("")
        
def tim_hocsinh_diem_cao_thu_hai(lst):
    if len(lst) < 2:
        print("Khong du hoc sinh de xet diem cao thu hai")
        return
    diem_khac_nhau = sorted({s.sum3s for s in lst}, reverse=True)
    if len(diem_khac_nhau) < 2:
        print("Tat ca hoc sinh co cung tong diem")
        return
    diem_cao_thu_hai = diem_khac_nhau[1]
    print("Hoc sinh co tong diem cao thu hai:")
    for s in lst:
        if s.sum3s == diem_cao_thu_hai:
            print(f"{s.idst:<10} {s.name:<20} {s.sum3s}")
def main():
    FILE_NAME = "danhsachhocsinh.txt"
    nhap_du_lieu(FILE_NAME)
    lst_hoc_sinh = doc_du_lieu(FILE_NAME)
    if not lst_hoc_sinh:
        print("not found")
        return
    in_danh_sach(lst_hoc_sinh)
    timhocsinhdiemthap(lst_hoc_sinh)
    tim_hocsinh_diem_cao_thu_hai(lst_hoc_sinh)
    
if __name__ == "__main__":
    main()