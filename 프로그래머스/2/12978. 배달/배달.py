import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [int(10e8)] * (N + 1)
    
    for u, v, w in road:
        graph[u].append([v, w])
        graph[v].append([u, w])
    
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue 
        for node in graph[now]:
            d = dist + node[1]
            if distance[node[0]] > d:
                distance[node[0]] = d
                heapq.heappush(q, (d, node[0]))
    
	
    answer = 0
    for i in distance:
        if i <= K: answer += 1
                
    return answer
