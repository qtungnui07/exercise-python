arr = list(map(int, input().split()))

x = int(input())


def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x: return mid
        elif arr[mid] < x: left = mid + 1
        else: right = mid - 1
    return -1
    


result = binary_search(arr, x)
if result != -1:
    print(f"Tim thay x tai vi tri (index): {result}")
else:
    print("not found")
