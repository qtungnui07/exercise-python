# Exercise 1
print("1.")
n = int(input())
if n == 0:
    print("zero")
elif n > 0:
    print("positive")
else:
    print("negative")

# Exercise 2
print("\n2.")
for i in range(1, 11):
    print(i)

# Exercise 3
print("\n3.")
n = int(input())
if n < 1:
    print("Invalid input")
else:
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)

# Exercise 4
print("\n4.")
n = int(input())
print("even" if n % 2 == 0 else "odd")

# Exercise 5
print("\n5.")
for i in range(2, 21, 2):
    print(i)

# Exercise 6
print("\n6.")
n = abs(int(input()))
if n == 0:
    print(1)
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1
    print(count)

# Exercise 7
print("\n7.")
n = int(input())
if n < 0:
    print("Invalid input")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

# Exercise 8
print("\n8.")
n = int(input())
if n < 1 or n > 9:
    print("Invalid input")
else:
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# Exercise 9
print("\n9.")
for i in range(1, 101):
    if i % 3 != 0:
        print(i)

# Exercise 10
print("\n10.")
n = 101
while True:
    if n % 7 == 0:
        print(n)
        break
    n += 1

# Exercise 11
print("\n11.")
n = int(input())
if n < 2:
    print("Not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

# Exercise 12
print("\n12.")
n = int(input())
if n <= 0:
    print("Invalid input")
else:
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Exercise 13
print("\n13.")
n = abs(int(input()))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)

# Exercise 14
print("\n14.")
s = input()
c = input()
if len(c) != 1:
    print("Invalid character")
else:
    print(s.count(c))

# Exercise 15
print("\n15.")
def factorial(n):
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input())
res = factorial(n)
print("Invalid input" if res is None else res)

# Exercise 16
print("\n16.")
a = abs(int(input()))
b = abs(int(input()))
while b != 0:
    a, b = b, a % b
print(a)

# Exercise 17
print("\n17.")
for num in range(1, 1001):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        print(num)

# Exercise 18
print("\n18.")
n = int(input())
sign = -1 if n < 0 else 1
n = abs(n)
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(sign * rev)

# Exercise 19
print("\n19.")
n = abs(int(input()))
if n == 0:
    print(0)
else:
    largest = 0
    while n > 0:
        largest = max(largest, n % 10)
        n //= 10
    print(largest)

# Exercise 20
print("\n20.")
def sum_recursive(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

n = int(input())
res = sum_recursive(n)
print("Invalid input" if res is None else res)