S = input()

p1, p2 = 0, 0

while p2 < len(S) + 1:
	if p2 - p1 == 2:
		if S[p1:p2] == 'pi' or S[p1:p2] == 'ka':
			p1 = p2
		elif S[p1:p2] == 'ch':
			p2 += 1
			continue
		else:
			print('NO')
			exit()
	elif p2 - p1 == 3:
		if S[p1:p2] == 'chu':
			p1 = p2
		else:
			print('NO')
			exit()
	p2 += 1

if p1 != len(S): print('NO')
else: print('YES')