import heapq

def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

        if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue               # 따라서 다음으로 넘어간다.

        for i in graph[now]:     # 연결된 모든 노드 탐색
            if dist+i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 크다면
                distance[i[0]] = dist+i[1]   #
                heapq.heappush(q, (dist+i[1], i[0]))

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)] 
    distance = [int(10e8)] * (N+1)
    
    for eachRoad in road:
        u, v, w = eachRoad[0], eachRoad[1], eachRoad[2]
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    dijkstra(1, distance, graph)
    
    for i in range(len(distance)):
        if distance[i] <= K: answer += 1
    print(distance)
    return answer