#b1
print("\nb1")

m,n=map(int,input().split())
for i in range(m):
    for j in range(n):
        print("*", end=" ")
    print()
# b1
# 4 6
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
#b2
print("\nb2")
n=int(input())
print("hinh` 1")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
# b2
# 4
# hinh` 1
# * * * *
# * * * *
# * * * *
# * * * *
print("\nhinh` 2")
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
# hinh` 2
# *
# * *
# * * *
# * * * *
print("\nhinh` 3")
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
# hinh` 3
# * * * *
# * * *
# * *
# *
print("\nhinh` 4")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
# hinh` 4
#       *
#     * *
#   * * *
# * * * *
print("\nhinh` 5")
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# hinh` 5
# *
# * *
# *   *
# * * * *

print("\nhinh` 6")
for i in range(n):
    for j in range(n-i):
        if j==0 or i==0 or j==n-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# hinh` 6
# * * * *
# *   *
# * *
# *
print("\nhinh` 7")
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# hinh` 7
# *
# * *
# *   *
# * * * *
print("\nhinh` 8")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()
    
# hinh` 8
#    *
#   * *
#  * * *
# * * * *
print("\nhinh` 9")
for i in range(1,n+1):
    print(" " * (n-i), end="")  
    if i==1:
        print("*")
    elif i==n:
        print("* "*n)
    else:
        print("*"+" "*(2*i-3)+"*")
        
# hinh` 9
#    *
#   * *
#  *   *
# * * * *

print("\nhinh` 10")
for i in range(n,0,-1):
    print(" " * (n - i), end="")  
    if i==1:
        print("*")
    elif i==n:
        print("* "*n)
    else:
        print("*"+" "*(2*i-3)+"*")
        
# hinh` 10
# * * * *
#  *   *
#   * *
#    *

#b3
print("\nb3")

n=int(input())
print("\nhinh`1")
for i in range(n):
    for j in range(n):
        print(1, end="  ")
    print()
    
# b3
# 4

# hinh`1
# 1  1  1  1
# 1  1  1  1
# 1  1  1  1
# 1  1  1  1
print("\nhinh`2")
for i in range(n):
    for j in range(n):
        print(j+1, end="  ")
    print()

# hinh`2
# 1  2  3  4
# 1  2  3  4
# 1  2  3  4
# 1  2  3  4
print("\nhinh`3")
for i in range(n):
    for j in range(i+1):
        print(j+1, end="  ")
    print()
    
# hinh`3
# 1
# 1  2
# 1  2  3
# 1  2  3  4

print("\nhinh`4")
for i in range(n,0,-1):
    for j in range(i):
        print(j+1, end="  ")
    print()
    
# hinh`4
# 1  2  3  4
# 1  2  3
# 1  2
# 1
print("\nhinh`5")
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print(j,end="  ")
        else:
            print("  ",end=" ")
    print()
    

# hinh`5
# 1
# 1  2
# 1     3
# 1  2  3  4

print("\nhinh`6")
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i==n or j==1 or j==i:
            print(j,end="  ")
        else:
            print("  ",end=" ")
    print()
    
# hinh`6
# 1  2  3  4
# 1     3
# 1  2
# 1

print("\nhinh`7")
for i in range(1,n+1):
    print("  "*(n-i),end="  ")
    print((str(i)+"   ") * i)
    
# hinh`7
#         1
#       2   2
#     3   3   3
#   4   4   4   4

print("\nhinh`8")
for i in range(1,n+1):
    print("   "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="  ")
    for k in range(i-1,0,-1):
        print(k,end="  ")
    print()
    
# hinh`8
#          1
#       1  2  1
#    1  2  3  2  1
# 1  2  3  4  3  2  1
print("\nhinh`9")
for i in range(1,n+1):
    print("  "*(n-i),end="")
    if i==n:
        for j in range(1,n+1):
            print(j,end=" ")
        for j in range(n-1,0,-1):
            print(j,end=" ")
    else:
        print(1,end=" ")
        if i>1:
            print("  "*(2*i-3),end="") 
            print("1",end=" ")
    print()
    
    
# hinh`9
#       1
#     1   1
#   1       1
# 1 2 3 4 3 2 1