n = int(input())
ans = 0
p = 5
while p <= n:
    ans += n // p
    p *= 5
print(ans)