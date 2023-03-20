def solution(brown, yellow):
    # x * y = brown + yellow
    # x + y = 2 + brown // 2
    multiple = brown + yellow
    sum_ = 2 + brown // 2
    for y in range(1, sum_, 1):
        x = sum_ - y
        if x * y == multiple:
            return [x, y]