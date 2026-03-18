from python_library import array_input
def tong():   
    return sum(array_input)

def sobe_solon():
    a = array_input
    print(min(a),' ',max(a))

def dem():
    a = array_input
    x = int(input())
    return(a.count(x))

def tim_so_chan():
    a = array_input
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return(b)

def sap_xep():
    a = array_input()
    return sorted(a)

def prime():
    a = array_input()
    prime_arr = []

    def prime_num():
        if i < 2:
            return False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                return False
        return True

    for i in a:
        if prime_num(i):
            prime_arr.append(i)

    return sum(prime_arr)

def tach_list():
    a = array_input()
    list_chan = []
    list_le = []
    for i in a:
        if i % 2 == 0:
            list_chan.append(i)
        else:
            list_le.append(i)
    return list_chan, list_le

def so_xuat():
    a = array_input()
    max_count = 0
    max_so = None
    for i in a:
        if a.count(i) > max_count:
            max_count = a.count(i)
            max_so = i
    return max_so , max_count

def xoa_mang():
    a = array_input()
    arr = []
    for i in a:
        if i not in arr:
            arr.append(i)
    return arr

def ghep_list():
    a = array_input()
    b = array_input()
    c = a + b
    return sorted(c)

def trung_binh():
    a = array_input()
    if len(a) == 0:
        return 0    
    return sum(a) / len(a)

def tong_chan_le():
    a = array_input()
    chan = 0
    le = 0
    for i in range(0, len(a)):
        if i % 2 == 0:
            chan += a[i]
        else:
            le += a[i]
    return chan, le

def tong_hop():
    a = array_input()
    b = array_input()
    mang_xoa = []
    c = a + b
    for i in c:
        if i not in mang_xoa:
            mang_xoa.append(i)
    return sorted(mang_xoa)
