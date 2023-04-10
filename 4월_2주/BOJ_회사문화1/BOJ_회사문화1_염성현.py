from collections import defaultdict
n, m = map(int,input().split())
boss = list(map(int,input().split()))
total = [0]*(n+1)

tree = defaultdict(list)
for i in range(1,n):
    tree[boss[i]].append(i+1)

for i in range(m):
    a, b =map(int, input().split())
    total[a] += b

def dfs(a):
    visited = [False]*(n+1)
    queue = []
    queue.append(a)
    while queue:
        next = queue.pop()
        if visited[next]:
            continue 
        visited[next]= True 
        for i in tree[next]:
            if not visited[i]:
                queue.append(i)
                total[i] += total[next]
dfs(1)
print(*total[1:])