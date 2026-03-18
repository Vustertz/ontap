def pumks():
    with open('PUMPKS.INP', 'r') as f:
        arr = list(map(int, f.readline().split()))
    tong = 0
    best = 0  
    for val in arr:
        tong += val
        if best == 0:
            best = tong
        else:
            if abs(tong - 200) < abs(best - 200):
                best = tong
            elif abs(tong - 200) == abs(best - 200) and tong > best:
                best = tong
    with open('PUMPKS.OUT', 'w') as f:
        f.write(str(best))
pumks()
