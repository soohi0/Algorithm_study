import sys 
input = lambda : sys.stdin.readline().strip()

N, M = map(int,input().split())
T = list(map(int,input().split()))
partyl = list()

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node 
    rank[node] = 0

def connet(party):
    for p in range(len(party)-1):
        if find(party[p]) != find(party[p+1]):
            union(party[p], party[p+1])
    
for i in range(N+1):
    make_set(i)

for j in range(M):
    party = list(map(int,input().split()))
    partyl.append(party[1])
    connet(party[1:])
    
if T[0] == 0:
    print(M)
else:
    answer = 0
    for p in partyl:
        flag = 0
        for t in T[1:]:        
            if find(p) == find(t):
                flag = 1 
                break 
        if flag == 0:
            answer += 1
    print(answer)