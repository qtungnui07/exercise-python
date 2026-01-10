n=int(input())
def tongcacchuso(n):
    if n == 0:
        return 0
    else:
        return n % 10 + tongcacchuso(n // 10)
print(tongcacchuso(n))
