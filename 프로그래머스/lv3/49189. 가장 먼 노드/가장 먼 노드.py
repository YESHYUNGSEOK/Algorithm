from collections import deque

def solution(n, edge):
    Graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for e in edge:
        u, v = e
        Graph[u].append(v)
        Graph[v].append(u)
    
    visited[1] = 1
    Q = deque([1])
    while Q:
        cur = Q.popleft()
        for node in Graph[cur]:
            if not visited[node]:
                visited[node] = visited[cur] + 1
                Q.append(node)
    print(visited)
    return visited.count(max(visited))