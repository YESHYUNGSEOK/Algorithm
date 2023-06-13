from copy import deepcopy
import sys


def melt(x, y):
    count = 0
    if x > 0 and not Map[x-1][y]:
        count += 1
    if y > 0 and not Map[x][y-1]:
        count += 1
    if x < N - 1 and not Map[x+1][y]:
        count += 1
    if y < M - 1 and not Map[x][y+1]:
        count += 1
    if not count:
        return
    if Map[i][j] - count < 0:
        after.append((x, y, 0))
    else:
        after.append((x, y, Map[i][j] - count))


def dfs(Board, i, j):
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    Stack = [(i, j)]
    Board[i][j] = 0
    while Stack:
        cur = Stack.pop()
        for i in range(4):
            x, y = cur[0] + dx[i], cur[1] + dy[i]
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if not Board[x][y]:
                continue
            Board[x][y] = 0
            Stack.append((x, y))


N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    answer += 1
    after = []
    islands = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j]:
                melt(i, j)
    for change in after:
        Map[change[0]][change[1]] = change[2]
    Board = deepcopy(Map)
    for i in range(N):
        for j in range(M):
            if Board[i][j]:
                islands += 1
                dfs(Board, i, j)
    if not islands:
        print(0)
        break
    if islands >= 2:
        print(answer)
        break
