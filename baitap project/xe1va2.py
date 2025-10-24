def thue_xe(n):
    xeloai1 = 0
    xeloai2 = 0
    xeloai2 = n // 3
    check = n % 3
    if check == 1:
        xeloai1 = 1
    elif check == 2:
        xeloai1 = 1
    print("Xe loại 1 là: ", xeloai1)
    print("Xe loại 2 là: ", xeloai2)

n = int(input("Nhập số học sinh: "))
thue_xe(n)
