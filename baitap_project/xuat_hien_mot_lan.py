from python_library import array_input
def count():
    with open('input.txt','r') as f:
        n = int(f.readline())
        ar = list(map(int, f.readline().split()))
    d = {}
    c = ""
    for i in ar:
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] += 1
    for i in d:
        if d[i] == 1:
            c += str(i) + " "
    with open('output.txt','w') as f:
        f.write(c)
count()

