from collections import deque

def dfs (graph, v, visited):

    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs (graph, start, visited):

    queue = deque([start])
    print(start, end=' ')

    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v ]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')


N, M, V = (map(int, input().split()))

graph = [[] for i in range(N+1)]
for i in range(M):
    li = (list(map(int, input().split())))
    graph[li[0]].append(li[1])
    graph[li[1]].append(li[0])

for i in range(N+1):
    graph[i] = sorted(graph[i])



visited = [False] * (N+1)
dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)