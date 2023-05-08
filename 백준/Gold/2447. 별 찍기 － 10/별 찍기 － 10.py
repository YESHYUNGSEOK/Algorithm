import copy

N = int(input())
arr = [['*', '*', '*'], ['*',' ', '*'], ['*', '*', '*']]
def	recur(cnt):
	if cnt == 3:
		return
	cnt = cnt // 3
	length = len(arr)
	for i in range(length):
		arr[i] = arr[i] * 3
	for i in range(length):
		arr.append(copy.deepcopy(arr[i]))
	for i in range(length):
		arr.append(copy.deepcopy(arr[i]))
	start = len(arr) // 3
	end = start * 2
	for i in range(start, end):
		for j in range(start, end):
			arr[i][j] = ' '
	recur(cnt)
recur(N)
for x in range(len(arr)):
	for y in range(len(arr)):
		print(arr[x][y], end='')
	print()