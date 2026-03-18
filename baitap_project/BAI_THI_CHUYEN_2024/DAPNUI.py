# import time
# def dap_nui():
#     with open('DAPNUI.INP', 'r') as f:
#         n = int(f.readline().strip())
#         b = list(map(int, f.readline().split()))

#     print(len(b))
#     left = [0] * n
#     arr = b[:]
#     for i in range(1, n):
#         if arr[i] <= arr[i - 1]:
#             left[i] = left[i - 1] + (arr[i - 1] + 1 - arr[i])
#             arr[i] = arr[i - 1] + 1
#         else:
#             left[i] = left[i - 1]
#     right = [0] * n
#     arr = b[:]
#     for i in range(n - 2, -1, -1):
#         if arr[i] <= arr[i + 1]:
#             right[i] = right[i + 1] + (arr[i + 1] + 1 - arr[i])
#             arr[i] = arr[i + 1] + 1
#         else:
#             right[i] = right[i + 1]
#     min_chi_phi = float('inf')
#     for i in range(n):
#         min_chi_phi = min(min_chi_phi, left[i] + right[i])
#     with open('DAPNUI.OUT', 'w') as f:
#         f.write(str(min_chi_phi))
# start = time.time()
# dap_nui()
# end = time.time()
# print(end - start)

# def dap_nui():
#     max_idx = 0
#     count = 0
#     with open('DAPNUI.INP', 'r') as f:
#         n = list(map(int, f.readline().split()))
#     max_value = n[0]
#     arr_len = len(n)
#     for i in range(arr_len):
#         if max_value < n[i]:
#             max_value = n[i]
#             max_idx = i

#     for i in range(max_idx - 1):
#         if n[i] >= n[i + 1]:
#             count = count + n[i] - n[i + 1] + 1
#             n[i + 1] = n[i] + 1

#     for i in range(arr_len - 1, max_idx + 1, -1):
#         if n[i] >= n[i - 1]:
#             count = count + n[i] - n[i - 1] + 1
#             n[i-1] = n[i] + 1
    
#     return (n, count)

# print(dap_nui())

def build_best_mountain(b):
    n = len(b)
    # left pass
    left_cost = [0]*n
    left_val = b[:]   # giá trị sau điều chỉnh prefix
    for i in range(1, n):
        if left_val[i] <= left_val[i-1]:
            need = left_val[i-1] + 1 - left_val[i]
            left_cost[i] = left_cost[i-1] + need
            left_val[i] = left_val[i-1] + 1
        else:
            left_cost[i] = left_cost[i-1]

    # right pass
    right_cost = [0]*n
    right_val = b[:]  # giá trị sau điều chỉnh suffix
    for i in range(n-2, -1, -1):
        if right_val[i] <= right_val[i+1]:
            need = right_val[i+1] + 1 - right_val[i]
            right_cost[i] = right_cost[i+1] + need
            right_val[i] = right_val[i+1] + 1
        else:
            right_cost[i] = right_cost[i+1]

    best_cost = 10**30
    best_peak = 0
    best_seq = None

    for i in range(n):
        # loại bỏ phần tăng ở đỉnh (để không đếm 2 lần)
        left_excl = left_cost[i] - (left_val[i] - b[i])
        right_excl = right_cost[i] - (right_val[i] - b[i])
        V = max(left_val[i], right_val[i])   # chiều cao cần tại đỉnh
        total = left_excl + right_excl + (V - b[i])

        if total < best_cost:
            best_cost = total
            best_peak = i
            # dựng dãy kết quả từ peak và V
            res = [0]*n
            res[i] = V
            # trái
            for j in range(i-1, -1, -1):
                res[j] = max(b[j], res[j+1] - 1)
            # phải
            for j in range(i+1, n):
                res[j] = max(b[j], res[j-1] - 1)
            best_seq = res

    return best_cost, best_peak, best_seq

# ví ụ:
b = [3,4,5,6,5,1]
cost, peak, seq = build_best_mountain(b)
print(cost)   # sẽ in: 4 2 [2,3,4,3]
