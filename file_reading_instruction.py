#length không cố định
with open('input.txt','r') as f:
    while True:
        line = f.readline()
        if not line:      
            break
        n = int(line)
        length = int(f.readline())
        arr = []
        for i in range(length):
            arr.append(int(f.readline()))
        print(n)
        print(length)
        print(arr)  

    