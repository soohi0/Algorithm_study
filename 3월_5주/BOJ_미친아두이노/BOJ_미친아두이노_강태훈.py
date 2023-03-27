import sys
input = lambda : sys.stdin.readline().strip()

# 이동 방향에 따른 좌표변화값 저장
move = [(dx,dy) for dy in (1,0,-1) for dx in (-1,0,1)]

def solve(r, c, user_loc, krajs, queries):
    """ 유저 위치와 로봇들의 위치만 입력받습니다.

    Args:
        r (int): 필드의 세로 길이
        c (int): 필드의 가로 길이
        user_loc (list): 유저의 초기 위치
        krajs (set(list)): 미친 아두이노들의 현재 위치를 set으로
        queries (list): 유저의 이동방향을 0부터 시작하는 숫자로 표현한 리스트
    """
    for X, query in enumerate(queries, 1):
        # 유저 이동
        user_loc = [i+j for i,j in zip(user_loc, move[query])]
        # 이동 후 아두이노와 동일 좌표에 있으면 종료
        if tuple(user_loc) in krajs:
            print(f"kraj {X}")
            exit()
        n_krajs = set()
        destroied = set()
        # 미친 아두이노들에 대하여
        for kraj in krajs:
            # 가까운 방향으로 이동, 차이만 계산하면 된다.
            n_kraj = []
            for uloc, kloc in zip(user_loc, kraj):
                diff = 0 if uloc==kloc else 1 if uloc>kloc else -1
                n_kraj.append(diff+kloc)
            # 아두이노가 유저와 동일한 위치로 이동 시 종료
            if n_kraj == user_loc:
                print(f"kraj {X}")
                exit()
            # 겹치면 파괴
            robot = tuple(n_kraj)
            if robot in n_krajs:
                destroied.add(robot)
            else:
                n_krajs.add(robot)
        # 파괴된 아두이노 배제
        krajs = n_krajs-destroied
    # 출력을 위한 보드 설정
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