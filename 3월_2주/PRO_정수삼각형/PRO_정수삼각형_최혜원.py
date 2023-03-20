def solution(triangle):
    answer = 0
    for idx, line in enumerate(triangle[1:]):
        for idx_l, num in enumerate(line):
            if idx_l > 0 and idx_l < len(line)-1:
                triangle[idx+1][idx_l] += max(triangle[idx][idx_l-1], triangle[idx][idx_l])
            elif idx_l == 0:
                triangle[idx+1][idx_l] += triangle[idx][idx_l]
            elif idx_l == len(line)-1:
                triangle[idx+1][idx_l] += triangle[idx][idx_l-1]
    return max(triangle[-1])