n = int(input())
def bianary(cur,count):
    if count == n:
        print(cur)
        return
    bianary(cur + "1",count + 1)
    bianary(cur + "0", count + 1)

bianary("",0)