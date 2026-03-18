def giaithua(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * giaithua(n - 1)

n = int(input())
print(giaithua(n))