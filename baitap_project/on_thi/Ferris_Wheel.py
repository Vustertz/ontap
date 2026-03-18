a,b = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
l = 0
r = a - 1
ans = 0
while l <= r:
    if arr[l] + arr[r] <= b:
        l += 1
    r -= 1
    ans += 1

print(ans)