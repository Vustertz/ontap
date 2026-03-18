n = str(input())
di = {}
key_val = ""
for c in n:
    di[c] = 1 + di.get(c,0)
count = 0
for key in di:
    if di[key] % 2 == 1:
        count += 1
        key_val = key
if count >= 2:
    print('NO SOLUTION')
else:
    left = []
    if key_val:
        mid = key_val*di[key_val]
        di[key_val] = 0
    else:
        mid = ""
    for i in di:
        left.append(i * (di[i] // 2))
    left = "".join(left)
    print(left + mid + left[::-1] )

        