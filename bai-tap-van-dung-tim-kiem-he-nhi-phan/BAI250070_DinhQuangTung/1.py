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
arr = list(map(int, input().split()))
x = int(input())
if len(arr)==n:
    def binary_search(arr, x):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x: return mid
            elif arr[mid] < x: left = mid + 1
            else: right = mid - 1
        return -1
    result = binary_search(arr, x)
    print("index: ",result if result != -1 else "not found")
else:
    print("k du phan tu trong mang")








