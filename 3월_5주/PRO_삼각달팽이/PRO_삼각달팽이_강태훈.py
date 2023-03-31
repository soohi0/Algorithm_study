from itertools import zip_longest
import sys
sys.setrecursionlimit(10**6)

rot120 = lambda arr: [i for i in map(lambda x:list(strip(list(x))), list(zip_longest(*arr)))][::-1]
divide = lambda arr, n: [arr[i*(i+1)//2:i*(i+1)//2+i+1] for i in range(n)]
strip = lambda line : list(filter(lambda x:x, line))

# 재귀로 구현 -> 시간 초과
def solution(n):
    if n==1:
        return [1]
    else:
        arr = [[]] + rot120(divide(list(map(lambda x:x+n, solution(n-1))),n-1))
        for i in range(n):
            arr[i].insert(0,i+1)
    return sum(arr,[])

# 재귀를 for문으로 변경 -> 시간 초과, 배열 조작 횟수가 워낙 많은게 원인
def solution(n):
    arr = [1]
    for j in range(1, n):
        arr = [[]] + rot120(divide(list(map(lambda x:x+j, arr)),j-1))
        for i in range(j):
            arr[i].insert(0,i+1)
        arr = sum(arr,[])
    return arr

# 성공! 진행 방향으로 나아가 보고 배열의 범위를 벗어나거나 값이 이미 존재하는 칸에 들어가게 되면 방향을 바꾼다.
dx = [0,1,-1]
dy = [1,0,-1]

def solution(n):
    if n==1: 
        return [1]
    arr = [[0]*(i+1) for i in range(n)]
    x, y, direction, cnt = 0, 0, 0, 1
    while True:
        if arr[y][x]:
            return sum(arr, [])
        arr[y][x] = cnt
        cnt += 1
        nx, ny = x+dx[direction], y+dy[direction]
        if ( ny < 0 or ny >= len(arr) or nx < 0 or nx >= len(arr[ny]) or arr[ny][nx]):
            direction = (1+direction)%3
            nx, ny = x+dx[direction], y+dy[direction]
        x, y = nx, ny
