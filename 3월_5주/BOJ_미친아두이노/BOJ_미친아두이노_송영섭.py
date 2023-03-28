R, C = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(R)]
direct_list = list(input())

i_list = [(i, j) for j in range(C) for i in range(R) if board[i][j] == 'I']
r_list = [(i, j) for j in range(C) for i in range(R) if board[i][j] == "R"]
cur_i = i_list[0]

d_j = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1] # index_0 은 direction 번호와 index를 같게 만들기 위함
d_i = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]

for cnt, direct in enumerate(direct_list):
    direct = int(direct)
    # move I
    next_i = (cur_i[0] + d_i[direct], cur_i[1] + d_j[direct])

    # I 가 이동한 위치에 R 이 있을 경우
    if next_i in r_list:
        print(f"kraj {cnt+1}")
        break

    # move R
    remove_list = set()
    r_set = set()
    for cur_r in r_list:
        min_distance, next_r = 100000, cur_r
        for idx in range(1, 10):
            tmp_r = (cur_r[0] + d_i[idx], cur_r[1] + d_j[idx])
            # 거리계산
            distance = abs(next_i[0] - tmp_r[0]) + abs(next_i[1] - tmp_r[1])
            # 가장 작은 거리일 경우로 갱신
            if distance < min_distance:
                min_distance = distance
                next_r = tmp_r

        # 중복확인
        if next_r not in r_set:
            r_set.add(next_r)
        else:
            remove_list.add(next_r)

    # I == R 일 시 
    if next_i in r_set:
        print(f"kraj {cnt+1}")
        break
    
    # 중복 제거
    for val in remove_list:
        r_set.remove(val)
    
    cur_i = next_i
    r_list = list(r_set)

else:
    result = [['.'] * C for _ in range(R)]
    result[cur_i[0]][cur_i[1]] = 'I'
    for i, j in r_list:
        result[i][j] = 'R'
    
    for i in result:
        print(''.join(i))