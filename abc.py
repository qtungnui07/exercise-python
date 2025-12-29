# n=int(input())
# arr=[]
# arr.append(list(map(int,input().split()))); print(*arr) if len(arr) else print("viet thieu")


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

# Bài 10: Nhập vào n là số phần tử trong mảng. Sau đó lần lượt nhập các phần tử trong mảng. Tìm những số đối xứng xuất hiện trong mảng đó kèm vị trí của nó. (Số đối xứng là số mà khi viết xuôi hay ngược mình đều thu được số đó ví dụ 1230321, 171,22,353… ).n = int(input()); arr = list(map(int, input().split()))
n = int(input())
arr = list(map(int, input().split()))
if len(arr) == n:
    for i in range(n):
        x=arr[i]
        temp=x
        s=0
        while temp>0:
            s=s*10+temp%10
            temp//=10
        if s==x:    
            print(x,i)
