T = int(input())
for _ in range(T):
    s = list(input().strip())
    n = len(s)

    # Duyệt từ phải sang trái
    i = n - 1
    while i >= 0 and s[i] == '1':
        s[i] = '0'
        i -= 1
    
    # Nếu tìm được vị trí để đặt '1'
    if i >= 0:
        s[i] = '1'
    
    print("".join(s))
