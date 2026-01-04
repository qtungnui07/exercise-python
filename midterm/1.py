def bai_2_xu_ly_chuoi():
    # 1. Nhập vào một chuỗi
    print("Mời bạn nhập chuỗi văn bản:")
    text = input()
    
    # Ví dụ mẫu nếu bạn muốn test nhanh mà không cần nhập:
    # text = "Python is great! Python is easy, and Python is powerful."

    if not text:
        print("Chuỗi rỗng.")
        return

    # 2. Chuẩn hóa chuỗi
    # - Chuyển tất cả thành chữ thường
    text_lower = text.lower()
    
    # - Loại bỏ các ký tự không phải chữ cái hoặc khoảng trắng
    #   Dùng list comprehension để giữ lại ký tự là chữ (isalpha) hoặc dấu cách (isspace)
    cleaned_text = "".join([char for char in text_lower if char.isalpha() or char.isspace()])

    # 3. Tách chuỗi thành danh sách các từ
    words_list = cleaned_text.split()

    # 4. Đếm tần suất xuất hiện của từng từ và lưu vào dict
    word_dict = {}
    for word in words_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # 5. In ra top 5 từ xuất hiện nhiều nhất
    #   Sắp xếp dictionary theo value (số lần xuất hiện) giảm dần
    #   key=lambda item: item[1] nghĩa là sắp xếp dựa trên giá trị (value) của phần tử
    sorted_words = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)

    #   Lấy 5 từ đầu tiên
    top_5_words = sorted_words[:5]

    print("\nOutput")
    for word, count in top_5_words:
        print(f"Từ: {word} | Số lần: {count}")

# Gọi hàm để chạy chương trình
if __name__ == "__main__":
    bai_2_xu_ly_chuoi()