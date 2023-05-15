Array = list(input())
Stack = []
num = 1
ret = 0
for i in range(len(Array)):
	if Array[i] == '(':
		Stack.append(Array[i])
		num *= 2
	elif Array[i] == '[':
		Stack.append(Array[i])
		num *= 3
	elif Array[i] == ')':
		if not Stack or Stack[-1] == '[':
			ret = 0
			break
		if Array[i-1] == '(':
			ret += num
		Stack.pop()
		num //= 2
	elif Array[i] == ']':
		if not Stack or Stack[-1] == '(':
			ret = 0
			break
		if Array[i-1] == '[':
			ret += num
		Stack.pop()
		num //= 3
if Stack:
	print(0)
else:
	print(ret)