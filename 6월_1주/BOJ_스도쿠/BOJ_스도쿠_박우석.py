board = [list(map(int, list(input()))) for _ in range(9)]

# 먼저 빈칸 찾기
def find_blank():
    blanks = []
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                blanks.append((x, y))
    return blanks

# 백트래킹 - 순서대로 채워나감
def recur(blanks, board, i):
    global found
    if found: return

    if i >= len(blanks):
        found = True
        for b in board:
            print(''.join([str(x) for x in b]))
        return
    bx, by = blanks[i]
    # set 으로 남는 숫자만 한해서 진행
    number = set(range(1, 10))
    row = set(board[bx]); col = set([b[by] for b in board])
    # 정사각형 구역
    xl, yl = bx//3, by//3
    sq = set([board[sx][sy] for sy in range(yl*3, yl*3+3) for sx in range(xl*3, xl*3+3)])
    number -= (row.union(col).union(sq))
    if not number:
        return
    else:
        number = sorted(list(number))
        for num in number:
            board[bx][by] = num
            recur(blanks, board, i+1)
            board[bx][by] = 0
   
found = False
blanks = find_blank()
recur(blanks, board, 0)