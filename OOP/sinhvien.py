class SinhVien:
    def __init__(self, ma_sv, ho_ten, tuoi, que_quan):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.que_quan = que_quan
lst=[]
option = int(input("option: "))
if option == 1:
    n = int(input("Nhap so luong sinh vien: "))
    for i in range(n):
        ma_sv = input("Nhap ma sinh vien: ")
        ho_ten = input("Nhap ho ten: ")
        tuoi = int(input("Nhap tuoi: "))
        que_quan = input("Nhap que quan: ")
        sv = SinhVien(ma_sv, ho_ten, tuoi, que_quan)
        lst.append(sv)
    with open("thongtinSV.txt", "w") as f:
        for sv in lst:
            f.write(f"{sv.ma_sv},{sv.ho_ten},{sv.tuoi},{sv.que_quan}\n")
elif option == 2:
    with open("thongtinSV.txt", "r") as f:
        for line in f:
            ma_sv, ho_ten, tuoi, que_quan = line.strip().split(",")
            if int(tuoi) > 19:
                print(f"{ma_sv}, {ho_ten}, {tuoi}, {que_quan}")

else:
    pass
