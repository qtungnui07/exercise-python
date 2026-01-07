arr=list(map(int,input().split()))
def bubblesort(arr):
    for i in range(len(arr)):
        swap=False
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]
                
                swap=True
        if not swap:
            break
    print(*arr)
bubblesort(arr)