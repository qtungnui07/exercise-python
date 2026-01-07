# Bài 2: Xử lý chuỗi và từ điển (4 điểm)
# Yêu câu:
# 1. Nhập vào một chuỗi gồm nhiều câu (có thể chứa dấu chấm, dấu phẩy, ký tự đặc biệt).
# 2. Chuẩn hóa chuỗi:
# Chuyển tất cả thành chữ thường.
# Loại bỏ các ký tự không phải chữ cái hoặc khoảng trắng.
# 3. Tách chuỗi thành danh sách các từ.
# 4. Đếm tần suất xuất hiện của từng từ và lưu kết quả vào một dict.
# 5. In ra top 5 từ xuất hiện nhiều nhất, theo định dạng: Từ: | Số lần: <số lần> Ví du: Python is great! Python is easy, and Python is powerful.
# Output
# Từ: python | Số lần: 3
# Từ: is | Số lần: 3
# Từ: great | Số lần: 1
# 1. Nhập chuỗi
s = input("Nhập văn bản: ")

# 2. Chuẩn hóa chuỗi
s = s.lower()

# Tạo một chuỗi mới chỉ chứa chữ cái và khoảng trắng
# Ký tự đặc biệt sẽ được thay bằng khoảng trắng để tránh dính từ (vd: "hello,world" -> "hello world")
s_clean = ""
for char in s:
    if char.isalpha() or char.isspace():
        s_clean += char
    else:
        s_clean += " " 

# 3. Tách chuỗi thành danh sách
# split() mặc định sẽ tự động loại bỏ các khoảng trắng thừa
words = s_clean.split()

# 4. Đếm tần suất (dùng Dictionary)
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

# 5. Sắp xếp và in Top 5
# Sắp xếp dictionary theo value (số lần xuất hiện) giảm dần
# d.items() trả về danh sách các cặp (key, value)
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

# Dùng hàm min để lấy 5 hoặc ít hơn nếu danh sách từ không đủ 5
top_n = min(5, len(sorted_d))

for i in range(top_n):
    # sorted_d[i][0] là từ, sorted_d[i][1] là số lần
    print(f"Từ: {sorted_d[i][0]} | Số lần: {sorted_d[i][1]}")