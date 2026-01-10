import os
class student:
    def __init__(self, idst, name, math, lith, eng):
        self.idst = idst
        self.name = name
        self.math = float(math)
        self.lith = float(lith)
        self.eng = float(eng)
        self.sum3s = (self.math + self.lith) * 2 + self.eng
        self.giai = "k"
    def __str__(self):
        return f"{self.idst},{self.name},{self.math},{self.lith},{self.eng}"
def nhap_du_lieu(filename="info.txt"):
    try:
        n = int(input("Nhap so luong hs: "))
    except ValueError:
        print("nhap so nguyen")
        return

    with open(filename, "w", encoding="utf-8") as f:
        # for i in range(n):
        #     print(f"--- Nhap hs thu {i+1} ---")
        #     idst = input("ma: ")
        #     name = input("ten: ")
        #     math = float(input("toan: "))
        #     lith = float(input("van: "))
        #     eng = float(input("anh: "))
        #     f.write(f"{idst},{name},{math},{lith},{eng}\n")
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

def doc_du_lieu(filename="info.txt"):
    lst = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                d = line.strip().split(',')
                if len(d) == 5:
                    lst.append(student(d[0], d[1], d[2], d[3], d[4]))
    return lst

def in_danh_sach(lst):
    print("-" * 60)
    print(f"{'ma':<10} {'name':<20} {'sum':<10} {'giai'}")
    for s in lst:
        print(f"{s.idst:<10} {s.name:<20} {s.sum3s:<10} {s.giai}")

def tim_max_diem(lst):
    if not lst: return
    
    mx = max(s.sum3s for s in lst)
    print(f"thu khoa")
    for s in lst:
        if s.sum3s == mx:
            print(f"{s.name} - {s.sum3s}")
    print("")

def sap_xep_hoc_sinh(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0:
            move = False
            if lst[j].sum3s < key.sum3s: 
                move = True
            elif lst[j].sum3s == key.sum3s:
                if lst[j].math < key.math: 
                    move = True
                elif lst[j].math == key.math:
                    if lst[j].lith < key.lith: 
                        move = True
            if move:
                lst[j+1] = lst[j]
                j -= 1
            else:
                break
        lst[j+1] = key

def xep_loai_giai(lst):
    prizes = [(1, "dac biet"), (2, "nhat"), (4, "nhi"), (6, "ba"), (10, "kk")]
    idx = 0
    for cnt, name in prizes:
        for _ in range(cnt):
            if idx < len(lst):
                lst[idx].giai = name
                idx += 1
            else:
                return
def main():
    FILE_NAME = "info.txt"
    nhap_du_lieu(FILE_NAME)
    lst_hoc_sinh = doc_du_lieu(FILE_NAME)
    if not lst_hoc_sinh:
        print("not found")
        return
    tim_max_diem(lst_hoc_sinh)
    sap_xep_hoc_sinh(lst_hoc_sinh)
    xep_loai_giai(lst_hoc_sinh)
    in_danh_sach(lst_hoc_sinh)
if __name__ == "__main__":
    main()