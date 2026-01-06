arr=list(map(int,input().split()))
def inserion(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
inserion(arr)
print(*arr)




def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key>arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
insertion(arr)
print(*arr)
