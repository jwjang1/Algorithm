from collections import deque

N, M = map(int, input().split())

maze = []

for i in range(N):
    maze.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        v = queue.popleft()

        for i in range(4):
            tmpx = v[0] + dx[i]
            tmpy = v[1] + dy[i]

            if tmpx < 0 or tmpx >= N or tmpy < 0 or tmpy >= M:
                continue

            if maze[tmpx][tmpy] == 0:
                continue

            if maze[tmpx][tmpy] == 1:
                maze[tmpx][tmpy] = maze[v[0]][v[1]] + 1
                queue.append([tmpx, tmpy])
                

bfs(0, 0)
print(maze[N-1][M-1])