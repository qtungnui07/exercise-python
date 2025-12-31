n = int(input())
arr=[]
for i in range(1,n+1):
    arr.append(i)
def prime(x):
    if x < 2:
        return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return True
    return False
res = []
for i in range(n):
    if prime(arr[i]):
        res.append(arr[i])
print(*res)
