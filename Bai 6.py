print("=============MENU============= "
    ,"\n 1. Câu 1:   "
    ,"\n 2. Câu 2:   "
    ,"\n 3. Câu 3:   "
    ,"\n 4. Câu 4:   "
    ,"\n 5. Câu 5:   "
    ,"\n 0. Thoát")

def c1():
    n = input()
    t = n.lower()
    print(t)
    tb = n.upper()
    print(tb)
    s, ss = 0, 0
    for i in range(0, len(t)):
        if t[i].isdigit(): #đếm số
            s += 1
        elif t[i].isalpha(): #đếm chữ
            ss += 1
    print(s, "  ", ss)
    print(n.count("a"))
    print(n.count("t"))

    a = n.split() #tách n thành array a rồi đếm phần tử
    print(len(a))
def c2():
    def sumi(a, b):
        if a >= 10:  #n vẫn lớn hơn 10, gọi đệ quy với n//10, tổng mới bằng n%10
            return sumi(a // 10, b + a % 10)
        else:
            return b + a #khi n bé hơn 10 cộng lại lần cuối với biến tổng
    n = int(input())
    print(sumi(n, 0)) #khởi tạo với n, tổng bằng 0
def c3():
    def dq(i, t):
        if i <= n: #biến chạy vẫn bé hơn n => gọi lại đệ quy với biến chạy i + 2 ( số lẻ )
            return dq(i + 2, t + i) # biến chạy + 2, biến tổng cộng thêm chính i
        else:
            return t # thỏa mãn i==n rồi thì trả lại tổng
    n = int(input())
    print(dq(1, 0)) #khởi tạo với biến chạy = 1, tổng ban đầu = 0
def c4():
    def ssc(): #sắp xếp chèn
        for i in range(1, len(a)):
            m = a[i]
            j = i - 1
            while j >= 0 and a[j] < m:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = m
            print(a)

    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    print(max(a)) #in phần tử lớn nhất
    ssc()
    v = 0
    for i in range(1, n):
        if a[i] != a[i - 1]: #sau khi sxep a[0] lớn nhất, tìm phần tử thứ hai khác a[0]
            v += 1 # mỗi lần v+1 là 1 phần tử khác phần tử đứng trước
        if v == 2:
            s = a[i] #tìm được số thứ 3 => break
            break
    print(s)
def c5():
    class hoc_sinh:     #tạo class
        def __init__(self, mhs, ht, dt, dv, da, td):
            self.mhs = mhs
            self.ht = ht
            self.dt = dt
            self.dv = dv
            self.da = da
            self.td = td

        def ghi(self): #print thông tin gồm mã học sinh, họ tên, tổng điểm
            print(f"{self.mhs} | {self.ht} : {self.td}")

        def nhap(self): #ghi thông tin vào file input
            fin.write(f"{self.mhs} | {self.ht} | {self.dt} | {self.dv} | {self.da} | {self.dt} | {self.td}\n")

    def sortt(): #sắp xếp chọn
        for i in range(n):
            mint = i
            for j in range(i + 1, n):
                if a[mint].td > a[j].td:
                    mint = j
            a[mint], a[i] = a[i], a[mint]

    fin = open("danhsachhs.txt", "w") # mở để ghi

    n = int(input())
    a = []
    for i in range(n):
        mhs = input()
        ht = input()
        dt = int(input())
        dv = int(input())
        da = int(input())
        td = (dt + dv) * 2 + da #tính tổng điểm => thêm v thuộc class hoc_sinh
        v = hoc_sinh(mhs, ht, dt, dv, da, td)
        a.append(v) #thêm v thành phần tử của array a
        v.nhap() #nhập v vào file input
    sortt()

    a[0].ghi()#in ra phần tử bé nhất ( sau khi sort a[0] bé nhất )
    for i in range(n - 1, 0, -1): #chạy ngược lại tìm phần tử lớn thứ 2
        if a[i].td != a[i - 1].td: #phần tử đầu tiên khác phần tử cuối (lớn nhất) chính là phần tử lớn thứ 3
            v = a[i - 1].td #lưu vào v, break vòng lặp
            break

    for i in range(n):
        if a[i].td == v:
            a[i].ghi() #in ra tất cả học sinh có tổng điểm =v

    fin.close()
try:
    while True:
        n = int(input())
        if n == 0:
            break
        elif n == 1:
            c1()
        elif n == 2:
            c2()
        elif n == 3:
            c3()
        elif n == 4:
            c4()
        else:
            c5()
except ValueError:
    print("khong hop le")


