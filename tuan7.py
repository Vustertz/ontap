def dem_ky_tu():
    a = str(input())
    with open("output.txt","w") as f:
        f.write(str(len(a)))

def dem_tu():
    a = str(input())
    b = a.split()
    return len(b)

def dao_chuoi():
    a = str(input())
    return a[::-1]

def kiem_tra_palindrome():
    a = str(input())
    a = a.lower()
    a = a.replace(" ", "")
    b = a[::-1]
    if a == b:
        return True
    else:
        return False
    
def dem_ki_tu_chi_tiet():
    a = str(input())
    ki_tu = {}
    for i in a:
        if i not in ki_tu:
            ki_tu[i] = 1
        elif i in ki_tu:
            ki_tu[i] += 1
    print(ki_tu)

def ky_tu_nhieu_nhat():
    a = str(input())
    ki_tu = {}
    b = 0
    c = ""
    for i in a:
        if i not in ki_tu:
            ki_tu[i] = 1
        elif i in ki_tu:
            ki_tu[i] += 1
    for i in ki_tu:
        if ki_tu[i] > b:
            b = ki_tu[i]
            c = i
    return b, c

def viet_hoa_tu():
    a = str(input())
    a = a.lower()
    b = a.split()
    c = []
    for i in b:
        d = i[0].upper() + i[1:]
        c.append(d)
    e = " ".join(c)
    return e

def viet_hoa_dau_cau():
    a = str(input())
    if not a:
        return ""
    b = a[0].upper() + a[1:]
    return(b)

def chuan_hoa_ten():
    a = str(input())
    a = a.lower()
    b = a.split()
    c = []
    if len(a) == 0:
        return(a)
    for i in b:
        d = i[0].upper() + i[1:]
        c.append(d)
    e = " ".join(c)
    return e

def dem_tu_chi_tiet():
    a = str(input())
    a = a.lower()
    b = a.split()
    c = {}
    if len(a) == 0:
        return(a)
    for i in b:
        if i not in c:
            c[i] = 1
        elif i in c:
            c[i] += 1
    return c

def tach_phan_mo_rong():
    a = str(input())
    if "." not in a:
        return False
    b = a.split(".")
    return b[-1]

def chua_chu_so():
    a = str(input())
    for i in a:
        if i.isdigit():
            return True
    return False

def sort_chu_cai():
    s = str(input())
    c = "".join(sorted(s))
    return c

dem_ky_tu()