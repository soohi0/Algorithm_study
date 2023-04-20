def solution(beginning, target):
    answer = 0
    r = len(target)
    c = len(target[0])
    dp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            cand = []
            if (x, y) == (0, 0) and beginning[x][y] != target[x][y]:
                dp[x][y] == 1
                continue
            if y > 0: 
                cand.append(dp[x][y-1])
            if x > 0:
                cand.append(dp[x-1][y])
            if sum(cand) % 2 == 0: # 짝수 : 안바뀜
                if beginning[x][y] != target[x][y]:
                    dp[x][y] = sum(cand) + 1
                else:
                    dp[x][y] = sum(cand)
            else:
                if beginning[x][y] == target[x][y]:
                    dp[x][y] = sum(cand) + 1
                else:
                    dp[x][y] = sum(cand)
           
    return answer