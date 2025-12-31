n=int(input())
if n>0:
    if n%3==0:
        print(f"So {n} la so chia het cho 3")
    elif n%3!=0:
        print(f"So {n} la so khong chia het cho 3")
elif n==0:
    print("So 0 la so khong")
else:
    print(f"So {n} la so am")