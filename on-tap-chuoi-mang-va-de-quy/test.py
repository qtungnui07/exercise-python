def fib(n):
    if n<=1: return n
    return fib(n-1)+fib(n-2)

def tcs(n):
    if n<10: return n
    return n%10+tcs(n//10)

def tongChusole(n):
    if n==0: return 0
    d=n%10
    if d%2!=0: return d+tongChusole(n//10)
    return tongChusole(n//10)

def tday(n):
    if n<=0: return 0
    if n%2!=0: return n+tday(n-2)
    return tday(n-1)
    
    
# n=int(input("n="))
# a=[]
# for i in range(n):
#     a.append(int(input()))
# s=0
# for x in a:
#     if x%5==0:
#         s+=xn=int(input("n="))
# a=[]
# for i in range(n):
#     a.append(float(input()))
# s=0
# d=0
# for x in a:
#     if x<0:
#         s+=x
#         d+=1
# if d>0:
#     print(s/d)
# else:
#     print(0)
n=int(input())
a=list(map(int,input().split()))
if len(a)==n:
    for i in range(n-1):
        m=i
        for j in range(i+1,n):
            if a[j]>a[m]:m=j
        a[i],a[m]=a[m],a[i]
    d=[]
    for x in a:
        if x not in d:d.append(x)
    if len(d)>=3:
        v=d[2]
        print(v)
        for i in range(n):
            if a[i]==v:print(i)
    else:
        print("k du 3 gia tri khac nhau")