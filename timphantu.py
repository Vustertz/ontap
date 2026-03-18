n = int(input("input array length: "))
a = int(input("element need to find: "))
arr = []
for i in range(n):
    v = int(input(f"element number: {i+1}: "))
    arr.append(v)
indi = [i + 1 for i, n in enumerate(arr) if n == a]  
if indi:
    print(f"element {a} index in1 array: {indi}")
else:
    print(f"element {a} not found.")

