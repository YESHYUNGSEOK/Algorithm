function solution(N, road, K) {
    graph = [];
    for (let i = -1; i < N; i++) graph.push([])
    for (const [u, v, w] of road) {
        graph[u].push({to:v, dist:w})
        graph[v].push({to:u, dist:w})
    }
    
    const queue = [{to:1, dist:0}];
    const dist = Array(graph.length).fill(Infinity);
    
    dist[1] = 0;
    
    while (queue.length) {
        const { to } = queue.pop();
        
        graph[to].forEach((next) => {
            const acc = dist[to] + next.dist;
            if (dist[next.to] > acc) {
                dist[next.to] = acc;
                queue.push(next);
            }
        })
    }
    
    answer = 0
    for (let i = 0; i < dist.length; i ++) {
        if (dist[i] <= K) answer++
    }
    return answer;
}