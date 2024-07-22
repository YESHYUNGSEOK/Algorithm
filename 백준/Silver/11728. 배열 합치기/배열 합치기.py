N, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []

p1, p2 = 0, 0

while p1 != N or p2 != M:
	if p1 == N:
		result.append(b[p2])
		p2 += 1
	elif p2 == M:
		result.append(a[p1])
		p1 += 1
	else:
		if a[p1] < b[p2]:
			result.append(a[p1])
			p1 += 1
		else:
			result.append(b[p2])
			p2 += 1

print(*result)