def in_square():
    with open('INSQUARE.INP','r') as f:
        for i in f:
            c = list(map(int, i.split()))
    a = c[0]
    n = c[1]
    count = 0
    for i in range(n):
        if i**2 < a:
            continue
        elif i**2 >= a and i**2 <= n:
            count += 1
        elif i**2 > n:
            break
    with open('INSQUARE.OUT','w') as f:
        f.write(str(count))
in_square()