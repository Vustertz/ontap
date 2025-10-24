n = int(input())
def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)

print("gia thua cua ",n," la: ", giaithua(n))