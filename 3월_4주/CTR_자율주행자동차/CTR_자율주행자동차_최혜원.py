import sys
sero, garo = map(int,sys.stdin.readline().split())
#0 북 1 동 2 남 3 서
s_y, s_x, d = map(int, sys.stdin.readline().split())
#좌회전은 하나 빼기
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
q = [(s_x, s_y, d)]
area = 1
road = []

for i in range(sero):
# for j in range(garo):
    r = list(map(int,sys.stdin.readline().split()))
    road.append(r)
# print(road)
road[s_y][s_x] = -1

while q:
    x, y, dir_ = q.pop(0)
    next_dir = dir_
    print("-----------------------------")
    for r in road:        
        print(r)
    isitgo = False
    for cnt in range(4):
        next_dir -= 1
        if next_dir < 0:
            next_dir += 4
        next_x = dirs[next_dir][0] + x
        next_y = dirs[next_dir][1] + y
        if road[next_y][next_x] == 0:
            #go
            q.append((next_x, next_y, next_dir))
            road[next_y][next_x] = -1
            area += 1
            isitgo = True
            break
    if isitgo == False:
        next_x = x - dirs[dir_][0]
        next_y = y - dirs[dir_][1]
        if road[next_y][next_x] != 1:
            q.append((next_x, next_y, dir_))
        else:
            break
print(area)

