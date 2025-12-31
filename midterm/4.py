a, b=map(int,input("nhap 2 so nguyen duoc cach boi dau cach: ").split())
print("Chọn \n 1 để nhân 2 số \n 2 để chia 2 số \n 3 để cộng 2 số \n 4 để trừ 2 số \n 5 in ra số bé hơn trong 2 số đó ")
n=int(input())
if n==1:print(a*b)
elif n==2:
    if b ==0:
        print("b=0 k hop le")
    else:
        print(a/b)
elif n==3:print(a+b)
elif n==4:print(a-b)
elif n==5:
    if a < b:print(a)
    elif b<a:print(b)
    else:print(f"{a, b} bang nhau")
else:
    print("nhap lai lua chon")
