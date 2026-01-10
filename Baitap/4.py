arr=list(map(int,input().split()))
def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key>arr[j]:
            arr[j+1]=arr[j]
            j-=1
            print(arr)
        arr[j+1]=key
insertion(arr)
print(*arr)
for i in range(len(arr)-1):
    m=i
    for j in range(i+1,len(arr)):
        if arr[j]>arr[m]:m=j
    arr[i],arr[m]=arr[m],arr[i]
d=[]
for x in arr:
    if x not in d:d.append(x)
if len(d)>=3:
    v=d[2]
    print(v)
    for i in range(len(arr)):
        if arr[i]==v:print(i)
else:
    print("k du 3 gia tri khac nhau")