import sys 
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n, K = map(int,input().split())
    graph = list(map(int,input().split()))
    graph.sort()
    answer = 0
    min_diff = 1e9
    for i in range(n):
        s = i+1
        e = n-1
        while s <= e:
            mid = (s+e)//2
            avg = graph[i]+graph[mid]
            if avg > K:
                e = mid-1
            else:
                s = mid+1
            if abs(avg-K) < min_diff:
                answer = 1
                min_diff = abs(avg-K)
            elif abs(avg-K) == min_diff:
                answer += 1
    print(answer)
        