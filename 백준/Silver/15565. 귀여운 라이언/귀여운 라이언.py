from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = int(1e8)
p1, p2, = 0, 0
q = deque()
count = 0

while p2 < N:
    if arr[p2] == 1:
        q.append(p2)
        count += 1

    if count > K: 
        p1 = q.popleft()
        count -= 1
    
    if count == K:
        answer = min(answer, p2 - q[0] + 1)

    p2 += 1

if answer == int(1e8): print(-1)
else: print(answer)