s = str(input())
n = len(s)
res = 1
temp = 1
for c in range(n - 1):
    if s[c] == s[c + 1]:
        temp += 1
        if temp > res:
            res = temp
    else:
        temp = 1
print(res)