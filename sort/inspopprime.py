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
    def inserion(res):
        for i in range(len(res)):
            key=res[i]
            j=i-1
            while j>=0 and key<res[j]:
                res[j+1]=res[j]
                j-=1
                print(*res)
            res[j+1]=key
    inserion(res)
else:pass