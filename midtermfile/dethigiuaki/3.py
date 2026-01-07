# --- PHẦN 1: ĐỌC FILE (Giữ nguyên) ---
def read_transactions(filename):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                parts = line.split(',')
                transaction = {
                    'id': int(parts[0]),
                    'user': parts[1].strip(),
                    'amount': int(parts[2]),
                    'time': parts[3].strip() 
                }
                data.append(transaction)
        return data
    except FileNotFoundError:
        return []

transactions = read_transactions('data.txt')

if transactions:
    # --- YÊU CẦU 1 & 2 (Giữ nguyên vì không liên quan ngày giờ) ---
    user_totals = {}
    for t in transactions:
        u = t['user']
        user_totals[u] = user_totals.get(u, 0) + t['amount']
    
    print(f"1. Tổng tiền: {user_totals}")
    print(f"2. Top 1: {max(user_totals, key=user_totals.get)}")

    # --- YÊU CẦU 3: XỬ LÝ GIỜ (KHÔNG DÙNG DATETIME) ---
    hour_totals = {}
    
    for t in transactions:
        time_str = t['time'] # Ví dụ: "2025-10-28 09:10"
        
        # BƯỚC XỬ LÝ CHUỖI THAY CHO DATETIME:
        # 1. Tách bằng khoảng trắng để lấy phần giờ phút: "2025-10-28" và "09:10"
        split_space = time_str.split() 
        time_part = split_space[1] # Lấy "09:10"
        
        # 2. Tách bằng dấu hai chấm để lấy giờ: "09" và "10"
        split_colon = time_part.split(':')
        hour = split_colon[0] # Lấy "09"
        
        # Tạo key, ví dụ "09h"
        hour_key = hour + "h"
        
        # Cộng dồn như bình thường
        if hour_key in hour_totals:
            hour_totals[hour_key] += t['amount']
        else:
            hour_totals[hour_key] = t['amount']

    print("3. Tổng tiền theo khung giờ:", end=" ")
    for h, total in hour_totals.items():
        print(f"{h}: {total}", end="  ")
    print()

    # --- YÊU CẦU 4 (Giữ nguyên) ---
    # Hàm này chỉ tính toán số tiền, không liên quan ngày giờ nên không đổi
    def detect_anomaly(data, threshold):
        user_sums = {}
        user_counts = {}
        for t in data:
            u = t['user']
            user_sums[u] = user_sums.get(u, 0) + t['amount']
            user_counts[u] = user_counts.get(u, 0) + 1
            
        anomalies = []
        for t in data:
            u = t['user']
            avg = user_sums[u] / user_counts[u]
            if t['amount'] > threshold or t['amount'] > (3 * avg):
                anomalies.append(t)
        return anomalies

    print("4. Bất thường:", detect_anomaly(transactions, 600))