n = int(input())
arr = list(map(int, input().split()))
if len(arr)==n:
    def prime(x):
        if x>0:
            s=0
            for j in range(1, x): 
                if x%j==0:
                    s+=j
            if s==x:
                return False
        return True
    res = []
    for i in range(n):
        if prime(arr[i]):
            print(arr[i])
            res.append(arr[i])
    def sel(a):
        for i in range(len(a)):
            min_idx = i
            for j in range(i + 1, len(a)):
                if a[j] < a[min_idx]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
            print(a)
    sel(res)
else:pass