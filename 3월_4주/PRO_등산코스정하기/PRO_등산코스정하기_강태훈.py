from heapq import heappop, heappush, heapify
from collections import defaultdict
INF = float("inf")

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for i,j,w in paths:
        graph[i-1].append((w,j-1))
        graph[j-1].append((w,i-1))

    summits = set(map(lambda x:x-1, summits))
    gates = set(map(lambda x:x-1, gates))
    dist = [0 if i in gates else INF for i in range(n)]
    pq = [(0, gate) for gate in gates]; heapify(pq)
        
    while pq:
        cintensity, cnode = heappop(pq)
        if dist[cnode] < cintensity or cnode in summits:
            continue
        for nintensity, nnode in graph[cnode]:
            bigger_intensity = max(cintensity, nintensity)
            if bigger_intensity < dist[nnode]:
                dist[nnode] = bigger_intensity
                heappush(pq, (bigger_intensity, nnode))
    return sorted([[summit+1, dist[summit]] for summit in summits], key=lambda x:(x[1],x[0]))[0]


tc = [
    [6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5],	[5, 3]],
    [7,	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1],	[2, 3, 4],	[3, 4]],
    [7,	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7],	[1, 5],	[5, 1]],
    [5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],	[1, 2],	[5],	[5, 6]],
]
for case in tc:
    print(solution(*case[:-1]), case[-1])
