n = int(input())
sett = n*(n+1)//2
target = sett//2
count = 0
a,b = [],[]
if sett % 2 == 1:
    print("NO")
else:
    print("YES")
    for i in range(n,0,-1):
        if i <= target:
            a.append(str(i))
            target -= i
            count += 1
        else:
            b.append(str(i))
    print(count)
    print(" ".join(a))
    print(n - count)
    print(" ".join(b))