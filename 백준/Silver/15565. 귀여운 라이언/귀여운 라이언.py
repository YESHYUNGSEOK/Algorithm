N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = int(1e8)
count = 0
p1, p2 = 0, 0

while p2 < N:
    if arr[p2] == 1:
        count += 1

    while count > K:
        if arr[p1] == 1:
            count -= 1
        p1 += 1
    
    if count == K:
        while arr[p1] != 1:
              p1 += 1
        answer = min(answer, p2 - p1 + 1)

    p2 += 1

if answer == int(1e8): print(-1)
else: print(answer)