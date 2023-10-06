from collections import deque

def bfs(From, To, maps):
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    Board = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    queue = deque()
    queue.append((From[0], From[1]))
    while queue:
        cur = queue.popleft()
        if cur == To: return Board[cur[0]][cur[1]]
        for i in range(4):
            x, y = dx[i] + cur[0], dy[i] + cur[1]
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]):
                if maps[x][y] != 'X' and not Board[x][y]:
                    Board[x][y] = Board[cur[0]][cur[1]] + 1
                    queue.append((x, y))
    return -1

def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S': start = (i, j)
            if maps[i][j] == 'L': lever = (i, j)
            if maps[i][j] == 'E': exit = (i, j)
    
    toLever = bfs(start, lever, maps)
    toExit = bfs(lever, exit, maps)
    if toLever == -1 or toExit == -1: return -1
    return toLever + toExit