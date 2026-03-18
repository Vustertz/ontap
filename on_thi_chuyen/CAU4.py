n = int(input())
arr = list(map(int,input().split()))
ans = 0
for i in range(n):
    min_temp = arr[i]
    max_temp = arr[i]
    for j in range(i,n):
        if arr[j] < min_temp:
            min_temp = arr[j]
        if arr[j] > max_temp :
            max_temp = arr[j]
        ans += abs(min_temp - max_temp)

print(ans)