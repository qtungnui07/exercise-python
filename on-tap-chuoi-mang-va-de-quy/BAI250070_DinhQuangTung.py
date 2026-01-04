def fib(n):
    if n<=1:return n
    return fib(n-1)+fib(n-2)

def tcs(n):
    if n<10:return n
    return n%10+tcs(n//10)

def tongChusole(n):
    if n==0:return 0
    d=n%10
    if d%2!=0:return d+tongChusole(n//10)
    return tongChusole(n//10)

def tday(n):
    if n<=0:return 0
    if n%2!=0:return n+tday(n-2)
    return tday(n-1)

print("mang")

print("bai` 1")
n=int(input())
a=list(map(int,input().split()))
if len(a)==n:
    s=0
    for x in a:
        if x%5==0:s+=x
    print(s)

print("\nbai` 2")
n=int(input())
a=list(map(float,input().split()))
if len(a)==n:
    s=0
    d=0
    for x in a:
        if x<0:
            s+=x
            d+=1
    if d>0:print(s/d)
    else:print(0)

print("\nbai` 3")
n=int(input())
a=list(map(int,input().split()))
if len(a)==n:
    for i in range(n-1):
        m=i
        for j in range(i+1,n):
            if a[j]>a[m]:m=j
        a[i],a[m]=a[m],a[i]
    print(a)

print("\nbai` 4")
n=int(input())
a=list(map(int,input().split()))
if len(a)==n:
    for i in range(n):
        for j in range(n-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)

print("\nbai` 5")
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

print("de quy")

print("\nbai` 1")
n=int(input())
print(fib(n))

print("\nbai` 2")
n=int(input())
print(tcs(n))

print("\nbai` 3")
n=int(input())
print(tongChusole(n))

print("\nbai` 4")
n=int(input())
print(tday(n))
