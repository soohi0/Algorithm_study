import sys
input = lambda : sys.stdin.readline().rstrip()

direction = {'R':(1,0),
             'L':(-1,0),
             'B':(0,-1),
             'T':(0,1),
             'RT':(1,1),
             'LT':(-1,1),
             'RB':(1,-1),
             'LB':(-1,-1)}

loc2idx = lambda x : (ord(x[0])-ord('A'), int(x[1])-1)
idx2loc = lambda x,y : chr(ord('A')+x)+str(y+1)

is_in_grid = lambda c : all([0<=i<8 for i in c])

def solve(king, stone, n, move_dirs):
    sx, sy = loc2idx(stone)
    kx, ky = loc2idx(king)
    for dx, dy in move_dirs:
        knx, kny = kx+dx, ky+dy
        snx, sny = sx+dx, sy+dy
        if not is_in_grid([knx, kny]):
            continue
        if (knx,kny) == (sx, sy):
            if is_in_grid([snx,sny]):
                kx, ky, sx, sy = knx, kny, snx, sny
        else:
            kx, ky = knx, kny
    return idx2loc(kx, ky), idx2loc(sx, sy)


if __name__=="__main__":
    king, stone, _n = input().split()
    n = int(_n)
    move_dirs = [direction[input()] for _ in range(n)]
    print(*solve(king, stone, n, move_dirs), sep="\n")