from collections import deque

masks = [
    0b111000000,
    0b000111000,
    0b000000111, 
    0b100100100, 
    0b010010010, 
    0b001001001,  
    0b100010001, 
    0b001010100   
]

def bitmask(bit_board):
    queue = deque([(bit_board, 0)])
    visited = set([bit_board])
    
    while queue:
        cur_bit_board, flips = queue.popleft()
        
        if cur_bit_board == 0 or cur_bit_board == 0b111111111:
            return flips
        
        for mask in masks:
            new_bit_board = cur_bit_board ^ mask
            if new_bit_board not in visited:
                visited.add(new_bit_board)
                queue.append((new_bit_board, flips + 1))
    
    return -1

T = int(input())

result = []

for _ in range(T):
    board = [input().split() for _ in range(3)]
    
    bit_board = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'T':
                bit_board |= (1 << (i * 3 + j))
                
    result.append(bitmask(bit_board))
    
for r in result:
    print(r)