def luy_thua(a, n):
    if n == 0:
        return 1
    half = luy_thua(a, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return a * half * half

a = int(input()) 
n = int(input())
print(luy_thua(a, n))