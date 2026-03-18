a,b = list(map(int,input().split()))
arr = []
for i in range(a):
    v = list(map(str,input()))
    arr.append(v)
letter = ['A','B','C','D']
for i in range(a):
    for j in range(b):
        for c in letter:
            if c == arr[i][j]:
                continue
            elif i > 0 and c == arr[i - 1][j]:
                continue
            elif j > 0 and c == arr[i][j - 1]:
                continue
            arr[i][j] = c
            break
for i in arr:
    print("".join(i))