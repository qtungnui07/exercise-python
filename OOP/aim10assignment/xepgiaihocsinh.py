import os

class student:
    def __init__(self,idst,name,math,lith,eng):
        self.idst=idst
        self.name=name
        self.math=float(math)
        self.lith=float(lith)
        self.eng=float(eng)
        self.sum3s=(self.math+self.lith)*2+self.eng
        self.giai="k"

    def __str__(self):
        return f"{self.idst},{self.name},{self.math},{self.lith},{self.eng}"

n=int(input("Nhap so luong hs: "))
with open("info.txt","a",encoding="utf-8") as f:
    for i in range(n):
        print(f"nhap hs thu {i+1}:")
        idst=input("ma: ")
        name=input("ten: ")
        math=float(input("toan: "))
        lith=float(input("van: "))
        eng=float(input("anh: "))
        f.write(f"{idst},{name},{math},{lith},{eng}\n")

lst=[]
if os.path.exists("info.txt"):
    with open("info.txt","r",encoding="utf-8") as f:
        for line in f:
            d=line.strip().split(',')
            if len(d)==5:
                lst.append(student(d[0],d[1],d[2],d[3],d[4]))

if not lst: exit()
# 5.	In ra thông tin học sinh có tổng điểm cao nhất (nếu có nhiều học sinh cùng tổng điểm cao nhất thì in ra tất cả).
mx=max(s.sum3s for s in lst)
print("ds diem cao nhat:")
for s in lst:
    if s.sum3s==mx:
        print(f"{s.name} - {s.sum3s}")

for i in range(1,len(lst)):
    key=lst[i]
    j=i-1
    while j>=0:
        move=False
        if lst[j].sum3s<key.sum3s: 
            move=True
        elif lst[j].sum3s==key.sum3s:
            if lst[j].math<key.math: 
                move=True
            elif lst[j].math==key.math:
                if lst[j].lith<key.lith: 
                    move=True
        if move:
            lst[j+1]=lst[j]
            j-=1
        else: break
    lst[j+1]=key

prizes=[(1,"dac biet"),(2,"nhat"),(4,"nhi"),(6,"ba"),(10,"kk")]
idx=0
for cnt,name in prizes:
    for _ in range(cnt):
        if idx<len(lst):
            lst[idx].giai=name
            idx+=1
        else: break

print(f"{'MA':<10} {'TEN':<20} {'TONG':<10} {'GIAI'}")
for s in lst:
    print(f"{s.idst:<10} {s.name:<20} {s.sum3s:<10} {s.giai}")






# def insertion(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and key>arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
# insertion(arr)
# print(*arr)  