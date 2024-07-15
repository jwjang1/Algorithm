from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N+1)]
for i in range(M):
    li = (list(map(int, sys.stdin.readline().split())))
    graph[li[0]].append(li[1])

distance = [-1 for i in range(N+1)]
distance[X] = 0

queue = deque()
queue.append(X)

while queue:
    curr = queue.popleft()
    for i in graph[curr]:
        if distance[i] == -1:
            distance[i] = distance[curr]+1
            queue.append(i)

if K in distance:
    for i in range(len(distance)):
        if distance[i] == K:
            print(i)
else:
    print(-1)