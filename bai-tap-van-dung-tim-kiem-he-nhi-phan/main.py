import sys

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

log_file = __file__.replace(".py", ".txt")
sys.stdout = Logger(log_file)
sys.stderr = sys.stdout

def bs_asc(a,x):
    l,r=0,len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x:return m
        if a[m]<x:l=m+1
        else:r=m-1
    return -1

def bs_desc(a,x):
    l,r=0,len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x:return m
        if a[m]<x:r=m-1 
        else:l=m+1
    return -1

print("Bai 1")
n=int(input("n="))
# yeu cau nhap tang dan
a=list(map(int,input("nhap mang tang dan: ").split()))
x=int(input("x="))
print(bs_asc(a,x))

print("\nBai 2")
n=int(input("n="))
a=list(map(int,input("nhap mang: ").split()))
# sap xep chon tang dan
for i in range(n-1):
    k=i
    for j in range(i+1,n):
        if a[j]<a[k]:k=j
    a[i],a[k]=a[k],a[i]
print("sorted:",a)
x=int(input("x="))
print(bs_asc(a,x))

print("\nBai 3")
n=int(input("n="))
a=list(map(int,input("nhap mang: ").split()))
# noi bot tang dan
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("sorted:",a)
x=int(input("x="))
print(bs_asc(a,x))

print("\nBai 4")
n=int(input("n="))
a=list(map(int,input("nhap mang: ").split()))
# chen giam dan
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and key>a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print("sorted desc:",a)
x=int(input("x="))
# dung ham tim kiem giam dan
print(bs_desc(a,x))