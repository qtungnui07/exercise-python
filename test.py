# # # n=int(input())
# # # def fb(n):
# # #     if n>=5:
# # #         return True
# # #     return False
# # # if fb(n):
# # #    print("lon hon 5")
# # # else: print("nho hon 5") 


# # def bai_2():
# #     print("\n--- BÀI 2 ---")
# #     # 1. Nhập danh sách email (Ví dụ: an@gmail.com, binh@yahoo.com, an@outlook.com) [cite: 12]
# #     raw_input = input("Nhập danh sách email (cách nhau bởi dấu phẩy): ")
    
# #     # Tách chuỗi thành danh sách
# #     email_list = raw_input.split(',')
    
# #     domain_counts = {}

# #     print("\nKết quả thống kê:")
# #     for email in email_list:
# #         # 2. Chuẩn hóa dữ liệu: Chữ thường và loại bỏ khoảng trắng thừa [cite: 14, 15, 16]
# #         clean_email = email.strip().lower()
        
# #         # Kiểm tra tính hợp lệ cơ bản (phải có @)
# #         if '@' in clean_email:
# #             # 3. Trích xuất tên miền (phần sau @) [cite: 17]
# #             domain = clean_email.split('@')[0]
# #             # name = clean_email.split('@')[0]
            
# #             # 4. Đếm tần suất dùng Dictionary [cite: 18]
# #             if domain in domain_counts:
# #                 domain_counts[domain] += 1
# #             else:
# #                 domain_counts[domain] = 1
    
# #     # 5. In kết quả [cite: 19, 20]
# #     for domain, count in domain_counts.items():
# #         print(f"Domain: {domain} | Số lượng: {count}")
        
# #     # for name in clean_email:
# #     #     print(f"{name}")
# # # Chạy thử hàm với dữ liệu mẫu: an@gmail.com,  BINH@yahoo.com, an@OUTLOOK.com, lan@gmail.com
# # bai_2()



# # #hello world
# # print("ABCD")


# n=int(input())
# a=list(map(int,input().split()))
# if len(a)==n:
#     for i in range(n-1):
#         m=i
#         for j in range(i+1,n):
#             if a[j]>a[m]:m=j
#         a[i],a[m]=a[m],a[i]
#     d=[]
#     for x in a:
#         if x not in d:d.append(x)
#     if len(d)>=3:
#         v=d[2]
#         print(v)
#         for i in range(n):
#             if a[i]==v:print(i)
#     else:
#         print("k du 3 gia tri khac nhau")


s=input()
x=s[::-1]
print(x)