n=int(input())
def tongle(n):
    if n<=0:
        return 0
    if n%2!=0:
        return n+tongle(n-2)
    else:
        return tongle(n-1)
print(tongle(n))