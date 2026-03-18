n = list(map(str, input().split()))
di = {}
for i in n:
    a = len(i)
    di[a] = 1 + di.get(a,0)

print(len(di))
for i in di:
    print(i, di[i])