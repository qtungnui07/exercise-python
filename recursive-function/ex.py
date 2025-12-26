print("1.")
def res_sum(n):
    if n==1:
        return 1
    return n + res_sum(n-1)
n=int(input())
print(res_sum(n))



print("\n2.")

def res_prod(n):
    if n==0 or n==1:
        return 1
    return n * res_prod(n-1)
n=int(input())
print(res_prod(n))

print("\n3.")

n=int(input())
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(f"so thu tu cua {n} fib la: {fib(n)}")
for i in range(n+1):
    print(fib(i), end=" ")

print("\n4.")
n=abs(int(input())) #abs la gia tri tuyet doi
def total_num(n):
    if n <10:
        return 1
    return 1 + total_num(n//10)
print(total_num(n))

print("\n5.")

n=abs(int(input())) #abs la gia tri tuyet doi
def total_num_even(n):
    if n==0:
        return 0
    if (n%10)%2==0:
        return 1 + total_num_even(n//10)
    else:
        return total_num_even(n//10)
    # else:    return 1 + total_num_even(n//10)
if n==0:
    print(1)
else: print(total_num_even(n))



print("\n6.")
n=abs(int(input()))
def total_char_num(n):
    if n ==0:
        return 0
    return n%10 + total_char_num(n//10)
print(total_char_num(n))
print("\n7.")
a,n=map(int,input("a, n: ").split())
def a_n(a,n):
    if n == 0:
            return 1
    return a * a_n(a, n-1)
print("\n8.")
n=int(input())
def sum_of_1_n(n):
    if n == 1:
        return 1
    return 1/n +sum_of_1_n(n-1)
if n<1:
    print("n phai lon hon 1")
else: print(sum_of_1_n(n))