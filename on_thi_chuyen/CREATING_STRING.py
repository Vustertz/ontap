s = sorted(input())
n = len(s)
used = [False]*n
res = []
def backtrack(path):
    if len(path) == n:
        res.append("".join(path))
        return
    for i in range(n):
        if used[i]:
            continue
        if i>0 and s[i]==s[i-1] and not used[i-1]:
            continue
        used[i] = True
        path.append(s[i])
        backtrack(path)
        path.pop()
        used[i] = False
backtrack([])
print(len(res))
for x in res:
    print(x)