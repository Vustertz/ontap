n, m = map(int, input().split())
a = list(map(int, input().split()))
def check(k):
    left = sorted(a[:k])
    right = sorted(a[k:])  
    i = 0
    j = 0
    cnt = 0
    while i < k and j < len(right):
        if left[i] < right[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            j += 1
    return cnt >= k
l, r = 0, n//2
ans = -1
while l <= r:
    mid = (l+r)//2
    if check(mid):
        ans = mid
        l = mid+1
    else:
        r = mid-1
print(ans if ans>0 else -1)