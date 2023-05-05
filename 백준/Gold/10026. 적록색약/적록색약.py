N = int(input())
Board = [input() for _ in range(N)]
Board1, Board2 = [[1 for _ in range(N)] for _ in range(N)], [[1 for _ in range(N)] for _ in range(N)]
answer1, answer2 = 0, 0
for i in range(N):
    for j in range(N):
        if Board[i][j] == 'R':
            Board1[i][j] = Board2[i][j] = 2
        elif Board[i][j] == 'G':
            Board1[i][j] = 3
            Board2[i][j] = 2

def	dfs(i, j, target, Board_):
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    Stack = [(i, j)]
    Board_[i][j] = 0
    while Stack:
        cur = Stack.pop()
        for i in range(4):
            x, y = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= x < N and 0 <= y < N and Board_[x][y] == target:
                Board_[x][y] = 0
                Stack.append((x, y))
    return 1

for i in range(N):
    for j in range(N):
        if Board1[i][j]: 
            answer1 += dfs(i, j, Board1[i][j], Board1)
        if Board2[i][j]:
            answer2 += dfs(i, j, Board2[i][j], Board2)
            
print(answer1, answer2)