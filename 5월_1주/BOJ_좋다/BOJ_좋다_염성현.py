N = int(input())
graph = list(map(int,input().split()))
graph.sort()

def binary(N):
    answer = 0
    for i in range(N):
        tmp = graph[:i] + graph[i+1:]
        start = 0
        end = len(tmp)-1
        while start < end:
            t = tmp[start] + tmp[end]
            if t == graph[i]:
                answer += 1
                break 
            if t < graph[i]:
                start += 1
            else:
                end -= 1
    return answer 
print(binary(N))