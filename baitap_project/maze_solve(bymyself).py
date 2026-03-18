import time
def maze():
    
    # n = int(input())
    # m = int(input())
    count = 0
    maze = []
    path = []
    visited = []

    with open('maze.txt','r') as f:
        n = int(f.readline())
        m = int(f.readline())
        x = int(f.readline())
        y = int(f.readline())
        for i in f:
            maze.append(list(map(int, i.split())))

    for i in range(n):
        a = [False]*m
        # v = list(map(int, input().split()))
        # maze.append(v)
        visited.append(a)


    def maze_solve(x,y,visited,maze,path,count):
        
        if 0 <= x <= n - 1 and 0 <= y <= m - 1 and maze[x][y] == 0 and not visited[x][y]:
            visited[x][y] = True
            path.append((x,y))
            count += 1

            if x == n - 1 and y == m - 1:
                print(path)
                print(count)
                return True
            
            if (maze_solve(x, y + 1, visited, maze, path,count) or
                maze_solve(x, y - 1, visited, maze, path,count) or
                maze_solve(x + 1, y, visited, maze, path,count) or
                maze_solve(x - 1, y, visited, maze, path,count)):
                return True
            
            path.pop()
            count -= 1
            visited[x][y] = False
            return False
        return False
    
    if not maze_solve(x,y,visited,maze,path,count):
        print('no way')

start = time.time()
maze()
end = time.time()
print(end - start)