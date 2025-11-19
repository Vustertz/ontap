def dao_nguoc():
    with open('input.txt','r') as f:
        a = f.readline().split()
    for i in range(len(a)):
        b = a[i]
        a[i] = b[::-1]
    c = " ".join(a)
    with open('output.txt','w') as f:
        f.write(c)

dao_nguoc()