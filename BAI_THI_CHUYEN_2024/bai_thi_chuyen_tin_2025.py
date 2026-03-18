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
    with open('DAPNUI.INP','r') as f:
        for i in f:
            n = i
            b = list(map(int, i.split()))
    e = len(b) // 2
    a = b[:e]
    c = b[e:]
    chi_phi = 0
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            while a[i] >= a[i + 1]:
                a[i + 1] += 1
                chi_phi += 1
    for i in range(len(c) - 1,0, -1): 
        if c[i] >= c[i - 1]:
            while c[i] >= c[i - 1]:
                    c[i - 1] += 1
                    chi_phi += 1
    with open('DAPNUI.OUT','w') as f:
        f.write(chi_phi)

def loc_nuoc():
    c = 0
    a = []
    luong_nuoc = []
    dung_tich = []
    output = []
    with open('LOCNUOC.INP','r') as f:
        for i in f:
            a = list(map(int, i.spilt()))
            luong_nuoc = list(map(int, i.spilt()))
            dung_tich = list(map(int, i.spilt()))
    n = a[0]
    m = a[1]
    for i in range(n):
        a = int(input("luong nuoc "))
        luong_nuoc.append(a)

    for i in range(m):
        a = int(input("dung tich "))
        dung_tich.append(a)

    for i in range(len(dung_tich)):
        if sum(luong_nuoc) == 0:
            break
        for j in range(len(luong_nuoc)):
            if luong_nuoc[j] > dung_tich[i]:
                c += dung_tich[i]
                luong_nuoc[j] -= dung_tich[i]
            elif luong_nuoc[j] <= dung_tich[i]:
                c += luong_nuoc[j]
                luong_nuoc[j] = 0
        output.append(c)
        c = 0
    with open('LOCNUOC.OUT','w') as f:
        f.write(c)

tuyet_chieu()
