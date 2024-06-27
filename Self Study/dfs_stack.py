def dfs(graph, v, visited):
    stack = []
    stack.append(v)
    visited[v] = True
    print(v, end=' ')
    
    while stack:
        v = stack[-1]
        for i in graph[v]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                print((i), end=' ')
                break
            elif i == graph[v][-1]:
                stack.pop()
            


graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7] 
]

visited =[False]*9

first_node = 1

dfs(graph,first_node,visited)