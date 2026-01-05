import sys

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

log_file = __file__.replace(".py", ".txt")
sys.stdout = Logger(log_file)
sys.stderr = sys.stdout


arr=list(map(int,input().split()))
n=int(input())
def sel(arr):    
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    print(*arr)
sel(arr)
def binary_search(arr,n):
    l,r=0,len(arr)-1
    while l<=r:
        m=(l+r)//2
        if arr[m]==n:return m
        if arr[m]<n:l=m+1
        else:r=m-1
    return -1
binary_search(arr,n)