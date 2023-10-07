from collections import deque

def solution(n, edge):
    Graph = [[] for _ in range(n+1)]
    Visited = [0] * (n + 1)
    
    for e in edge:
        u, v = e
        Graph[u].append(v)
        Graph[v].append(u)
    
    Q = deque([1])
    Visited[1] = 1
    
    while Q:
        cur = Q.popleft()
        for node in Graph[cur]:
            if not Visited[node]:
                Visited[node] = Visited[cur] + 1
                Q.append(node)

    return Visited.count(max(Visited))