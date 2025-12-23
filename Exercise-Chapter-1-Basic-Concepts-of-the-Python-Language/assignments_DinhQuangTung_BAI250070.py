# Exercise1. Create variables of different data types
# • Create and print three variables: one integer, one float, and one string.

integer_variables = 21012007
float_variables = 6.5
string_variables = "Hi there, I'm Tung."
# print(f"{integer_variables, float_variables, string_variables}")
print(f"{integer_variables} {float_variables} {string_variables}")

# Exercise 2. Greet the user
# • Prompt the user to enter their name and print: "Hello, [Name]".

name = input("Put ur name: ")
print(f"Hello, {name}")


# Exercise 3. Display data type of variable x = 3.14
# • Use the type() function to print the data type of x = 3.14.

x = 3.14
print(f"{type(x)}")

# Exercise 4. Calculate the circumference of a circle
# • Define a constant PI = 3.14.
# • Calculate and print the circumference of a circle with radius r = 5

Pi = 3.14
r = 5
circumference = 2 * Pi * r
print(f"{circumference}")

# Exercise 5. Perform basic arithmetic with two numbers
# • Input two integers from the user.
# • Calculate and print their sum, difference, product (nhân), and quotient (thương).

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Exercise 6. Function to calculate the sum of two numbers
# • Write a function sum_two_numbers(a, b) that returns the sum of two integers.
# • Call the function and print the result.


def sum_two_numbers(a, b):
    return a + b


print(sum_two_numbers(21, 7))

# Exercise 7. Declare, process, and display personal information
# • Create variables name, age, and average_score.
# • Use the type() function to display the data type of each variable.
# • Create a variable age_next_year by adding 1 to age, and doubled_score by
# doubling average_score.
# • Print all the information and their data types.

name = "qtitpc"
age = 18
average_score = 85.5
print(f"Name: {name}, {type(name)}")
print(f"Age: {age}, {type(age)}")
print(f"Average Score: {average_score}, {type(average_score)}")
age_next_year = age + 1
doubled_score = average_score * 2
print(f"Age Next Year: {age_next_year}, {type(age_next_year)}")
print(f"Doubled Score: {doubled_score}, {type(doubled_score)}")

# Exercise 8. Check if a number is even
# • Write a function is_even(n) that returns True if n is even, otherwise False.

n = int(input())


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(is_even(n))

# Exercise 9. Find the maximum of three numbers
# • Input three numbers and print the largest one.

# n=map(int,input().split())
# print(max(n))

# n=map(int, input().split())
# list=list(n)
# for i in list(n):
#     if a[i] < a[i+1]:
#         print(a[i+1])
#     elif a[i] > a[i+1]:
#         print(a[i])
#     else:
#         print(a[i])

n = list(map(int, input().split()))
maximum = n[0]
for num in n:
    if num > maximum:
        maximum = num
print(maximum)

# Exercise 10. Function with default argument
# • Write a function greet(name="Student") that prints "Hello, Student!".
# • Call the function with and without providing an argument.


def greet(name="Student"):
    print(f"Hello, {name}!")


greet()
greet("qtitpc")
greet("qtung")


# Exercise 11. Validate age input
# • Prompt the user to enter their age.
# • Check if the age is between 1 and 120. Print a suitable message.

try:
    age_input = int(input())
    age = int(age_input)
    if age >= 120 or age <= 1:
        print("Invalid age")
    else:
        print("OK")
except ValueError:
    print("Invalid input")

# Exercise 12. Count occurrences of character 'a'
# • Input a string and count the number of times the letter 'a' appears.

s = input()
sum_c = 0
for i in s:
    if i == "a":
        sum_c += 1
print(sum_c)

# Exercise 13. Convert string number to integer
# • Convert the string "123" into an integer, multiply it by 2, and print the result.

s = "123"
n = int(s)
res = n * 2
print(res)

# Exercise 14. Convert Celsius to Fahrenheit
# Write a program that converts a temperature from degrees Celsius to
# degrees Fahrenheit.
# • Ask the user to input the temperature in Celsius (as a float).
# • Use the formula: F = C × 9/5 + 32
# • Print the result in a formatted string.

c = float(input())
f = c * 9 / 5 + 32
print(f"{c}oC = {f}oF")

# Exercise 15. Calculate BMI (Body Mass Index)
# Write a program that calculates and displays the Body Mass Index (BMI).
# • Input: weight in kilograms and height in meters.
# • Formula: BMI = weight / (height * height)
# • Use float type and arithmetic operators.
# • Display the BMI rounded to 2 decimal places.
# If weight = 60kg and height = 1.65m → BMI ≈ 22.04


weight, height = map(float, input().split())
avg_bmi = weight / (height * height)
# print(round(avg_bmi, 2))
print(f"{avg_bmi:.2f}")


# Assignment - Exception Handling
# • Exercise 16: Input two integers from the keyboard and print the result of
# their division. Handle division by zero and invalid input types.

try:
    a, b = map(int, input().split())
    print("a / b =", a / b)
except ZeroDivisionError:
    print("Error: division by zero")
