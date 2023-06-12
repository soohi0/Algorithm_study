import sys 
import heapq as hq
input = lambda : sys.stdin.readline().strip()

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
graph.sort()
queue = list()

for i in graph:
    hq.heappush(queue,i[1])
    if len(queue) > i[0]:
        hq.heappop(queue)
    
print(sum(queue))
