import sys
input = lambda : sys.stdin.readline().strip()

move = [(dx,dy) for dy in (1,0,-1) for dx in (-1,0,1)]

def solve(r, c, user_loc, krajs, queries):
    for X, query in enumerate(queries, 1):
        user_loc = [i+j for i,j in zip(user_loc, move[query])]
        if tuple(user_loc) in krajs:
            print(f"kraj {X}")
            exit()
        n_krajs = set()
        destroied = set()
        for kraj in krajs:
            n_kraj = []
            for uloc, kloc in zip(user_loc, kraj):
                diff = 0 if uloc==kloc else 1 if uloc>kloc else -1
                n_kraj.append(diff+kloc)
            if n_kraj == user_loc:
                print(f"kraj {X}")
                exit()
            robot = tuple(n_kraj)
            if robot in n_krajs:
                destroied.add(robot)
            else:
                n_krajs.add(robot)
        krajs = n_krajs-destroied
    board = [["."]*c for _ in range(r)]
    board[user_loc[1]][user_loc[0]] = "I"
    for kraj in krajs:
        board[kraj[1]][kraj[0]] = "R"
    for l in board:
        print(*l, sep="")

if __name__ == "__main__":
    r, c = map(int, input().split())
    jongsu, krajs = None, set()
    for rloc in range(r):
        line = input()
        if "I" in line:
            jongsu = (line.index("I"), rloc)
        for cloc, token in enumerate(line):
            if token == "R":
                krajs.add((cloc, rloc))
    solve(r, c, jongsu, krajs, queries = map(lambda x:int(x)-1, list(input())))