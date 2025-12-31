m,y=map(int,input("nhap thang, nam duoc cach boi dau cach: ").split())
arr=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if (y%4==0 and y%100!=0) or y%400==0:
    arr[2]=29
    print(f"thang {m} co {arr[m]} ngay`")
else:
    print(f"thang {m} co {arr[m]} ngay`")