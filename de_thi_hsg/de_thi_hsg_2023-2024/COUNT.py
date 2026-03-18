def count():
    check = 0
    with open('COUNT.INP','r') as f:
        a = int(f.readline())
        for i in f:
            n = int(i)
            if n % 90 == 0:
                check += 1
    with open('COUNT.OUT','w') as f:
        f.write(str(check))
count()