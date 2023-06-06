answer = 0

def dfs(numbers, target, idx, current):
    global answer
    if idx == len(numbers):
        if current == target: answer += 1
        return
    dfs(numbers, target, idx + 1, current + numbers[idx])
    dfs(numbers, target, idx + 1, current - numbers[idx])

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer