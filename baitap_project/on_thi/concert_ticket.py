a,b = map(int,input().split())
ticket = list(map(int,input().split()))
custom = list(map(int,input().split()))
ticket.sort()
for i in range(b):
    l = 0
    r = len(ticket)-1
    pos = -1
    while l <= r:
        m = (l+r)//2
        if ticket[m] <= custom[i]:
            pos = m
            l = m+1
        else:
            r = m-1
    if pos == -1:
        print(-1)
    else:
        print(ticket[pos])
        ticket.pop(pos)
