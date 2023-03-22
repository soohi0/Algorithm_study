# from collections import deque

# def fromsum_dfs(v,s,g,m):
#     queue = deque([v])
#     while queue:
#         intensity, node = queue.popleft()
#         visited[node] = True
#         max_intensity = max(m, intensity)
#         if node in g:
#             answer.append([s, max_intensity])
#             break
#         for c in graph[node]:
#             w, d = c
#             if not visited[d]:
#                 fromsum_dfs([w,d],s,g,max_intensity)

# def solution(n,paths, gates, summits):
#     # n : xx 산의 지점 수
#     # paths : 각 등산로의 정보를 담은 2차원 정수 배열
#     # gates : 출입구들의 번호가 담긴 정수 배열
#     # summits : 산봉우리들의 번호가 담긴 정수 배열
#     # return : [산봉우리의 번호, intensity의 최솟값]
#     global graph
#     global visited
#     global answer
#     graph = {}
#     for p in paths:
#         i, j , w = p
#         graph[i] = graph.get(i, [])+[[w,j]]
#         graph[j] = graph.get(j, [])+[[w,i]]
#         graph[i].sort()
#         graph[j].sort()
#     answer = []
#     for s in summits:
#         visited = [False] * (n+1)
#         fromsum_dfs([0,s],s,gates,0)
#     answer.sort(key=lambda x: (x[1],x[0]))
#     return answer[0]

def solution(n, paths, gates, summits):
    field = {}
    answer = [-1, 10000001]
    
    # 경로 맵 초기화
    for A, B, time in paths:
        for x, y in ((A, B), (B,A)):
            field[x] = field.get(x,[]) + [(y,time)]
    
    # intensity 최대값으로 초기화, 다익스트라(?)
    intensity = [10000001] * (n+1)
    
    for gate in gates:
        intensity[gate] = 0
    
    # check : 정상 확인용
    check = set(summits)
    # stack : gates에서부터 시작
    stack = gates
    # 첫번째 반복문 : 정상까지 도달할 단계가 더 존재하는지 아닌지 확인
    while stack:
        target = set()
        # 두번째 반복문 : 각 단계에서 가능한 모든 연결을 탐색하며 도착 노드까지의 최소 intensity를 환원
        while stack:
            now = stack.pop()
            for to, time in field[now]:
                # 간선의 intensity 갱신
                max_time = max(intensity[now], time)
                # 최소 intensity 갱신
                if intensity[to] > max_time:
                    intensity[to] = max_time
                    # 정상이면 더 이상 뻗어가지 못하게
                    if to not in check:
                        target.add(to)
        stack = list(target)
    # 결과 : gates로부터의 도달 가능한 각 index의 intensity 최소값이 저장
    return min([[summit, intensity[summit]] for summit in summits], key=lambda x: (x[1], x[0]))