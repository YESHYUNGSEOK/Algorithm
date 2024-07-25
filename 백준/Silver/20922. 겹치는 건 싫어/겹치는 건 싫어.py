N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = [0] * 100001

answer = 0
p1, p2 = 0, 0

while p2 < N:
    count[arr[p2]] += 1

    while count[arr[p2]] > K:
        count[arr[p1]] -= 1
        p1 += 1
    
    answer = max(answer, p2 - p1 + 1)
    p2 += 1

print(answer)