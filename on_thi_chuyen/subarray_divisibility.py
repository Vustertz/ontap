import time 
with open('input.txt','r') as f:
    n = int(f.readline())
    arr = list(map(int,f.readline().split()))
start = time.time()
count = [0]*n
count[0] = 1
prefix = 0
ans = 0
for x in arr:
    prefix = (prefix + x) % n
    ans += count[prefix]
    count[prefix] += 1
print(ans)
end = time.time()
print(end - start)