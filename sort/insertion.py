arr=list(map(int,input().split()))
def inserion(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            print(*arr)
        arr[j+1]=key
inserion(arr)
print(*arr)