except ValueError:
    print("Error: invalid integer input")

# • Exercise 17: Input a number and calculate its square root. If the input is
# negative, display an error message.

try:
    n = float(input())
    if n < 0:
        print("negative number")
    else:
        print(n**0.5)
except ValueError:
    print("Invalid input")

# • Exercise 18: Input two floating-point numbers and print their sum. Handle
# errors when the input is not a valid float.

try:
    a, b = map(float, input().split())
    print(a + b)
except ValueError:
    print("input is not a valid float")

# • Exercise 19: Input an integer and calculate its factorial. Handle errors for
# negative input or invalid data types.
try:
    a = int(input())
    if a < 0:
        print("negative input")
    res = 1
    for i in range(1, a + 1):
        res *= i
except ValueError:
    print("invalid data types")

# • Exercise 20: Input a string and print its length. Handle the case where the
# user enters an empty string by displaying an error message.

s = input()
if s == "":
    print("an empty string")
else:
    print(len(s))


# Exercise 21. Discriminant and classification (Quadratic equation)
# Requirements:
# •	Input three real numbers a, b, c using try–except for error handling.
# •	Define two functions:
# • tinh_biet_thuc(a, b, c) → returns b² – 4ac
# • phan_loai(d) → returns "Âm", "Không", or "Dương"
# •	Restriction: Do not use if/elif/else; use list + boolean addition for selection.
# Example Output:
# Biệt thức = 5.00 → Loại: Dương


# print("21. ")
# try:
#     a,b,c=map(float,input().split())

#     # print(a,b,c)
#     def tinh_biet_thuc(m,n,p):
#         d=n**2-(4*m*p)
#         return d


#     print(tinh_biet_thuc(a,b,c))
# except:
#     print("error handling")


# print()
# print("22. ")
# DONG_BANG = 0.0
# SOI = 100.0
# HE_SO = 9/5
# HIEU = 32
# c=int(input())
# def doC_sang_doF(c):
#     f = c × 9/5 + 32
#     return f
# def


print()
print("21. ")


def exercise_21():
    try:
        a, b, c = map(float, input().split())

        # return a,b,c
        def tinh_biet_thuc(a, b, c):
            return b**2 - 4 * a * c

        def phan_loai(d):
            sth = ["Âm", "Không", "Dương"]
            index = int(d >= 0) + int(d > 0)
            return sth[index], index

        delta = tinh_biet_thuc(a, b, c)
        init = phan_loai(delta)
        print(delta, init)
    except ValueError:
        print("error handling")


exercise_21()

print()
print("22. ")


def exercise_22():
    dong_bang = 0.0
    soi = 100.0
    he_so = 9 / 5
    hieu = 32
    c = float(input("nhap nhiet do c: "))

    def doC_sang_doF(c):
        f = c * he_so + hieu
        return f

    def duoi_dong_bang(c):
        return c < dong_bang

    def tren_diem_soi(c):
        return c > soi

    # print(doC_sang_doF(c), duoi_dong_bang(c), tren_diem_soi(c))
    # Nhiệt độ: 25.00°C → 77.00°F
    # Dưới đóng băng: False
    # Trên điểm sôi: False
    print(f"Nhiệt độ: {c}°C -> {doC_sang_doF(c)}°F")
    print(f"Dưới đóng băng: {duoi_dong_bang(c)}")
    print(f"Trên điểm sôi: {tren_diem_soi(c)}")


exercise_22()
print()
print("23. ")

# Exercise 23. BMI calculation and health classification
# Requirements:
# •	Input can_nang (kg) and chieu_cao (m) as floats using try–except.
# •	Compute bmi = can_nang / (chieu_cao ** 2).
# •	Define phan_loai_bmi(bmi) → returns one of:
# "Gầy" , "Bình thường" , "Thừa cân" , "Béo phì"
# •	Use list indexing and sum of boolean conditions, not if.
# •	Round BMI to 2 decimal places when printing.
# Example Output:
# BMI: 22.04 → Phân loại: Bình thường


def exercise_23():
    try:
        can_nang, chieu_cao = map(float, input("nhap can nang va chieu cao: ").split())
        bmi = can_nang / (chieu_cao**2)

        def phan_loai_bmi(bmi):
            label = ["Gầy", "Bình thường", "Thừa cân", "Béo phì"]
            index = (bmi >= 18.5) + (bmi >= 25) + (bmi >= 30)
            return label[index]

        res_bmi = phan_loai_bmi(bmi)
        print(f"BMI: {round(bmi, 2)}-> Phan loai: {res_bmi}")

    except ValueError:
        print("error, try again")


exercise_23()


print()
print("24.")


