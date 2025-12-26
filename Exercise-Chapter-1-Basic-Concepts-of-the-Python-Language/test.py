# q = [[3, 4], [1, 2], [5, 6], [8, 7], [10, 9]]
# q = sorted(q)
# for i in q:
#     a, b = i
#     if not e:
#         e = [a, b]
#     else:
#         if a <= e[1]:
#             e[1] = max(e[1], b)
#         else:
#             r.append(e)
#             e = [a, b]
# r.append(e)
# print(r)

# q = [[1,2],[3,4],[5,6],[7,8]]
# w = []
# e = []
# r = []
# for i in q:
#     for j in i:
#         w.append(j)
#         if len(w) == 4:
#             e.append(min(w))
#             e.append(max(w))
#             r.append(e)
#             e = []
#             w = []
# print(r)

# s = input()
# if s == "":
#     print("an empty string")
# else:
#     print(len(s))

# try:
#     a = int(input())
#     if a < 0:
#         print("negative input")
#     res = 1
#     for i in range(1, a + 1):
#         res *= i
#     print(res)
# except ValueError:
#     print("invalid data types")

# try:
#     a,b=map(float,input().split())
#     print(a+b)
# except ValueError:
#     print("input is not a valid float")


# try:
#     n = float(input())
#     if n < 0:
#         print("negative number")
#     else:
#         print(n**0.5)
# except ValueError:
#     print("Invalid input")

# try:
#     a, b = map(int, input().split())
#     print("a / b =", a / b)
# except ZeroDivisionError:
#     print("Error: division by zero")
# except ValueError:
#     print("Error: invalid integer input")

# weight, height = map(float, input().split())
# avg_bmi = weight / (height * height)
# # print(round(avg_bmi, 2))
# print(f"{avg_bmi:.2f}")

# c = float(input())
# f = c * 9 / 5 + 32
# print(f"{c}oC = {f}oF")


# s = "123"
# n = int(s)
# res = n * 2
# print(res)


# s = input()
# sum = 0
# for i in s:
#     if i == "a":
#         sum += 1
# print(sum)


# try:
#     age_input = int(input())
#     age=int(age_input)
#     if age >= 120 or age <=1:
#         print("Invalid age")
#     else:
#         print("OK")
# except ValueError:
#     print("Invalid input")

# def greet(name="Student"):
#     print(f"Hello, {name}!")
# greet()
# greet("qtitpc")
# greet("qtung")

# n = list(map(int, input().split()))
# maximum = n[0]
# for num in n:
#     if num > maximum:
#         maximum = num
# print(maximum)
#
def bai_tap_26():
    try:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        c = float(input("Nhập số c: "))
        def sum_calc(x, y):
            print(f"Tổng ({x} + {y}) = {x + y}")
        def dif(x, y):
            print(f"Hiệu ({x} - {y}) = {x - y}")
        def mul(x, y, z):
            print(f"Tích ({x} * {y} * {z}) = {x * y * z}")
        def max_value(x, y, z):
            m = x
            if y > m: m = y
            if z > m: m = z
            print(f"Số lớn nhất là {m}")
            # if x >= y and x >= z:
            #     print(f"Số lớn nhất là {x}")
            # elif y >= x and y >= z:
            #     print(f"Số lớn nhất là {y}")
            # else:
            #     print(f"Số lớn nhất là {z}")
            # print(f"Số lớn nhất trong ba số là: {max(x, y, z)}")
        def binh_phuong(x):
            return x ** 2
        def lap_Phuong(x):
            return x ** 3
        sum_calc(a, b)
        dif(b, c)
        mul(a, b, c)
        max_value(a, b, c)
        print(f"Bình phương: a={binh_phuong(a)}, b={binh_phuong(b)}, c={binh_phuong(c)}")
        print(f"Lập phương: a={lap_Phuong(a)}, b={lap_Phuong(b)}, c={lap_Phuong(c)}")
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào không đúng định dạng.")

bai_tap_26()
