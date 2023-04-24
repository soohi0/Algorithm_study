import heapq as hq

def solution(x, y, n):
    total_len = max(y//n +1,y//2+1,y//3+1)
    dp= [set() for _ in range(total_len)]
    dp[0].add((x,0))
    i = 0
    if x == y:
        return 0
    while True:
        for v, cnt in dp[i]:
            c1 = v+n
            c2 = v*2
            c3 = v*3
            if c1 == y or c2 == y or c3 == y:
                return cnt+1
            if c1 < y:
                dp[i+1].add((c1,cnt+1))
            if c2 < y:
                dp[i+1].add((c2,cnt+1))
            if c3 < y:
                dp[i+1].add((c3,cnt+1))
            if c1 > y and c2 > y and c3 > y:
                return -1
        i += 1