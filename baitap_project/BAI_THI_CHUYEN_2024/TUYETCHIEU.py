import time

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