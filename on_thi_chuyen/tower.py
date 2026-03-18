def bianary(curr):
    global ans
    l = 0
    r = ans - 1
    while l <= r:
        m = (l + r) // 2    
        if tower[m] > curr:
            r = m - 1
        else:
            l = m + 1
    if l < ans:
        tower[l] = curr
    else:
        tower.append(curr)
        ans += 1
n = int(input())
arr = list(map(int,input().split()))
tower = []
ans = 0
for i in arr:
    bianary(i)
print(ans)

