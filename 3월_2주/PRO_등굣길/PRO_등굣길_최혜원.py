def solution(m, n, puddles):
    road = [[1 for _ in range(m)] for __ in range(n)]
    
    for p_x, p_y in puddles:
        road[p_y-1][p_x-1] = 0
        if p_x == 1:
            for i in range(p_y-1, n):
                road[i][0] = 0
        if p_y == 1:
            for j in range(p_x-1, m):
                road[0][j] = 0
    # print(road)
    
    for y in range(1, n):
        for x in range(1, m):
            if road[y][x] != 0:
                road[y][x] = road[y-1][x] + road[y][x-1]
    # print(road)
                
    return road[-1][-1] % 1000000007