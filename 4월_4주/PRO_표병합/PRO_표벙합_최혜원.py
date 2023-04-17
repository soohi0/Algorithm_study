def find_merged(merged, p):
    for idx in range(len(merged)):
        if p in merged[idx]:
            return idx
    return -1
def value_update(merged, table, r, c, value):
    idx_orF = find_merged(merged, (r,c))
    if idx_orF == -1:
        table[r][c] = value
    else:
        for m1,m2 in merged[idx_orF]:
            table[m1][m2] = value
def change_value(table, v1, v2):
    for y in range(len(table)):
        for x in range(len(table[0])):
            if table[y][x] == v1:
                table[y][x] = v2
def merge_point(merged, table, p1, p2):
    idx_orF1 = find_merged(merged, p1)
    idx_orF2 = find_merged(merged, p2)
    
    if idx_orF1== -1 and idx_orF2 == -1:
        merged.append({p1, p2})
        if table[p1[0]][p1[1]] != '':
            table[p2[0]][p2[1]] = table[p1[0]][p1[1]]
        else:
            table[p1[0]][p1[1]] = table[p2[0]][p2[1]]
    elif idx_orF1 == -1:
        merged[idx_orF2].add(p1)
        if table[p1[0]][p1[1]] != '':
            for m1,m2 in merged[idx_orF2]:
                table[m1][m2] = table[p1[0]][p1[1]]
        else:
            table[p1[0]][p1[1]] = table[p2[0]][p2[1]]
    elif idx_orF2 == -1:
        merged[idx_orF1].add(p2)
        if table[p1[0]][p1[1]] != '':
            table[p2[0]][p2[1]] = table[p1[0]][p1[1]]
        else:
            for m1,m2 in merged[idx_orF1]:
                table[m1][m2] = table[p2[0]][p2[1]]
    else:
        if idx_orF2 != idx_orF1:
            if table[p1[0]][p1[1]] != '':
                for m1,m2 in merged[idx_orF2]:
                    table[m1][m2] = table[p1[0]][p1[1]]
            else:
                for m1,m2 in merged[idx_orF1]:
                    table[m1][m2] = table[p2[0]][p2[1]]
            merged[idx_orF1] |= merged[idx_orF2]
            merged.pop(idx_orF2)
        else:
            pass
    # print(merged)
        
def solution(commands):
    answer = []
    new_commands = [c.split() for c in commands]
    table = [['' for __ in range(51)] for _ in range(51)]
    merged = []

    for command in new_commands:
        # print(command)
        if command[0]== 'UPDATE':
            if len(command) == 4:
                value_update(merged,table, int(command[1]), int(command[2]), command[3])
            elif len(command) == 3:
                change_value(table, command[1], command[2])
        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1]),int(command[2]),int(command[3]),int(command[4])
            if r1 == r2 and c1 == c2:
                continue
            else:
                merge_point(merged,table, (r1,c1), (r2,c2))
        elif command[0] == 'UNMERGE':
            r1, c1 = int(command[1]),int(command[2])
            idx_orF = find_merged(merged, (r1,c1))
            if idx_orF == -1:
                continue
            else:
                v = ''
                for m1, m2 in merged[idx_orF]:
                    v = table[m1][m2]
                    table[m1][m2] = ''
                merged.pop(idx_orF)
                table[r1][c1] = v
        elif command[0] == 'PRINT':
            r1, c1 = int(command[1]),int(command[2])
            re = table[r1][c1]
            if re == '':
                answer.append("EMPTY")
            else:
                answer.append(re)
                
        # for t in table[1:5]:
        #     print(t[1:5])
        # print('---------')
                
    return answer