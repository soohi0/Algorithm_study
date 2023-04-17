from collections import defaultdict
from heapq import heappop, heapify, heappush
def solution(n, paths, gates, summits):
    inf = float(1e9)
    answer = []
    graph = defaultdict(list)
    weights = [0]+ [inf for _ in range(n)]
    summits = set(summits)
    gates = set(gates)
    hq = []
    for x, y, w in paths:
        graph[x].append([w, y])
        graph[y].append([w, x])
        
    for gate in gates:
        heappush(hq, [0, 0, gate])
    min_intensity = 10000000
    while hq:
        intensity, w, node = heappop(hq)
        if weights[node] < w:
            continue
        if node in summits:
            if intensity < min_intensity:
                answer = [[node, intensity]]
                min_intensity = intensity
            elif intensity == min_intensity:
                heappush(answer, [node, intensity])
            continue
        for n_w, n_node in graph[node]:
            if weights[n_node] > n_w:
                if n_node not in gates:
                    heappush(hq, [max(intensity, n_w), n_w, n_node])
                    weights[n_node] = n_w
    # print(answer)
    return answer[0]