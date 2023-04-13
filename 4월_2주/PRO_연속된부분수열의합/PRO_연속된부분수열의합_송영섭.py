def solution(sequence, k):
    left, right = 0, 0
    sum_val = sequence[0]
    min_length = 1000001
    result = [left, right]
    while left <= right:
        if sum_val < k and right + 1 < len(sequence):
            right += 1
            sum_val += sequence[right]
        else:
            if sum_val == k and right-left+1 < min_length:
                min_length = right - left + 1
                result = [left, right]
            sum_val -= sequence[left]
            left += 1
            
    return result