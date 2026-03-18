from python_library import array_input
def length_of_lis(arr):
    if not arr:
        return 0
    
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def get_lis(arr):
    if not arr:
        return []
    
    dp = [1] * len(arr)
    parent = [-1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    # Find the index with maximum LIS length
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # Reconstruct the LIS
    lis = []
    current = max_index
    while current != -1:
        lis.insert(0, arr[current])
        current = parent[current]
    
    return lis


# Test cases
