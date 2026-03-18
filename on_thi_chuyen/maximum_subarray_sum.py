n = int(input())
arr = list(map(int,input().split()))
max_sum = arr[0]
curr = 0
for i in arr:
    curr = max(curr + i,i)
    max_sum = max(max_sum, curr)

print(max_sum)