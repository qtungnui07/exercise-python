def cau1():
    print("Câu 1")
    s=input()
    print(s.lower())
    print(s.upper())
    sum=0
    chars=0
    suma=0
    sumt=0
    for char in s:
        if s.isdigit():
            sum+=1
        if s.isalpha():
            chars+=1
        if char == "a":
            suma+=1
        if char == "t":
            sumt+=1
    print(sum)
    print(chars)
    print(suma)
    print(sumt)
    words=s.split()
    print(len(words))
    
            
def cau2():
    print("Câu 2")
    n=int(input())
    def tongcacchuso(n):
        if n == 0:
            return 0
        else:
            return n % 10 + tongcacchuso(n // 10)
    print(tongcacchuso(n))

def cau3():
    print("Câu 3")
    n=int(input())
    def tongle(n):
        if n<=0:
            return 0
        if n%2!=0:
            return n+tongle(n-2)
        else:
            return tongle(n-1)
    print(tongle(n))
def cau4():
    print("Câu 4")
    arr=list(map(int,input().split()))
    def insertion(arr):
        for i in range(1,len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and key>arr[j]:
                arr[j+1]=arr[j]
                j-=1
                print(arr)
            arr[j+1]=key
    insertion(arr)
    print(*arr)
    for i in range(len(arr)-1):
        m=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[m]:m=j
        arr[i],arr[m]=arr[m],arr[i]
    d=[]
    for x in arr:
        if x not in d:d.append(x)
    if len(d)>=3:
        v=d[2]
        print(v)
        for i in range(len(arr)):
            if arr[i]==v:print(i)
    else:
        print("k du 3 gia tri khac nhau")
def cau5():
    print("Câu 5")
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
def main():
    while True:
        print("MENU".center(30,"="))
        print("1. Câu 1:")
        print("2. Câu 2:")
        print("3. Câu 3:")
        print("4. Câu 4:")
        print("5. Câu 5:")
        print("0. Thoát")
        choice = input("Nhập lựa chọn: ")
        if choice == "1":cau1()
        elif choice == "2":cau2()
        elif choice == "3":cau3()
        elif choice == "4":cau4()
        elif choice == "5":cau5()
        elif choice == "0":break
        else:print("Lựa chọn không hợp lệ!")
main()