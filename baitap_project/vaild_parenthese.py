s = str(input())
def kiem_tra_dong_ngoac(s):
    stack = []
    cap = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for ch in s:
        if ch in cap:
            stack.append(cap[ch])
        elif ch in cap.values():
            if not stack or ch != stack[-1]:
                return False
            stack.pop()
    return not stack

print(kiem_tra_dong_ngoac(s))