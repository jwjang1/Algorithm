from collections import deque

N, M = map(int, input().split())

maze = []

for i in range(N):
    maze.append(list(map(int, input())))

step = 0

def bfs(x, y):
    queue = deque([x][y])