N = int(input())
rec = [list(map(int, input().split())) for _ in range(N)]
rec.sort(key = lambda x: -x[1])
maxw = rec[0][0]
maxh = rec[0][1]

answer = 0
prevw = 0
prevh = 0
rec.sort()
for rx, ry in rec:
    answer += (rx-prevw) * prevh
    prevh = max(prevh,ry)
    if rx==maxw:
        break
    prevw = rx

prevw = rec[-1][0]+1
prevh = 0
for rx, ry in rec[::-1]:
    answer += (prevw-rx) * prevh
    prevh = max(prevh,ry)
    if rx==maxw:
        break
    prevw = rx

answer += maxh
print(answer)