from python_library import array_input
from python_library import read_file
from python_library import readline_file
def ghi_danh_sach():
    a = array_input()
    with open("output.txt","w", encoding="uft-8") as f:
        for i in range(len(a)):
            f.write(f"phan tu thu {i + 1} la: {a[i]}" + "\n")

def doc_dictionary():
    n = int(input("nhap so luong key: "))
    d = {}
    for i in range(n):
        k = input("nhap key: ")
        v = input("nhap vaule: ")
        d[k] = v
    with open("output.txt","w", encoding="utf-8") as f:
        for k, v in d.items():
            f.write(f"key la {k} voi vaule {v}" + "\n")

def van_ban():
    with open("output.txt","w", encoding="utf-8") as f:
        while True:
            s = str(input())
            if s:
                f.write(s + "\n")
            else:
                break

def sao_chep():
    with open("input.txt","r", encoding="utf-8")as f:
        with open("copy.txt", "w", encoding="utf-8") as a:   
            for i in f:
                a.write(i)



        