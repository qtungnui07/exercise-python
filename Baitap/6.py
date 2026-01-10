def cau1():
    print("Câu 1")
def cau2():
    print("Câu 2")
def cau3():
    print("Câu 3")
def cau4():
    print("Câu 4")
def cau5():
    print("Câu 5")
def main():
    while True:
        print("MENU".center(30,"="))
        print("1. Câu 1:")
        print("2. Câu 2:")
        print("3. Câu 3:")
        print("4. Câu 4:")
        print("5. Câu 5:")
        print("0. Thoát")
        choice = input("Nhập lựa chọn: ")
        if choice == "1":cau1()
        elif choice == "2":cau2()
        elif choice == "3":cau3()
        elif choice == "4":cau4()
        elif choice == "5":cau5()
        elif choice == "0":break
        else:print("Lựa chọn không hợp lệ!")
main()
