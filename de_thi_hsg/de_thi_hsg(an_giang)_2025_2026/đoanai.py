with open('input.txt','r') as f:
    n = int(f.readline())
    arr = list(map(int,f.readline().split()))
res = [arr[0]]
temp = [arr[0]]
min_sum , temp_sum = arr[0],arr[0]
length,temp_length = 1,1
for i in range(n - 1):
    if arr[i] >= arr[i + 1]:
        temp_length += 1
        temp_sum += arr[i + 1]
        temp.append(arr[i + 1])
        if temp_length > length or (temp_length == length and temp_sum < min_sum):
            res = temp.copy()
            min_sum = temp_sum
            length = temp_length
    else:
        temp_length = 1
        temp_sum = arr[i + 1]
        temp = [arr[i + 1]]

with open('output.txt','w') as j:
    j.writelines(str(length) + "\n")
    j.writelines(str(min_sum) + "\n")
    output = " ".join(map(str, res))
    j.writelines(output)