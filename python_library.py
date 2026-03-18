def array_input():
    array = []
    n = int(input("so luong phan tu: "))
    for i in range(n):
        v = int(input())
        array.append(v)
    return(array)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

def hoan_vi(arr, i):
    if i == len(arr) - 1:
        print(arr)
        return
    for j in range(len(arr)):
        arr[i], arr[j] = arr[j] , arr[i]
        hoan_vi(arr,i + 1)
        arr[i] ,arr[j] = arr[j] , arr[i]

def tim_phan_tu(arr, a):
    indi = [i + 1 for i, n in enumerate(arr) if n == a]  
    if indi:
        print(f"element {a} index in1 array: {indi}")
    else:
        print(f"element {a} not found.")

def giaithua(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * giaithua(n - 1)
    
def luy_thua(a, n):
    if n == 0:
        return 1
    half = luy_thua(a, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return a * half * half

def reverse_string(string):
    print(string[::-1])

def maze_solve():
    def is_safe(maze, x, y, visited):
        n = len(maze)
        m = len(maze[0])
        return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]

    def solve_maze(maze, x, y, path, visited):
        n = len(maze)
        m = len(maze[0])

        if x == n - 1 and y == m - 1:
            path.append((x, y))
            print("Đường đi:", path)
            return True

        if is_safe(maze, x, y, visited):
            visited[x][y] = True
            path.append((x, y))

            if (solve_maze(maze, x + 1, y, path, visited) or
                solve_maze(maze, x, y + 1, path, visited) or
                solve_maze(maze, x - 1, y, path, visited) or
                solve_maze(maze, x, y - 1, path, visited)):
                return True

            path.pop()
            visited[x][y] = False

        return False

    maze = []
    n = int(input("row: "))
    m = int(input("colum: "))

    for i in range(n):
        row = list(map(int, input().split()))
        maze.append(row)

    visited = [[False for _ in range(m)] for _ in range(n)]
    path = []

    if not solve_maze(maze, 0, 0, path, visited):
        print("no way")

def prime_num(i):
        if i < 2:
            return False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                return False
        return True

def read_file():
    f = open("input.txt","r",encoding="utf-8")
    a = f.read()
    return a

def readline_file():
    with open("input.txt","r",encoding="utf-8") as f:
        for i in f:
            return i
        
def binary_search():
    target = int(input("target: "))
    arr = sorted(array_input()) 

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            print("found", target, "at", mid)
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print("not found", target)
    return False

def groupAnagrams():
    strs = input().split(",") 
    strs = [s.strip() for s in strs]  
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))  
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values()) 

def quicksort():
    nums = array_input() 

    def sort(arr):  
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return sort(left) + middle + sort(right)

    return sort(nums)