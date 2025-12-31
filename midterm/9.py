n=int(input())
arr=list(map(int,input().split()))
if len(arr)==n:
    def inserion(arr):
        for i in range(len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and key<arr[j]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
            print(arr)
    inserion(arr)
    print(*arr)
else:
    print("chua viet du so phan tu mang, viet thua so phan tu")