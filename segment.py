def lower_bound(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid][0] < target:
            left = mid + 1
        else:
            right = mid
    return left

def max_subarray_sum_k(nums, K):
    prefix = [(0, -1)]  
    curr = 0
    best = -10**18

    for i, val in enumerate(nums):
        curr += val
        need = curr - K

        # tìm L sao cho prefix[L] gần nhất với need
        pos = lower_bound(prefix, need)

        # thử pos
        if pos < len(prefix):
            cand = curr - prefix[pos][0]
            if abs(cand - K) < abs(best - K) or (abs(cand - K) == abs(best - K) and cand > best):
                best = cand

        # thử pos - 1
        if pos > 0:
            cand = curr - prefix[pos-1][0]
            if abs(cand - K) 
            < abs(best - K) or (abs(cand - K) == abs(best - K) and cand > best):
                best = cand

        # chèn curr vào prefix sao cho vẫn giữ sorted
        l = lower_bound(prefix, curr)
        prefix.insert(l, (curr, i))

    return best
