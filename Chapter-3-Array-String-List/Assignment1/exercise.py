print("1.")
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
print(fruits[0])
fruits[2] = "Pineapple"
print(fruits)

print("\n2.")
subjects = ["Math", "Physics", "Chemistry", "History"]
print(len(subjects))
for sub in subjects:
    print(sub)

print("\n3.")
friends = ["Son", "Tung", "ADU"]
friends.append("idkman")
friends.pop(1)
print(friends)

print("\n4.")
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
try:
    colors.remove("Green")
except ValueError:
    print("Not found")
print(colors)

print("\n5.")
nums = list(map(int, input().split()))
x = int(input())
nums.sort()
print(nums)
nums.reverse()
print(nums)
print(nums.count(x))

print("\n6.")
lst = list(map(int,input().split()))
n = len(lst)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if lst[j] < lst[min_idx]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]
print(lst)

print("\n7.")
lst = list(map(float,input().split()))
for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    while j >= 0 and key > lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key
print(lst)

print("\n8.")
lst = list(map(int,input().split()))
n = len(lst)
swaps = 0
for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            swaps += 1
print(lst)
print(swaps)

print("\n9.")
lst = list(map(int,input().split()))
target = int(input())
found = False
for i in range(len(lst)):
    if lst[i] == target:
        print(i)
        found = True
        break
if not found:
    print(-1)

print("\n10.")
lst = list(map(int,input().split()))
for x in lst:
    if x > 10:
        print(x)
        break

print("\n11.")
lst = list(map(int,input().split()))
for x in lst:
    if x % 2 != 0:
        print(x)

print("\n12.")
lst = list(map(int,input().split()))
evens = []
total = 0
for x in lst:
    if x % 2 == 0:
        evens.append(x)
        total += x
print(evens)
print(total)