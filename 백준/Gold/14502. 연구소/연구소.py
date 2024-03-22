from collections import deque
from copy import deepcopy

N, M = list(map(int, input().split(" ")))
Matrix = []
for _ in range(N): Matrix.append(list(map(int, input().split(" "))))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

answer = 0

def bfs():
	global answer

	graph = deepcopy(Matrix)
	q = deque()
	
	for i in range(len(graph)):
		for j in range(len(graph[0])):
			if graph[i][j] == 2: q.append([i,j])
	
	while q:
		cur = q.popleft()
		for i in range(4):
			x, y = cur[0] + dx[i], cur[1] + dy[i]
			if 0 <= x < len(graph) and 0 <= y < len(graph[0]) and not graph[x][y]:
				graph[x][y] = 2
				q.append([x, y])
	
	answer_ = 0
	for i in range(len(graph)):
		answer_ += graph[i].count(0)
	
	answer = max(answer, answer_)
	

def install(wall):
	if wall == 3:
		bfs()
		return
	
	for i in range(N):
		for j in range(M):
			if not Matrix[i][j]:
				Matrix[i][j] = 1
				install(wall + 1)
				Matrix[i][j] = 0

install(0)
print(answer)