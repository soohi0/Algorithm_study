import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def search(num: int, graph: dict, time_list: list, memory: list) -> int:
    que = deque()
    que.append(num)

    if memory[num]:
        return memory[num]

    sum_val = time_list[num]
    while que:
        cur_val = que.popleft()
        if len(graph[cur_val]) > 1:
            sum_val += max(*[search(next_val, graph, time_list, memory) for next_val in graph[cur_val]])
        elif graph[cur_val]:
            next_val = graph[cur_val][0]
            sum_val += time_list[next_val]
            que.append(next_val)

    memory[num] = sum_val
    return sum_val

def solution(n: int, graph: dict, time_list: list) -> None:
    dy = [0] * (n+1)
    result = [] 
    for num in range(1, n+1):
        result.append(search(num, graph, time_list, dy))

    for i in result:
        print(i)


if __name__ == "__main__":
    N = int(input())
    graph = defaultdict(list)
    time_list = [0] * (N+1)
    for i in range(1, N+1):
        build = list(map(int, input().split()))
        time_list[i] = build[0]
        if len(build) == 2:
            graph[i] = []
        else:
            for j in build[1:-1]:
                graph[i].append(j)

    solution(N, graph, time_list)