t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if a + b > n:
        print("NO")
        continue

    p1 = list(range(1, n + 1))
    p2 = []

    # player1 thắng
    for i in range(a):
        p2.append(n - i)

    # hòa
    for i in range(a, a + (n - a - b)):
        p2.append(i + 1)

    # player2 thắng
    for i in range(b):
        p2.append(i + 1)

    if len(set(p2)) != n:
        print("NO")
        continue

    print("YES")
    print(*p1)
    print(*p2)