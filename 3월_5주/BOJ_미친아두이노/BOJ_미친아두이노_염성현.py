from collections import deque
from collections import Counter
r,c  = map(int, input().split())

dx = [ 1, 1, 1, 0, 0, 0,-1,-1,-1]
dy = [-1, 0, 1,-1, 0, 1,-1, 0, 1]
graph = []
songa = []
mada = deque()
for i in range(r):
    temp = list(input())
    graph.append(temp)
    for j, k in enumerate(temp):
        if k == 'I':
            songa.append((i,j))
        elif k == 'R':
            mada.append((i,j))
jd = list(map(int,(list(input()))))

r1 = songa[0][0]
s1 = songa[0][1]
seconds = 0 
flag = 0 

for sd in jd:
    seconds += 1
    graph[r1][s1] = '.'
    r1 = r1+dx[sd-1]
    s1 = s1+dy[sd-1]
    
    if graph[r1][s1] == 'R':
        flag=1
        break
    else:
        graph[r1][s1] = 'I'

    mada_cand = []
    for j in range(len(mada)):
        r2, s2 = mada.popleft()
        graph[r2][s2] = '.'
        dr, ds = abs(r1-r2), abs(s1-s2)
                
        if dr > 0:
            if r2 > r1:
                r2 = r2 - 1
            else:
                r2 = r2 + 1
        if ds > 0:
            if s2 > s1:
                s2 = s2 - 1
            else:
                s2 = s2 + 1

        if graph[r2][s2] == 'I':
            flag = 1
            break
        else:
            mada_cand.append((r2,s2))

    for k, v in Counter(mada_cand).items():
        if v == 1:
            graph[k[0]][k[1]] = 'R'
            mada.append(k)
    
    if flag == 1:
        break

if flag == 1:
    print('kraj {}'.format(seconds))
else:
    for g in graph:
        print(''.join(g))
