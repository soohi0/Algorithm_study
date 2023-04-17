def solution(sequence, k):
    #투포인터
    answer = []
    s, e = 0, 0
    sum_ = sequence[s]
    for _ in range(2000000):
        if sum_ < k:
            if e < len(sequence)-1:
                e += 1
                sum_ += sequence[e]
        elif sum_ > k:
            if s < len(sequence)-1 and s < e:
                sum_ -= sequence[s]
                s += 1
        else:
            answer.append([s, e])
            if s == len(sequence)-1 and e== len(sequence)-1:
                break
            if e < len(sequence)-1:
                e += 1
                sum_ += sequence[e]
            else:
                break

    gap = 1000000
    result = []
    for x, y in answer:
        if y - x < gap:
            gap = y-x
            result = [x, y]
    return result