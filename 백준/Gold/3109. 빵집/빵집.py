R, C = map(int, input().split())
map = [list(input().strip()) for _ in range(R)]
pipe = 0

dx, dy = (-1, 0, 1), (1, 1, 1)

def dfs(x, y):
    global pipe
    map[x][y] = 'x'
    if y == C - 1:
        pipe += 1
        return True
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if map[nx][ny] != 'x':
                if dfs(nx, ny):
                    return True

for i in range(R):
    dfs(i, 0)
print(pipe)