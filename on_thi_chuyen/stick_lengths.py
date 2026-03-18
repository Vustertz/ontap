n = int(input())
arr = list(map(int,input().split()))
arr.sort()
median = arr[(n-1) // 2]
cost = 0
for i in arr:
    cost += abs(i -  median)
print(cost)