N = int(input())
graph = list(map(int,input().split()))
graph.sort()
s = 0
e = len(graph)-1
min_val = 1e9*2
while s < e:
    total = graph[s] + graph[e]
    if abs(total) < abs(min_val):
        min_val = total
        answer = (graph[s], graph[e])
        if answer == 0:
            break
    if total > 0 :
        e -= 1
    else:
        s += 1
print(*answer)
