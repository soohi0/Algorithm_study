import sys
from collections import deque
input = lambda : sys.stdin.readline()

def make_pos(point):
    return (ord(point[0])-65, int(point[1])-1)

def isinRange(x, y):
    if x < 8 and y < 8 and x >= 0 and y >= 0:
        return True
    return False
dirs = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 
        'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}#x, y

king, rock, n = input().split()
n = int(n)

start = make_pos(king)
rock = make_pos(rock)
cur_pos = start

for _ in range(n):
    go_dir = dirs[input().rstrip()]
    n_x, n_y = go_dir[0] + cur_pos[0], go_dir[1]+ cur_pos[1]
    if isinRange(n_x, n_y):
        if n_x == rock[0] and n_y == rock[1]:
            n_rock = (go_dir[0] + rock[0], go_dir[1]+ rock[1])
            if isinRange(n_rock[0], n_rock[1]):
                rock = n_rock
                cur_pos = (n_x, n_y)
        else:
            if isinRange(rock[0], rock[1]):
                cur_pos = (n_x, n_y)
    
print(chr(cur_pos[0]+65) + str(cur_pos[1]+1))
print(chr(rock[0]+65) + str(rock[1]+1))    
