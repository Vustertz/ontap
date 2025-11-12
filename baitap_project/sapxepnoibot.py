def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

    return arr

with open('bubble.inp', 'r') as file:
    n = int(file.readline().strip()) 
    arr = list(map(int, file.readline().strip().split())) 

bubble_sort(arr)

with open('bubble.out', 'w') as file:
    file.write(" ".join(map(str, arr)) + "\n")
