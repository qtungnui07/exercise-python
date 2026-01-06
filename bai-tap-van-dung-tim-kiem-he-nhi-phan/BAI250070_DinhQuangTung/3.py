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
    def binary_search(arr,x):
        l,r=0,len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m]==x:return m
            if arr[m]<x:l=m+1
            else:r=m-1
        return -1
    binary_search(arr,x)
    result = binary_search(arr, x)
    print("index: ",result if result != -1 else "not found")
    
else:
    print("k du phan tu trong mang")
