n=int(input())
arr=list(map(int,input().split()))
if len(arr)==n:
    for i in range(len(arr)):
        idx=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[idx]:
                idx=j
                arr[i],arr[idx]=arr[idx],arr[i]
                print(arr)
    print(*arr)
    
else:
    print("chua viet du so phan tu, viet thua so phan tu")