print("b1")
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
for i in arr:
    print(i, end=" ")
print("\nb2")
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
i=0
for x in arr:
    print(f"arr[{i}] = {x}")
    i+=1
print("\nb3")
n=int(input())
arr = list(map(int,input().split()))
if len(arr)==n:
    print(', '.join(f"arr[{i}] = {arr[i]}" for i in range(n-1,-1,-1) ))
else:
    print("viet thieu phan tu")
print("\nb4")
n=int(input())
arr = list(map(int,input().split()))
if len(arr)==n:
    for i in range(n):
        if i%2==0:
            print(arr[i])
else:
    print("viet thieu phan tu")
print("\nb5")
n=int(input())
arr = list(map(int,input().split()))
if len(arr)==n:
    for i in arr:
        if i%2==0:
            print(i, end=" ")
else:
    print("viet thieu phan tu")
print("\nb6")
n=int(input())
arr = list(map(int,input().split()))
if len(arr)==n:
    sum=0
    for i in arr:
        sum+=i
    print(sum)
else:
    print("viet thieu phan tu")
print("\nb7")
n = int(input())
arr = list(map(int, input().split()))
def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
res=[]
for i in range(n):
    if prime(arr[i]):
        res.append(f"arr[{i}] = {arr[i]}")
print(', '.join(res))
print("\nb8")
n=int(input())
arr=list(map(int,input().split()))
i=0
while i<n:
    x=arr[i]
    if x>=0:
        k=0
        while k*k<=x:
            if k*k==x:
                print(f"arr[{i}] = {x}")
                break
            k+=1
    i+=1
print("\nb9")
n = int(input()); arr = list(map(int, input().split()))
if len(arr)==n:
    for i in range(n):       
        x=arr[i]
        if x>0:
            s=0
            for j in range(1, x): 
                if x%j==0:
                    s+=j
            if s==x:
                print(i)
else:
    print("thieu phan tu")
print("\nb10")
n = int(input())
arr = list(map(int, input().split()))
if len(arr) == n:
    for i in range(n):
        x=arr[i]
        temp=x
        s=0
        while temp>0:
            s=s*10+temp%10
            temp//=10
        if s==x:    
            print(x,i)
