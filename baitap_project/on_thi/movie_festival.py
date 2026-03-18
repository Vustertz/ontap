n = int(input())
movie = []
cur_end,ans = 0,0
for i in range(n):
    a,b = list(map(int,input().split()))
    movie.append((a,b))
movie.sort(key=lambda x: x[1])
for start,end in movie:
    if cur_end <= start:    
        ans += 1
        cur_end = end

print(ans)



        