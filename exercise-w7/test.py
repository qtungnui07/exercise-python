# m,n=map(int,input().split())
# for i in range(m):
#     for j in range(n):
#         print("*", end=" ")
#     print()


# n=int(input())
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# print("\nhinh` 2")
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# print("\nhinh` 3")
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n=int(input())
# for i in range(n+1):
#     for j in range(n-i):
#         print("",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()


# n=int(input())
# for i in range(1, n + 1):
#         # print("*"*(o-1))
#     if i == 1:
#         print("*")
#     elif i == n:
#         print("* " * n)
#     else:
#         print("*" + " " * (i - 2) + "*")


# n=int(input())
# for i in range(n,0,-1):
#     print(" " * (n - i), end="")  
#     if i == 1:
#         print("*")

#     elif i == n:
#         print("* " * n)
#     else:
#         print("*" + " " * (2 * i - 3) + "*")

# *
# * *
# *   *
# * * * *



# n=int(input())
# # for i in range(n):
# #     for j in range(i+1):
# #         if j==0 or j==i or i==n-1:
# #             print("*",end=" ")
# #         else:
# #             print(" ",end=" ")
# #     print()
# for i in range(n):
#     for j in range(n-i):
#         if i==0 or j==0  or j==n-i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end="  ")
#     print()
    


# for i in range(1, n + 1):
#     print("  " * (n - i), end="  ")
#     print((str(i) + "   ") * i)


# for i in range(1,n+1):
#     print("   "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end="  ")
#     for k in range(i-1,0,-1):
#         for g in range(i-1,0):
#             print(".",end="  ")

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if i==n or j==1 or j==i:
#             print(j,end="  ")
#         else:
#             print("  ",end=" ")
#     print()
# for i in range(1,n+1):
#     print("  "*(n-i),end="")
#     if i==n:
#         for j in range(1,n+1):
#             print(j,end=" ")
#         for j in range(n-1,0,-1):
#             print(j,end=" ")
#     else:
#         print(1,end=" ")
#         if i>1:
#             print("  "*(2*i-3),end="") 
#             print("1",end=" ")
#     print()
    







# for i in range(1,n+1):
#     print(" " * (n-i), end="")  
#     if i==1:
#         print("*")
#     elif i==n:
#         print("* "*n)
#     else:
#         print("*"+" "*(2*i-3)+"*")



for i in range(n):
    for s in range(n - i - 1):
        print("  ", end="")
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()























