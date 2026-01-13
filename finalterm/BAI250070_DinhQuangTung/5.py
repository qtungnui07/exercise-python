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
def nhap_du_lieu(filename="danhsachsv.txt"):
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

def doc_du_lieu(filename="danhsachsv.txt"):
    lst = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                d = line.strip().split(',')
                if len(d) == 5:
                    lst.append(student(d[0], d[1], d[2], d[3], d[4]))
    return lst

def in_danh_sach(lst):
    print(f"{'ma':<10} {'name':<20} {'toan':<10} {'van':<10} {'anh':<10} {'sum':<10}")
    for s in lst:
        print(f"{s.idst:<10} {s.name:<20} {s.math:<10} {s.lith:<10} {s.eng:<10} {s.sum3s:<10}")

def tim_hoc_sinh_diem_cao_nhat(lst):
    # scores=sorted({s.sum3s} for s in lst,reverse=True)
    maxest=max(s.sum3s for s in lst)
    print("hoc sinh co diem cao nhat la")
    for students in lst:
        if students.sum3s==maxest:
            print(f"{students.name} - {students.sum3s}")
            
            
    
def main():
    FILE_NAME = "danhsachsv.txt"
    nhap_du_lieu(FILE_NAME)
    lst_hoc_sinh = doc_du_lieu(FILE_NAME)
    if not lst_hoc_sinh:
        print("not found")
        return
    in_danh_sach(lst_hoc_sinh)
    tim_hoc_sinh_diem_cao_nhat(lst_hoc_sinh)
    

if __name__ == "__main__":
    main()