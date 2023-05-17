import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    ss = sorted(list(map(int, input().split())))

    cnt = 0
    first, second = 0, n-1
    
    min_gap = abs((ss[first] + ss[second]) - k)
    while first < second:
        gap = abs(ss[first] + ss[second] - k)
        if gap < min_gap:
            min_gap = gap
            cnt = 1
        elif gap > min_gap:
            pass
        else:
            cnt += 1
        if (ss[first+1] + ss[second] - k) <= min_gap:
            first += 1
        elif (ss[first] + ss[second-1] - k) <= min_gap:
            second -= 1
        elif (ss[first+1] + ss[second-1] - k) <= min_gap:
            first += 1
            second -= 1
        else:
            first += 1
        
    print(cnt)
    