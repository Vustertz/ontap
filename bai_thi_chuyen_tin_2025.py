def tuyet_chieu():
    d = []
    with open('TUYETCHIEU.INP','r') as f:
        for i in f:
            a = list(map(int, i.split()))
            c = list(map(int, i.split()))
    n = a[0]
    k = a[1]
    for i in range(len(c)):
        end = min(i + k,len(c))
        for j in range(i + 1,end):
            if c[j] == c[i]:
                d.append(c[i])
    with open('TUYETCHIEU.OUT','w') as f:
        if not d:
            f.write('-1')
        else:
            f.write(str(min(d)))
        
def dap_nui():
    n = int(input())
    b = []
    for i in range(n):
        a = int(input())
        b.append(a)
    for i in range((len(b) // 2)):
        if b[i] >= b[i + 1]:
            while b[i] >= b[i + 1]:
                if b[i + 1] > b[i]:
                    break
                else:
                    b[i + 1] += 1
    for i in range(len(b) // 2 - 1, -1):
        if b[i] >= b[i - 1]:
            while b[i] >= b[i + 1]:
                if b[i - 1] > b[i]:
                    break
                else:
                    b[i - 1] += 1
    return(b)
print(dap_nui())
