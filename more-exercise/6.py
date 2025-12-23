n=int(input())
def prime(x):
    if x<2: return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: return False
    return True
def check_number(num):
    s=str(num)
    return s == s[::-1]
def final(n):
    res=[]
    for i in range(n+1):
        if prime(i) and check_number(i):
            res.append(i)
    print(", ".join(map(str, res)))
final(n)

