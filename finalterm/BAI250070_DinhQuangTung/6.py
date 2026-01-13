def b1():
    print()
def b2():
    print()
def b3():
    print()
def b4():
    print()
def b5():
    print()
def main():
    while True:
        print("MENU".center(30,"="))
        print("1. Cau 1:")
        print("2. Cau 2:")
        print("3. Cau 3:")
        print("4. Cau 4:")
        print("5. Cau 5:")
        print("0. Thoat")
        choice = input("Option: ")
        if choice == "1":b1()
        elif choice == "2":b2()
        elif choice == "3":b3()
        elif choice == "4":b4()
        elif choice == "5":b5()
        elif choice == "0":break
        else:print("nhap lai option: ")
main()
