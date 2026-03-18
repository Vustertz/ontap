def loc_nuoc():
    with open('LOCNUOC.INP','r') as f:
        [n, m] = f.readline().split()
        luong_nuoc = list(map(int, f.readline().split()))
        dung_tich = list(map(int, f.readline().split()))
    c = 0
    output = []
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
        e = " ".join(map(str, output))
    with open('LOCNUOC.OUT','w') as f:
        f.write(e)
loc_nuoc()