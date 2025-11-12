n = int(input("nhap so luong tien "))
coins = []
for i in range(n):
    v = int(input())
    coins.append(v)
X = int(input("Nhập số tiền cần đổi: "))

count = 0
for c in coins:
    count += X // c
    X %= c

print("Số tờ ít nhất:", count)