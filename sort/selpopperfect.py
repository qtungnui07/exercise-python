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
    def inserion(arr):
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