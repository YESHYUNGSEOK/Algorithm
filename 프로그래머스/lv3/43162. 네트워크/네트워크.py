def dfs(computers, i, j):
    Stack = []
    computers[i][j] = 0
    Stack.append((i, j))
    while Stack:
        i, j = Stack.pop()
        for k in range(len(computers)):
            if computers[j][k]:
                computers[j][k] = 0
                Stack.append((j, k))


def solution(n, computers):
    networks = 0
    for i in range(len(computers)):
        if 1 in computers[i]:
            networks += 1
        for j in range(len(computers)):
            if computers[i][j]:
                dfs(computers, i, j)
    return networks