from collections import deque

M, N = map(int, input().split())
Graph = [list(map(int, input().split())) for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def	bfs():
	Queue = deque()
	for i in range(N):
		for j in range(M):
			if Graph[i][j] == 1:
				Queue.append((i, j))
	while Queue:
		cur = Queue.popleft()
		for i in range(4):
			x = cur[0] + dx[i]
			y = cur[1] + dy[i]
			if x < 0 or x >= N or y < 0 or y >= M: continue
			if Graph[x][y] != 0: continue
			Graph[x][y] = Graph[cur[0]][cur[1]] + 1
			Queue.append((x, y))

bfs()
high, low = 0, 1
for i in range(N):
	for j in range(M):
		if Graph[i][j] > high:
			high = Graph[i][j]
		if Graph[i][j] == 0:
			low = Graph[i][j]
if not low:
	print(-1)
else:
	print(high - 1)