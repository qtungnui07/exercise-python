# n=int(input())
# arr = list(map(int,input().split()))
# print(', '.join(f"arr[{i}] = {arr[i]}" for i in range(n-1,-1,-1) ))

# import math
# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(n):
#     if is_prime(arr[i]):
#         print(f"arr[{i}] = {arr[i]}")
# n = int(input())
# arr = list(map(int, input().split()))
# def prime(x):
#     if x<2:
#         return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# res=[]
# for i in range(n):
#     if prime(arr[i]):
#         res.append(f"arr[{i}] = {arr[i]}")
# print(', '.join(res))

# Bài 9: Nhập vào n là số phần tử trong mảng. Sau đó lần lượt nhập các phần tử trong mảng. Tìm những số hoàn hảo xuất hiện trong mảng đó kèm vị trí của nó. (Số hoàn hảo là số có tổng các ước của nó bằng chính nó. Ví dụ 6 có ước là 1+2+3 =6 là số hoàn hảo)
# 
# n = int(input()); arr = list(map(int, input().split()))
# if len(arr)==n:
#     for i in range(n):       
#         x=arr[i]
#         if x>0:
#             s=0
#             for j in range(1, x): 
#                 if x%j==0:
#                     s+=j
#             if s==x:
#                 print(i)
# else:
#     print("thieu phan tu")

# n = int(input())
# arr = list(map(int, input().split()))
# if len(arr) == n:
#     for i in range(n):
#         x=arr[i]
#         temp=x
#         s=0
#         while temp>0:
#             s=s*10+temp%10
#             temp//=10
#         if s==x:    
#             print(x,i)


n=int(input())
arr=list(map(int,input().split()))
i=0
while i<n:
    x=arr[i]
    if x>=0:
        k=0
        while k*k<=x:
            if k*k==x:
                print(f"arr[{i}] = {x}")
                break
            k+=1
    i+=1