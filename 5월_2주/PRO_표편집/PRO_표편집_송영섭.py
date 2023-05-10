
def cur_move(cmd: str, move: int, cur: int, table):
    if cmd == 'U':
        for _ in range(move):
            cur = table[cur][0]
    else:
        for _ in range(move):
            cur = table[cur][1]

    return cur

def del_idx(cur, n, table, del_stack):
    del_stack.append(cur)
    pre_idx, next_idx = table[cur]
    check = 0
    if next_idx < n:
        table[next_idx][0] = pre_idx
        check = 1
    if 0 <= pre_idx:
        table[pre_idx][1] = next_idx

    cur = next_idx if check == 1 else pre_idx
    
    return cur

def undo(cur, table, n, del_stack, result):
    new_idx = del_stack.pop()
    left, right = new_idx-1, new_idx+1
    idx = None
    while True:
        if 0 <= left and result[left] == 'O':
            idx = left
            pre_idx, next_idx = table[idx]
            table[new_idx] = [idx, next_idx]
            table[idx][1] = new_idx
            if next_idx < n:
                table[next_idx][0] = new_idx
            break
        if right < n and result[right] == 'O':
            idx = right
            pre_idx, next_idx = table[idx]
            table[new_idx] = [pre_idx, idx]
            table[idx][0] = new_idx
            if 0 <= pre_idx:
                table[pre_idx][1] = new_idx
            break
        
        left, right = left-1, right+1

    return cur

def solution(n, k, cmd):
    table = {i: [i-1, i+1] for i in range(n)}
    result = ['O'] * n
    del_stack = []
    cur = k
    for c in cmd:
        if len(c.split()) == 2:
            c, x = c.split()
            cur = cur_move(c, int(x), cur, table)
        elif c == 'C':
            result[cur] = 'X'
            cur = del_idx(cur, n, table, del_stack)
        elif c == 'Z':
            result[del_stack[-1]] = 'O'
            cur = undo(cur, table, n, del_stack, result)
    
    return ''.join(result)