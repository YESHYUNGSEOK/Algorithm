def backtracking(idx, count, chickens):
    global result

    if count == 3:
        prefer = 0
        for i in range(N):
            prefer += max(matrix[i][chickens[0]], matrix[i][chickens[1]], matrix[i][chickens[2]])
        result = max(result, prefer)
        return
    
    if idx == M:
        return
    
    backtracking(idx + 1, count, chickens)
    
    chickens[count] = idx
    backtracking(idx + 1, count + 1, chickens)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = 0

chickens = [0, 0, 0]
backtracking(0, 0, chickens)

print(result)
