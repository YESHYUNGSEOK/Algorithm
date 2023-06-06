result = 0

def dfs(k, dungeons, visited, count):
    global result
    result = max(result, count)
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], dungeons, visited, count + 1)
            visited[i] = False

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)
    return result