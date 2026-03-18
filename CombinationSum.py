with open('input.txt','r') as f:
    target = int(f.readline())
    nums = list(map(int, f.readline().split()))
result = []
length = len(nums)

def combination(i,cur,total):
    if total == target:
        result.append(cur.copy())
        return
    if i >= length or total > target:
        return

    cur.append(nums[i])
    combination(i,cur,total + nums[i])
    cur.pop()
    combination(i+1,cur,total)

combination(0,[],0)
print(result)