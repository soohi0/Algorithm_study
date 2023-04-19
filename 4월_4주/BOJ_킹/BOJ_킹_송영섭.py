import sys
input = sys.stdin.readline

def convert_pos_to_idx(pos: str) -> tuple:
    idx1 = 9 - int(pos[1])
    idx2 = ord(pos[0]) - 64
    return (idx1, idx2)

def convert_idx_to_pos(idx1: int, idx2: int) -> str:
    string1 = chr(idx2 + 64)
    string2 = str(9 - idx1) 
    return string1 + string2

def move(command: str, king_idx: list, stone_idx: list) -> tuple:
    """
    return (n_king_idx1, n_king_idx2, n_stone_idx1, n_stone_idx2)
    """
    n_king_idx1, n_king_idx2 = king_idx
    n_stone_idx1, n_stone_idx2 = stone_idx
    if "R" in command:
        n_king_idx2 += 1
        n_stone_idx2 +=  1
    if "L" in command:
        n_king_idx2 -= 1
        n_stone_idx2 -= 1
    if "B" in command:
        n_king_idx1 += 1
        n_stone_idx1 += 1
    if "T" in command:
        n_king_idx1 -= 1
        n_stone_idx1 -= 1

    # 다음 좌표가 보드 안 검사
    if 1 <= n_king_idx1 <= 8 and 1 <= n_king_idx2 <= 8:
        if (n_king_idx1, n_king_idx2) == (stone_idx[0], stone_idx[1]):
            if 1 <= n_stone_idx1 <= 8 and 1 <= n_stone_idx2 <= 8:
                return (n_king_idx1, n_king_idx2, n_stone_idx1, n_stone_idx2)
        else:
            return (n_king_idx1, n_king_idx2, stone_idx[0], stone_idx[1])
        
    return (king_idx[0], king_idx[1], stone_idx[0], stone_idx[1])


king_pos, stone_pos, N = map(str, input().split())
king_idx1, king_idx2 = convert_pos_to_idx(king_pos)
stone_idx1, stone_idx2 = convert_pos_to_idx(stone_pos)

for _ in range(int(N)):
    command = str(input().rstrip())
    king_idx1, king_idx2, stone_idx1, stone_idx2 = move(command, [king_idx1, king_idx2], [stone_idx1, stone_idx2])

print(convert_idx_to_pos(king_idx1, king_idx2))
print(convert_idx_to_pos(stone_idx1, stone_idx2))