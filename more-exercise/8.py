import random as rd
n=int(input())
arr = [rd.randint(1, 100) for _ in range(n)]
print("ban dau`: ", arr)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(f"buoc {i+1}: {arr}")
