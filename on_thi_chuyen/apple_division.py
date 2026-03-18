n = int(input())
a = list(map(int, input().split()))
total = sum(a)
ans = 10**18
def dfs(i, sum1):
    global ans
    if i == n:
        sum2 = total - sum1
        ans = min(ans, abs(sum1 - sum2))
        return
    dfs(i + 1, sum1 + a[i])
    dfs(i + 1, sum1)
dfs(0, 0)
print(ans)