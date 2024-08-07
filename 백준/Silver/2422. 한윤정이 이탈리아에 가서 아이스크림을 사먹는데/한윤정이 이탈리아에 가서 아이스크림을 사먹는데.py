N, M = map(int, input().split())

arr = [set() for _ in range(N + 1)]

for _ in range(M):
	a, b = map(int, input().split())
	arr[a].add(b)
	arr[b].add(a)

result = 0

for i in range(1, N + 1):
	for j in range(i + 1, N + 1):
		if j in arr[i]: 
			continue
		for k in range(j + 1, N + 1):
			if k in arr[i] or k in arr[j]:
				continue
			result += 1

print(result)