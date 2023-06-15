from collections import deque

N, M = map(int, input().split())
Board = []
for _ in range(N): Board.append(input())
Visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
info = [0, 0, 0, 0, 1]
for i in range(N):
    for j in range(M):
        if Board[i][j] == 'R': info[0], info[1] = i, j
        if Board[i][j] == 'B': info[2], info[3] = i, j

def move(x, y, moveX, moveY):
    count = 0
    while Board[x + moveX][y + moveY] != '#' and Board[x][y] != 'O':
        x += moveX
        y += moveY
        count += 1
    return x, y, count

def bfs():
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    Q = deque()
    Q.append(info)
    Visited[info[0]][info[1]][info[2]][info[3]] = True
    while Q:
        cur = Q.popleft()
        if cur[4] > 10: break
        for i in range(4):
            rx, ry, rcount = move(cur[0], cur[1], dx[i], dy[i])
            bx, by, bcount, = move(cur[2], cur[3], dx[i], dy[i])
            if Board[bx][by] == 'O': continue
            if Board[rx][ry] == 'O':
                print(cur[4])
                return
            if rx == bx and ry == by:
                if rcount > bcount:
                    rx -= dx[i]
                    ry -= dy[i]
                else:
                    bx -= dx[i]
                    by -= dy[i]
            if not Visited[rx][ry][bx][by]:
                Visited[rx][ry][bx][by] = True
                Q.append([rx, ry, bx, by, cur[4] + 1])
    print(-1)

bfs()        