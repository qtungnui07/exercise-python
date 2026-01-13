arr = list(map(int,input().split()))
def findmaxest(arr):
    maxidx = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxidx:
            maxidx = arr[i]
    return maxidx
maxidx = findmaxest(arr)
print("Gia tri lon nhat cua arr la:", maxidx)
print(f"goc {arr}")
def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        print(arr)
        while j>=0 and key>arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
insertion(arr)
print(*arr)