# Exercise 24. Analyze integer properties
# Requirements:
# •	Input two integers x, y with error handling.
# •	Define four functions:
# • la_so_duong(n) → checks if positive
# • la_so_chan(n) → checks if even
# • cung_chan_le(x, y) → checks if both even or both odd
# • tong (x, y) → returns (sum), Tich(x,y) -> return (tich)
# •	Print all boolean results and computed values.
# •	Restriction: no loops, no conditional statements.
# Example Output:
# x = 4, y = 7
# Dương: True | Chẵn: True
# Cùng chẵn/lẻ: False
# Tổng = 11 | Tích = 28
def exercise_24():
    try:
        x, y = map(int, input("nhap 2 so x, y: ").split())

        def la_so_duong(n):
            return n > 0

        def la_so_chan(n):
            return n % 2 == 0

        def cung_chan_le(a, b):
            return (a % 2) == (b % 2)

        def tong_tich(a, b):
            return a + b, a * b

        tong, tich = tong_tich(x, y)
        print(f"x = {x}, y = {y}")
        print(f"X -> Dương: {la_so_duong(x)} | Chẵn: {la_so_chan(x)}")
        print(f"Y -> Dương: {la_so_duong(y)} | Chẵn: {la_so_chan(y)}")
        print(f"Cùng chẵn/lẻ: {cung_chan_le(x, y)}")
        print(f"Tổng = {tong} | Tích = {tich}")
    except ValueError:
        print("error handing")


exercise_24()

# Exercise 25. Personal info formatting and type checking
# Requirements:
# •	Input:
# • ten → string
# • tuoi → integer
# • diem → float (0–10)
# • Handle invalid input separately with try–except.
# •	Define:
# • dinh_dang_thong_tin(ten, tuoi, diem) → returns formatted string:
# [Nguyen Van A] | Tuổi: 18 (int) | Điểm: 9.50 (float)
# • da_truong_thanh(tuoi) → returns True if tuoi ≥ 18
# • diem_hoan_hao(diem) → returns True if diem == 10.0
# •	Use type(...).name to print types.
# Example Output:
# [Nguyen Van A] | Tuổi: 18 (int) | Điểm: 9.50 (float)
# Trưởng thành: True | Điểm hoàn hảo: False
# Technical Constraints (applied to all 5 exercises):
# •	Do not use: if, elif, else, for, while.
# •	Use instead:
# • List indexing (lst[True], lst[False])
# • Boolean arithmetic (True == 1, False == 0)
# • try–except for validation
# • f-string for formatting
# • type(...).name for type display


def exercise_25():
    try:
        ten = input("nhap ten: ")
        tuoi_input = input("nhap tuoi: ")
        diem_input = input("nhap diem tu 1 - 10: ")
        tuoi = int(tuoi_input)
        diem = float(diem_input)

        def dinh_dang_thong_tin(n, t, d):
            return (
                f"[{n}] | "
                f"Tuổi: {t} ({type(t).__name__}) | "
                f"Điểm: {d:.2f} ({type(d).__name__})"
            )

        def da_truong_thanh(t):
            return t >= 18

        def diem_hoan_hao(d):
            return d == 10.0

        info_str = dinh_dang_thong_tin(ten, tuoi, diem)
        print(info_str)
        print(
            f"Trưởng thành: {da_truong_thanh(tuoi)} | Điểm hoàn hảo: {diem_hoan_hao(diem)}"
        )

    except ValueError:
        print("error")


exercise_25()


# Exercise 26:

# Viết chương trình cho phép người dùng nhập vào 3 số thực a,b,c Kiểm tra xem dữ liệu nhập vào cho 3 biến đã đúng định dạng hay chưa. Sau đó thực hiện các yêu cầu sau:

# Viết hàm sum(x,y) thực hiện việc tính tổng hai số a và b sau đó in ra kết quả

# Viết hàm dif(x,y) thực hiện việc tính hiệu hai số b và c sau đó in ra kết quả

# Viết hàm mul(x,y,z) thực hiện việc tính tích ba số a , b và c sau đó in ra kết quả

# Viết hàm max_value(x,y,z) tìm số lớn nhất trong ba số a,b,c và in ra kết quả

# Viết hàm binh_phuong(x) để tính và in ra giá trị của a,b,c sau khi bình phương.

# Viết hàm lap_Phuong(x) để tính và in ra giá trị của a,b,c sau khi lập phương


# Gọi hàm và truyền vào các đối số đã nhập từ bàn phím
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
            if y > m:
                m = y
            if z > m:
                m = z
            print(f"Số lớn nhất là {m}")
            # if x >= y and x >= z:
            #     print(f"Số lớn nhất là {x}")
            # elif y >= x and y >= z:
            #     print(f"Số lớn nhất là {y}")
            # else:
            #     print(f"Số lớn nhất là {z}")
            # print(f"Số lớn nhất trong ba số là: {max(x, y, z)}")
        def binh_phuong(x):
            return x**2
        def lap_Phuong(x):
            return x**3
        sum_calc(a, b)
        dif(b, c)
        mul(a, b, c)
        max_value(a, b, c)
        print(
            f"Bình phương: a={binh_phuong(a)}, b={binh_phuong(b)}, c={binh_phuong(c)}"
        )
        print(f"Lập phương: a={lap_Phuong(a)}, b={lap_Phuong(b)}, c={lap_Phuong(c)}")
    except ValueError:
        print("error")


bai_tap_26()
