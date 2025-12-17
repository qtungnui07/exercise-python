def kiem_tra_toi_uu(n, matrix):
    """
    Hàm kiểm tra ma trận đối xứng qua cả 2 đường chéo.
    Tối ưu: Chỉ duyệt tam giác trên (phần tử phía trên đường chéo chính).
    """
    # Chỉ cần duyệt các phần tử nằm TRÊN đường chéo chính
    # i chạy từ 0 đến n-1, j chạy từ i+1 đến n-1
    for i in range(n):
        for j in range(i + 1, n): 
            
            # 1. Kiểm tra đối xứng qua đường chéo CHÍNH
            # A[i][j] phải bằng A[j][i]
            if matrix[i][j] != matrix[j][i]:
                return False
            
            # 2. Kiểm tra đối xứng qua đường chéo PHỤ
            # Đối xứng của (i, j) qua đường chéo phụ là (n-1-j, n-1-i)
            # Ta kiểm tra xem phần tử hiện tại có bằng phần tử đối xứng qua chéo phụ không
            if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
                return False
                
    return True

# --- PHẦN CHƯƠNG TRÌNH CHÍNH (Main Driver) ---
if __name__ == "__main__":
    try:
        # 1. Nhập kích thước n
        print("Nhập kích thước n của ma trận vuông:")
        n = int(input())

        # 2. Nhập ma trận
        print(f"Nhập {n} dòng, mỗi dòng chứa {n} số cách nhau bởi khoảng trắng:")
        matrix = []
        for i in range(n):
            # Đọc một dòng, tách chuỗi và chuyển thành số nguyên
            row = list(map(int, input().split()))
            
            # Kiểm tra lỗi nhập liệu (nếu nhập thiếu/thừa số)
            if len(row) != n:
                print(f"Lỗi: Dòng thứ {i+1} bạn nhập không đủ {n} số!")
                exit()
            matrix.append(row)

        # 3. Gọi hàm kiểm tra tối ưu
        ket_qua = kiem_tra_toi_uu(n, matrix)

        # 4. In kết quả
        print("-" * 30)
        if ket_qua:
            print("KẾT QUẢ: Đây LÀ ma trận đối xứng (thỏa mãn cả 2 đường chéo).")
        else:
            print("KẾT QUẢ: Đây KHÔNG PHẢI là ma trận đối xứng.")

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập các số nguyên hợp lệ.")