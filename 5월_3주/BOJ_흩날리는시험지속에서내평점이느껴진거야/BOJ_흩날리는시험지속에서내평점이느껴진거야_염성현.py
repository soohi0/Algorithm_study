N, K = map(int,input().split())
graph = list(map(int,input().split()))
answer = 0
s = 0
e = int(1e5)*20+1
while s<=e:
    mid = (s+e)//2
    group = 0
    score = 0
    for corr in graph:
        score += corr
        if score >= mid:
            group += 1
            score = 0
    if group >= K:
        answer = mid
        s = mid+1
    else:
        e = mid-1
print(answer)
