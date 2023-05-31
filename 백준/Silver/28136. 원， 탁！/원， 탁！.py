from collections import deque

N = int(input())
arr = deque(list(map(int, input().split())))
min = min(arr)
while arr[0] != min:
    arr.rotate(1)
answer = 1
cur = 0
for number in arr:
    if number <= cur:
        answer += 1
    cur = number
print(answer)
