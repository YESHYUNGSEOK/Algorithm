H, W = map(int, input().split())
answer = 0
Board = [[0 for _ in range(W)] for _ in range(H)]
for i, height in enumerate(map(int, input().split())):
    for j in range(H-1, H-height-1, -1):
        Board[j][i] = 1
for i in range(H):
    for j in range(1, W-1):
        if not Board[i][j] and Board[i][j-1]:
            fill, flag = 0, False
            for k in range(j, W-1):
                if Board[i][k+1]:
                    fill += 1
                    flag = True
                    break
            if flag:
                for k in range(j, j+fill):
                    Board[i][k] = 1
                    answer += 1
print(answer)
