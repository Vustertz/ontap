s = str(input())
l = 0
r = len(s) - 1
checked = False
length = 0
while l != r:
    if s[l] == s[r]:
        length += 2
        l += 1
        r -= 1
        continue
    else:
        if s[l + 1] == s[r]:
            length += 2
            l += 1
            continue
        elif s[r - 1] == s[l]:
            length += 2
            r -= 1
            continue
        l += 1
    if l == r or l + 1 == r:
        length += 1

print(len(s) - length - 1)
    