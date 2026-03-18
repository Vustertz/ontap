a, b = list(map(int,input().split()))
ans = 0
temp = 0
for i in range(a,b + 1):
    temp = int(i**0.5)
    if temp**2 == i:
        ans += 1
    
print(ans)