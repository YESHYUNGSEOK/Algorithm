def solution(n, m, x, y, r, c, k):
    matrix = [['.' for _ in range(m)] for _ in range(n)]
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    dx, dy, direction = [1, 0, 0, -1], [0, -1, 1, 0], ['d', 'l', 'r', 'u']
    
    moved = 0
    path = ''

    while moved != k:
        moved += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if k - moved < abs(r - nx) + abs(c - ny) : continue
            path += direction[i]
            x, y = nx, ny
            break
       
    if (len(path) != k): return 'impossible'
    return path