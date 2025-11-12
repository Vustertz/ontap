def pword():
    with open('PWORD.INP','r') as f:
        for i in f:
            n = i
    count = 0
    for i in n:
        if i.isdigit():
            if int(i) % 2 == 0:
                count += int(i)
    with open('PWORD.OUT','w') as f:
        f.write(str(count))
pword()