n = int(input())
event = []
max_custom = 0
cur_custom = 0
for i in range(n):
    a,b = list(map(int,input().split()))
    event.append((a,1))
    event.append((b,-1))
event.sort()
for time,visit in event:
    cur_custom += visit
    if cur_custom > max_custom:
        max_custom = cur_custom
print(max_custom)
