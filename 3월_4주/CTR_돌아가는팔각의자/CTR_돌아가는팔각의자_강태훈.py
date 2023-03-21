import sys
input = sys.stdin.readline

top_index = [0]*4
graph = [list(input().strip()) for _ in range(4)]
tc = [list(map(int, input().split())) for _ in range(int(input()))]

is_turnable = lambda list_idx1, list_idx2: graph[list_idx1][(top_index[list_idx1]+2)%8] != graph[list_idx2][(top_index[list_idx2]+6)%8]
turn = lambda idx, val : (top_index[idx]-val)%8

def determine_turnable_table(table_num, direction):
    l = r = table_num-1
    ldir = rdir = direction
    yield l, direction
    while l > 0 and is_turnable(l-1, l):
        l -= 1
        ldir *= -1
        yield l, ldir
    while r < 3 and is_turnable(r, r+1):
        r += 1
        rdir *= -1
        yield r, rdir

for table_num, direction in tc:
    for idx, turn_dir in list(determine_turnable_table(table_num, direction)):
        top_index[idx] = turn(idx, turn_dir)

print(sum([(2**i)*int(graph[i][val]) for i, val in enumerate(top_index)]))