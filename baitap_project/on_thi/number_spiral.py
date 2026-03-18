n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    maxx = max(x, y)
    if x > y:
        if maxx % 2 == 1:
            print(((maxx-1)**2 + maxx**2)//2 + 1 + y - x)
        else:
            print(((maxx-1)**2 + maxx**2)//2 + 1 + y)
    else:
        if maxx % 2 == 1:
            print(((maxx-1)**2 + maxx**2)//2 + 1 + y - x)
        else:
            print(((maxx-1)**2 + maxx**2)//2 + 1 - x)
        