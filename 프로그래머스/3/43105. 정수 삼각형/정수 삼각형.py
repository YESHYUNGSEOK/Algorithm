def solution(triangle):
    depth = len(triangle) - 2
    
    for i in range(depth, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])
    
    return triangle[0][0]