import time
def dap_nui():
    with open('DAPNUI.INP', 'r') as f:
        n = int(f.readline().strip())
        b = list(map(int, f.readline().split()))

    print(len(b))
    left = [0] * n
    arr = b[:]
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            left[i] = left[i - 1] + (arr[i - 1] + 1 - arr[i])
            arr[i] = arr[i - 1] + 1
        else:
            left[i] = left[i - 1]
    right = [0] * n
    arr = b[:]
    for i in range(n - 2, -1, -1):
        if arr[i] <= arr[i + 1]:
            right[i] = right[i + 1] + (arr[i + 1] + 1 - arr[i])
            arr[i] = arr[i + 1] + 1
        else:
            right[i] = right[i + 1]
    min_chi_phi = float('inf')
    for i in range(n):
        min_chi_phi = min(min_chi_phi, left[i] + right[i])
    with open('DAPNUI.OUT', 'w') as f:
        f.write(str(min_chi_phi))
start = time.time()
dap_nui()
end = time.time()
print(end - start)