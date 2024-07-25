N, K = map(int, input().split())
arr = list(map(int, input().split()))

dic, answer = {}, 0
p1, p2 = 0, 0

while p2 < N:
    if arr[p2] not in dic:
        dic[arr[p2]] = 1
    else:
        dic[arr[p2]] += 1

    while dic[arr[p2]] > K:
        dic[arr[p1]] -= 1
        if dic[arr[p1]] == 0:
            del dic[arr[p1]]
        p1 += 1
    
    answer = max(answer, p2 - p1 + 1)
    p2 += 1

print(answer)