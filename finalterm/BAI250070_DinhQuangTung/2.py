n=int(input())
if n>0:
    def stt(x):
        if x==0 or x==1:
            return 1
        else:
            return x*stt(x-1)
    print(stt(n))
else:
    print("n phai la so nguyen duong va lon hon 0")

    