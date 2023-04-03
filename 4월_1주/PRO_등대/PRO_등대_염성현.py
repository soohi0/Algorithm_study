# 그래프를 생성한다.
# 단말노드를 찾는다.
# 연결된 등대를 밝힌다.
# 불을 밝힌 등대를 그래프에서 지운다.
# 다시 단말노드를 찾는다.

from collections import defaultdict, deque
def solution(n, lighthouse):
    lighted = [0 for _ in range(n+1)]
    excepted = set()
    
    while True:
        # 그래프 생성
        graph = defaultdict(list)
        for a, b in lighthouse:
            if a not in excepted and b not in excepted:
                graph[a].append(b)
                graph[b].append(a)
        # 그래프가 그려지지 않으면 종료
        if not graph:
            break
            
        # 단말 노드를 찾아 연결된 등대를 밝힌다.
        for k, v in graph.items():
            if len(v) == 1 and lighted[k] != 1:
                lighted[v[0]] = 1
                excepted.add(v[0])
    
    return sum(lighted)

# import heapq as hq
# from collections import deque

# def dijkstra(start,g,d):
#     q = []
#     hq.heappush(q,(start,0))
#     d[start] = 0
#     friend = []
#     while q:
#         node, weight = hq.heappop(q)
#         if d[node] < weight:
#             continue
#         for nnode, nweight in g[node]:
#             cost = weight + nweight
#             if d[nnode] > cost:
#                 d[nnode] = cost
#                 hq.heappush(q,(nnode,cost))
#                 if cost == 1:
#                     friend.append(nnode)
#     return friend

# def bfs(f, s):
#     visited = [False] * (len(f)+1)
#     queue = deque()
#     queue.append((s,0))
#     while queue:
#         node, cnt = queue.popleft()
#         visited[node] = True
#         if sum(visited) >= len(f):
#             return cnt
#         for e in f[node]:
#             if not visited[e]:
#                 queue.append((e,cnt+1))

# def solution(n, lighthouse):
#     graph = [[] for _ in range(n+1)]
#     for l,r in lighthouse:
#         graph[l].append((r,1))
#         graph[r].append((l,1))
#     INF = int(1e9)
#     answer = INF
#     dlist = {}
#     for i in range(1,n+1):
#         dist = [INF] * (n+1)
#         dlist[i] = dijkstra(i,graph,dist)
#     for j in range(1,n+1):
#         answer = min(answer,bfs(dlist,j))
#     return answer