from python_library import array_input
def to_hop():
    n = int(input())
    k = int(input())
    def ham_sinh(a, start, cur):
        if len(cur) == k:
            print(cur)
            return
        for i in range(start, n + 1):
            cur.append(i)
            ham_sinh(a, i + 1, cur)
            cur.pop()
    ham_sinh(n, 1, [])
    
def in_hoan_vi():
    arr = array_input()
    def hoan_vi(arr, i):
        if i == len(arr) - 1:
            print(arr)
            return
        for j in range(i, len(arr)): 
            arr[i], arr[j] = arr[j], arr[i]
            hoan_vi(arr, i + 1)
            arr[i], arr[j] = arr[j], arr[i]
    print(hoan_vi(arr , 0))

def maze_path():
    maze = []           
    visited = set()       
    x = y = 0           
    with open("input.txt", "r") as f:
        for line in f:
            row = list(map(int, line.split()))
            maze.append(row)
    def solve_maze(maze, x, y, path, visited):
        n = len(maze)
        m = len(maze[0])
        if x < 0 or y < 0 or x >= n or y >= m or maze[x][y] == 1 or (x, y) in visited:
            return
        path.append((x, y))
        visited.add((x, y))
        if (x, y) == (n - 1, m - 1):
            print("duong di:", path)
        else:
            solve_maze(maze, x + 1, y, path, visited)  
            solve_maze(maze, x - 1, y, path, visited)  
            solve_maze(maze, x, y + 1, path, visited)  
            solve_maze(maze, x, y - 1, path, visited)  
        path.pop()
        visited.remove((x, y))
    solve_maze(maze, x, y, [], visited)

def bianary():
    n = int(input())
    def generate_binary(curr):
        if len(curr) == n:
            print(curr)
            return
        generate_binary(curr + '0')
        generate_binary(curr + '1')
    generate_binary('')
bianary()
    