def ynum():
    with open("YNUM.INP", "r") as f:
        k = int(f.readline().strip())
    if k <= 2:
        pos = k
    else:
        pos = 3 * k - 6
    with open("YNUM.OUT", "w") as f:
        f.write(str(pos))

ynum()
