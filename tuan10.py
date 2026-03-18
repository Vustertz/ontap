def ma_tran():
    a = str(input()).split()
    m = int(a[0])
    n = int(a[1])
    b =[]
    for i in range(m):
        row = list(map(int, input().split()))
        b.append(row)
    for row in b:
        print(*row)

def tong_ma_tran():
    a = str(input()).split()
    m = int(a[0])
    b =[]
    c = 0
    for i in range(m):
        row = list(map(int, input().split()))
        c += sum(row)
        b.append(row)
    return c

def min_max():
    a = str(input()).split()
    m = int(a[0])
    c = float('inf')
    d = float('-inf')
    for i in range(m):
        row = list(map(int, input().split()))
        if min(row) < c:
            c = min(row)
        if max(row) > d:
            d = max(row)
    return c , d

print(min_max())