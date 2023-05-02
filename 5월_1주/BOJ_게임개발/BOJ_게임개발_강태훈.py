import heapq
import sys
input = sys.stdin.readline


def solution(n):
    # 건물 완성 최소시간
    answer = [0 for _ in range(n)]
    # 가중치와 그래프 초기화
    w, graph = [], [[] for _ in range(n)]
    # in_degree
    in_degree = [0 for _ in range(n)]

    for idx in range(n):
        info = list(map(int, input().split()))[:-1]
        w.append(info[0])
        nodes = info[1:]
        in_degree[idx] += len(nodes)
        for k in info[1:]:
            graph[k-1].append(idx)
    hq = [(w[i], i) for i in range(n) if not in_degree[i]]

    # topology sort
    while hq:
        t, build = heapq.heappop(hq)
        answer[build] = t
        for p in graph[build]:
            in_degree[p] -= 1
            if not in_degree[p]:
                heapq.heappush(hq, (t + w[p], p))
    print(*answer, sep='\n')


if __name__ == "__main__":
    solution(n=int(input()))
