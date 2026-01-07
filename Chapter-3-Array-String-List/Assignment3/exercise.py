import random #random cho bai 2, 3
def is_prime(n): #ap dung bai 1 va 6
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#1
lst = list(map(int, input().split()))
k = int(input())
print(lst.count(k))
s = 0
for x in lst:
    if is_prime(x):
        s += x
print(s)
lst.sort()
print(lst)
lst.clear()
print(lst)

#2
n = int(input())
lst = [random.randint(0, 20) for _ in range(n)]
print(lst)
k = int(input())
lst = [x for x in lst if x != k]
print(lst)
print(lst == lst[::-1])

#3
m, n = map(int, input().split())
matrix = [[random.randint(0, 50) for _ in range(n)] for _ in range(m)]
for row in matrix:
    print(*row)
r = int(input())
print(*matrix[r])
c = int(input())
for i in range(m):
    print(matrix[i][c])
mx = matrix[0][0]
for row in matrix:
    for x in row:
        if x > mx:
            mx = x
print(mx)

#4
lst = [3, 0, 1, 5, 2]
x = 2
print(lst[0])
print(lst[3])
print(lst[x])
print(lst[-x])
print(lst[x + 1])
print(lst[x] + 1)
print(lst[lst[x]])
print(lst[lst[lst[x]]])

#5
lst = [20, 1, -34, 40, -8, 60, 1, 3]
print(lst)
print(lst[0:3])
print(lst[4:8])
print(lst[4:33])
print(lst[-5:-3])
print(lst[-22:3])
print(lst[4:])
print(lst[:])
print(lst[:4])
print(lst[1:5])
print(-34 in lst)
print(-34 not in lst)
print(len(lst))

#6
arr = list(map(int, input().split()))
odds = []
evens = []
primes = []
non_primes = []
for x in arr:
    if x % 2 != 0:
        odds.append(x)
    else:
        evens.append(x)
    if is_prime(x):
        primes.append(x)
    else:
        non_primes.append(x)
print(*odds, len(odds))
print(*evens, len(evens))
print(*primes)
print(*non_primes)

#7 **
m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(m)]
C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
for row in C:
    print(*row)

def transpose(mat):
    return list(map(list, zip(*mat)))

TA = transpose(A)
TB = transpose(B)
for row in TA:
    print(*row)
for row in TB:
    print(*row)

#8
arr = list(map(int, input().split()))
def reverselist(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
reverselist(arr)
print(arr)

#9 
arr = list(map(int, input().split()))
mx = mn = arr[0]
for x in arr:
    if x > mx:
        mx = x
    if x < mn:
        mn = x
print(mx, mn)

#10 **
mat = [list(map(int, input().split())) for _ in range(3)]
s = sum(mat[0])
ok = True
for i in range(3):
    if sum(mat[i]) != s:
        ok = False
for j in range(3):
    if mat[0][j] + mat[1][j] + mat[2][j] != s:
        ok = False
if mat[0][0] + mat[1][1] + mat[2][2] != s:
    ok = False
if mat[0][2] + mat[1][1] + mat[2][0] != s:
    ok = False
print(ok)
