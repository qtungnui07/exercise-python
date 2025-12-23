print("\n3")
n=int(input())
arr=list(map(int,input().split()))
# print(*arr)
# if n==len(arr):
#     print("du")
# else:
#     pass

if n==len(arr):
    sum=0
    for x in arr:
        sum+=x
    svg=sum/n
    print(n)
else:
    print("viet thieu")
    
    
print("\n4")


n=int(input())
arr=list(map(int,input().split()))
if n==len(arr):
    sum=0
    for x in arr:
        if x %2==0:
            sum+=1
    print(n)
else:
    print("viet thieu")
    
    
print("\n5")
n=int(input())
count=1
for i in range(n):
    for j in range(n):
        print(count,end=" ")
        count+=1
    print()
    
    
print("\n8")
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j)%2==0:
            print("B",end=" ")
        else:
            print("W",end=" ")
            
    print()
    
print("\n10")
n=int(input())
for i in range(n):
    for j in range(n):
        print(i+j+1,end=" ")
    print()

# print("\n11")
# n=int(input())



print("\n12")
# C(line, i) = C(line, i-1) * (line - i + 1) / i
n=int(input())
for i in range(1,n+1):
    c=1
    for j in range(1,i+1):
        print(c,end='')
        c=c*(i-j)//j
    print()

print("\n13")

n=int(input())
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split())))
# print(mat)
doixung=True
for i in range(n):
    for j in range(i+1, n):
        if mat[i][j] != mat[j][i]:
            doixung=False
            break
    if not doixung:
        break
print("YES"if doixung else doixung)
print("\n15")
s=input()
# def hoanvi(list(s))
# print(list(s))
def hoanvi(word, postion):
    if postion==len(word)-1:
        print("".join(word))
        return
    for i in range(postion,len(word)):
        word[i],word[postion]=word[postion],word[i]
        hoanvi(word,postion+1)
        word[i],word[postion] = word[postion],word[i]
hoanvi(list(s), 0)

print("\\n16")
def arrs(main,start,current):
    print(current)
    for i in range(start,len(main)):
        current.append(main[i])
        arrs(main,i+1,current)
        current.pop()
arr=list(map(int,input().split()))
arrs(arr,0,[])



print("\n17")
# n=int(input())
# mat=[]
# for _ in range(n):
#     mat.append(list(map(int,input().split())))
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
def selection_sort_list(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min= j
        arr[i],arr[min]=arr[min],arr[i]
for row in matrix:
    selection_sort_list(row)
    print(*row)


print("\n18")

n=int(input())
ds=[]
for _ in range(n):
    # # name=input()
    # # diem=(float(input()))
    # name,diem=map()
    name, diem = input().split()
    diem = float(diem)
    ds.append({"name": name,"diem": diem})
for i in range(n):
    min_idx=i
    for j in range(i+1,n):
        if ds[j]["diem"]<ds[min_idx]["diem"]:
            min_idx=j
        elif ds[j]["diem"]==ds[min_idx]["diem"]:
            if ds[j]["name"]<ds[min_idx]["name"]:
                min_idx=j
            
    ds[i],ds[min_idx]=ds[min_idx],ds[i]
# print(ds)
for sv in ds:
    print(sv["name"],sv["diem"])
print("\n19")


arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    min_idx=i
    for j in range(i+1,n):
        if arr[j]>arr[min_idx]:
            min_idx=j
    arr[i],arr[min_idx]=arr[min_idx],arr[i]
for i in range(n):
    if arr[i]!=arr[i-1]:
        print(arr[i],end=" ")
