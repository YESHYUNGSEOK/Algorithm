n, m = map(int, input().split())
Input = [input() for _ in range(n)]
Board = []
for i in range(n):
    board = []
    for j in range(m):
        if Input[i][j] == '.': board.append(1)
        else: board.append(0)
    Board.append(board)
throw = int(input())
heights = [i for i in map(int, input().split())]

def	path():
    Visited = [[True for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not Board[i][j]: Visited[i][j] = False
    return Visited

def	dfs(i, j):
    global Chunk
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    Chunk.append([i, j])
    Visited[i][j] = True
    Stack = [(i, j)]
    while Stack:
        cur = Stack.pop()
        for i in range(4):
            x, y = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= x < n and 0 <= y < m and not Visited[x][y]:
                Chunk.append([x, y])
                Visited[x][y] = True
                Stack.append((x, y))
    for i in Chunk:
        if i[0] == n - 1: return False
    return True

def drop():
    global Chunk
    Chunk_ = []
    y1, y2 = int(10e9), 0
    for i in Chunk:
        if i[1] > y2: y2 = i[1]
        if i[1] < y1: y1 = i[1]
    for j in range(y1, y2+1):
        i = 0
        for item in Chunk:
            if item[1] == j and item[0] > i: i = item[0]
        Chunk_.append([i, j])
    for i in Chunk_:
        if i[0] + 1 == n or Board[i[0] + 1][i[1]] == 0: return False
    return True

for i, height in enumerate(heights):
    height_ = n - height
    if i % 2 == 0:
        for j in range(m):
            if Board[height_][j] == 0:
                Board[height_][j] = 1
                break
    else:
        for j in range(m-1, -1, -1):
            if Board[height_][j] == 0:
                Board[height_][j] = 1
                break
    Visited = path()
    Chunk = []
    for x in range(n):
        for y in range(m):
            if not Visited[x][y] and dfs(x, y):
                while drop():
                    for i in Chunk:
                        Board[i[0]][i[1]] = 1
                        i[0] += 1
                for i in Chunk:
                    Board[i[0]][i[1]] = 0
            Chunk.clear()

for i in range(n):
    for j in range(m):
        if Board[i][j]: print('.',end="")
        else: print('x', end="")
    print()
