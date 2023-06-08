import sys

Board = [list(map(int, input().split())) for _ in range(19)]


def check(color, x, y):
    x2, y2, count = x, y, 0
    while x2 < 19 and y2 < 19 and Board[x2][y2] == color:
        if x2 == x and x2 > 0 and Board[x2-1][y2] == color:
            break
        x2 += 1
        count += 1
    if count == 5:
        return True
    x2, y2, count = x, y, 0
    while x2 < 19 and y2 < 19 and Board[x2][y2] == color:
        if y2 == y and y2 > 0 and Board[x2][y2-1] == color:
            break
        y2 += 1
        count += 1
    if count == 5:
        return True
    x2, y2, count = x, y, 0
    while x2 < 19 and y2 < 19 and Board[x2][y2] == color:
        if x2 == x and y2 == y and x2 > 0 and y2 > 0 and Board[x2-1][y2-1] == color:
            break
        x2 += 1
        y2 += 1
        count += 1
    if count == 5:
        return True
    x2, y2, count = x, y, 0
    while x2 >= 0 and y2 < 19 and Board[x2][y2] == color:
        if x2 == x and y2 == y and x2 < 18 and y2 > 0 and Board[x2+1][y2-1] == color:
            break
        x2 -= 1
        y2 += 1
        count += 1
    if count == 5:
        return True
    return False


for i in range(19):
    for j in range(19):
        if Board[i][j]:
            if check(Board[i][j], i, j):
                print(Board[i][j])
                print(i+1, j+1)
                sys.exit(0)
print(0)
