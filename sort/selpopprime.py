n = int(input())
arr = list(map(int, input().split()))
if len(arr)==n:
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