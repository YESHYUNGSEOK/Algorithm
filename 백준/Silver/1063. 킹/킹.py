def pos(pos):
    x, y = 0, 0
    if pos[0] == 'A': y = 0 
    elif pos[0] == 'B': y = 1 
    elif pos[0] == 'C': y = 2 
    elif pos[0] == 'D': y = 3 
    elif pos[0] == 'E': y = 4 
    elif pos[0] == 'F': y = 5 
    elif pos[0] == 'G': y = 6 
    elif pos[0] == 'H': y = 7 
    if pos[1] == '8': x = 0 
    elif pos[1] == '7': x = 1 
    elif pos[1] == '6': x = 2 
    elif pos[1] == '5': x = 3 
    elif pos[1] == '4': x = 4 
    elif pos[1] == '3': x = 5 
    elif pos[1] == '2': x = 6 
    elif pos[1] == '1': x = 7
    return x, y

Move = {'R' : [0, 1], 'L' : [0, -1], 'B' : [1, 0], 'T' : [-1, 0], 'RT' : [-1, 1], 'LT' : [-1, -1], 'RB' : [1, 1], 'LB' : [1, -1]}
Position = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H'}
Index = {0 : 8, 1 : 7, 2 : 6, 3 : 5, 4 : 4, 5 : 3, 6 : 2, 7 : 1}
King, Stone, move = map(str, input().split())
KingX, KingY = pos(King)
StoneX, StoneY = pos(Stone)
for _ in range(int(move)):
    N = input()
    x, y = KingX + Move[N][0], KingY + Move[N][1]
    if x < 0 or x > 7 or y < 0 or y > 7: continue    
    if x == StoneX and y == StoneY:
        x2, y2 = StoneX + Move[N][0], StoneY + Move[N][1]
        if x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7: continue
        KingX, KingY, StoneX, StoneY = x, y, x2, y2
    KingX, KingY = x, y
print(Position[KingY], Index[KingX], sep="")
print(Position[StoneY], Index[StoneX], sep="")