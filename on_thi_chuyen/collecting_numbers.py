n = int(input())
arr = list(map(int,input().split()))
pos = {}
round = 1
for i in range(n):
    pos[arr[i]] = i

for i in range(1,n):
    if pos[i + 1] < pos[i]:
        round += 1

print(round)
