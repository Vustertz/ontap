n = int(input())
m = int(input())
maze = []
for i in range(n):
    v = str(input())
    row = list(map(int, v.split()))
    maze.append(row)

def maze_solve(maze, x, y, path, visited):    
    n = len(maze)  
    m = len(maze[0])
    if 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]:
        visited[x][y] = True
        path.append((x, y))
        if x == n - 1 and y == m - 1:
            print("duong di:", path)
            return True
        if (maze_solve(maze, x + 1, y, path, visited) or
            maze_solve(maze, x, y + 1, path, visited) or
            maze_solve(maze, x - 1, y, path, visited) or
            maze_solve(maze, x, y - 1, path, visited)):
            return True
        path.pop()
        visited[x][y] = False
    return False

visited = []
for i in range(n):
    row = [False] * m
    visited.append(row)
path = []
if not maze_solve(maze, 0, 0, path, visited):
    print("no way") 