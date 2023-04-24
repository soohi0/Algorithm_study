from collections import deque 

K, S, N = input().split()
direction = {'R':(0,1),
             'L':(0,-1),
             'B':(1,0),
             'T':(-1,0),
             'RT':(-1,1),
             'LT':(-1,-1),
             'RB':(1,1),
             'LB':(1,-1)}

def chess_to_idx(p):
    return (8-int(p[1]),int(ord(p[0])-ord('A')))
def idx_to_chess(p):
    return chr(ord('A')+p[1])+str(8-p[0])

Kidx = chess_to_idx(K)
Sidx = chess_to_idx(S)

for _ in range(int(N)):
    d = input()
    kx, ky = Kidx
    dx, dy = direction[d]
    nx, ny = kx+dx, ky+dy    
    if 0<=nx<8 and 0<=ny<8:
        if (nx,ny) == Sidx:
            if 0<=nx+dx<8 and 0<=ny+dy<8:
                Sidx = (nx+dx,ny+dy)
            else:
                continue
        Kidx = (nx, ny)

print(idx_to_chess(Kidx))
print(idx_to_chess(Sidx))