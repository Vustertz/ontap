with open('TUYETCHIEU.INP','r') as f:
    [n, m] = f.readline().split()
    print(n,m)
    for i in f:
        c = list(map(int, i.split()))
        print(c)
