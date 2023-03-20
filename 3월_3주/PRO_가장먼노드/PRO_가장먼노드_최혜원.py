from collections import deque, defaultdict
def solution(n, edges):
    graph = defaultdict(list)
    visited = [0] * (n+1)
    max_dist = 0
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    q = deque([(1, 0)])
    while q:
        c_node, dist = q.popleft()
        # print(c_node, dist,graph[c_node])
        for n in graph[c_node]:
            if visited[n] == 0:
                q.append((n, dist+1))
                visited[n] = dist+1
                if dist+1 > max_dist:
                    max_dist = dist+1
    visited[1] = 0
    
    return sum([i == max_dist for i in visited])
