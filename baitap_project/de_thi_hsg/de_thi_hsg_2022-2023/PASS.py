def passw():
    with open('PASS.INP','r') as f:
        n = f.readline()
        k = f.readline()
    passout = ""
    for i in range(1, len(n) - 1):
        if n[i + 1] == k and n[i - 1] == k and n[i] != k:
            passout += n[i]
    with open('PASS.OUT','w') as f:
        if len(passout) == 0:
            f.write('NOT FOUND')
        else:
            f.write(passout)

print(passw())