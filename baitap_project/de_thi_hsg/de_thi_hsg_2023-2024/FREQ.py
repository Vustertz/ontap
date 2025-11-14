def freg():
    with open('FREQ.INP','r') as f:
        n = int(f.readline())
        ar = list(map(int, f.readline().split()))
    frequent = {}
    for i in ar:
        if i not in frequent:
            frequent[i] = 1
        elif i in frequent:
            frequent[i] += 1
    max_key = -1
    max_value= -1
    for key, value in frequent.items():
        if value > max_value or (value == max_value and key > max_key):
            max_value = value
            max_key = key
    with open('FREQ.OUT','w') as f:
        f.write(f"{max_key} {max_value}")
freg()