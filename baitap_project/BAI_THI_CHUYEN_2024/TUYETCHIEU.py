import time
def tuyet_chieu():
    d = []
    with open('TUYETCHIEU.INP','r') as f:
        [n, k] = f.readline().split()
        c = list(map(int, f.readline().split()))
    for i in range(len(c)):
        end = min(i + int(k),len(c))
        for j in range(i + 1,end):
            if c[j] == c[i]:
                d.append(c[i])
    # with open('TUYETCHIEU.OUT','w') as f:
    if not d:
        print('-1')
    else:
        print(str(min(d)))


def tuyet_chieu1():
    with open('TUYETCHIEU.INP','r') as f:
        [n, k] = f.readline().split()
        c = list(map(int, f.readline().split()))
    print(len(c))
    check = {}
    k = int(k)
    vi_pham = []
    for i, val in enumerate(c):
        if val not in check:
            check[val] = i
        elif val in check:
            a = int(i) - int(check[val])
            if a < k:
                vi_pham.append(val)
            else:
                check[val] = i
    with open('TUYETCHIEU.OUT') as f:
        if len(vi_pham) == 0:
            f.write('-1')
        else:
            f.write(str(min(vi_pham)))
    
start = time.time()
tuyet_chieu1()
end = time.time()
print(end - start)