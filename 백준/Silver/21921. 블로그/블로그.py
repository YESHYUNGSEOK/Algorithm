N, X = map(int, input().split())

days = list(map(int, input().split()))

most, periods = sum(days[:X]), 1
pos = most

p1, p2 = 0, X

while p2 < N:
	pos = pos - days[p1] + days[p2]

	if pos > most:
		most = pos
		periods = 1
	elif pos == most:
		periods += 1
	p1 += 1
	p2 += 1

if most == 0:
	print("SAD")
else:
	print(most)
	print(periods)
