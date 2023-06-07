import sys
input = sys.stdin.readline

def dfs_solution(r, c, board):
    max_val = 0
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    str_check = [0] * 26

    def dfs(n: int, cur: tuple):
        nonlocal max_val, dx, dy, str_check

        if n > max_val:
            max_val = n

        cx, cy = cur
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                alphabet = board[nx][ny]
                idx_str_check = ord(alphabet) - 65
                if str_check[idx_str_check] == 0:
                    str_check[idx_str_check] = 1
                    dfs(n+1, (nx, ny))
                    str_check[idx_str_check] = 0

    str_check[ord(board[0][0])-65] = 1
    dfs(1, (0, 0))
    return max_val


if __name__ == "__main__":
    R, C = map(int, input().split())
    board = [list(map(str, input().rstrip())) for _ in range(R)]
    print(dfs_solution(R, C, board))