import sys
input = sys.stdin.readline

sudoku = []
empty_list = []
for _ in range(9):
    sudoku.append(list(map(str, input().rstrip())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == '0':
            empty_list.append((i, j))

def check_row(num, idx1, idx2):
    global sudoku
    for i in range(9):
        if sudoku[idx1][i] == num:
            return False
    return True

def check_column(num, idx1, idx2):
    global sudoku
    for i in range(9):
        if sudoku[i][idx2] == num:
            return False
    return True

def check_box(num, idx1, idx2):
    global sudoku
    start_i, start_j = idx1//3 * 3, idx2//3 * 3 
    for i in range(start_i, start_i+3):
        for j in range(start_j, start_j+3):
            if sudoku[i][j] == num:
                return False
    return True

def dfs(n):
    global empty_list, sudoku

    if n == len(empty_list):
        for i in sudoku:
            print(''.join(i))
        exit()

    idx1, idx2 = empty_list[n]
    for num in range(1, 10):
        num = str(num)
        if check_row(num, idx1, idx2) and check_column(num, idx1, idx2) and check_box(num, idx1, idx2):
            sudoku[idx1][idx2] = num
            dfs(n+1)
            sudoku[idx1][idx2] = '0'


dfs(0)