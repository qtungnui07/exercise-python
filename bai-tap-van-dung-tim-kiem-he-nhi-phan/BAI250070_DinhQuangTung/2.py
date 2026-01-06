# import sys

# class Logger:
#     def __init__(self, filename):
#         self.terminal = sys.stdout
#         self.log = open(filename, "a", encoding="utf-8")

#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)

#     def flush(self):
#         pass

# log_file = __file__.replace(".py", ".txt")
# sys.stdout = Logger(log_file)
# sys.stderr = sys.stdout


n=int(input())
arr=list(map(int,input().split()))
x=int(input())
if len(arr)==n:
    def sel(arr):    
        for i in range(len(arr)):
            min_idx=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_idx]:
                    min_idx=j
            arr[i],arr[min_idx]=arr[min_idx],arr[i]
        print(*arr)
    sel(arr)
    def binary_search(arr,x):
        l,r=0,len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m]==x:return m
            if arr[m]<x:l=m-1
            elif arr[m]<x:l=m+1
            else:r=m-1
        return -1
    binary_search(arr,x)
    result = binary_search(arr, x)
    print("index: ",result if result != -1 else "not found")
    
else:
    print("k du phan tu trong mang")
    
    
#neu co 2 phan tu trung nhau thi
# 
# n=int(input())
# arr=list(map(int,input().split()))
# x=int(input())

# if len(arr)==n:

#     def sel(arr):
#         for i in range(len(arr)):
#             min_idx=i
#             for j in range(i+1,len(arr)):
#                 if arr[j]<arr[min_idx]:
#                     min_idx=j
#             arr[i],arr[min_idx]=arr[min_idx],arr[i]
#         print(*arr)

#     sel(arr)

#     def bs(arr,x):
#         l,r=0,len(arr)-1
#         while l<=r:
#             m=(l+r)//2
#             if arr[m]==x: return m
#             elif arr[m]<x: l=m+1
#             else: r=m-1
#         return -1

#     idx=bs(arr,x)

#     if idx==-1:
#         print("not found")
#     elif (idx>0 and arr[idx-1]==x) or (idx<len(arr)-1 and arr[idx+1]==x):
#         l=r=idx
#         while l>0 and arr[l-1]==x: l-=1
#         while r<len(arr)-1 and arr[r+1]==x: r+=1
#         print(l, r)
#     else:
#         print(idx)

# else:
#     print("k du phan tu trong mang")
