with open('input.txt','r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
height = -1
count = 0
for i in range(n-1,0,-1):
    if arr[i] > height:
        count += 1
        height = arr[i]
    
with open('output.txt','w') as j:
    j.write(str(count))