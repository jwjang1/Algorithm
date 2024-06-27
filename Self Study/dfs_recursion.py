def dfs (graph, v, visited):

    visited[v] = True
    print(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)




# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph=[
    [],
    [2,3,8],  # 1번부터 시작, 0번인덱스는 비워둠 
    [1,7],    # 2번노드는 1번 7번 노드와 연결되어있다.
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9 #모든 노드는 False로 초기화(처음에는 하나도 방문하지 않은 것처럼 처리), *9이유: 0번인덱스를 사용하지 않기 위해 하나 큰값을 줌

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)