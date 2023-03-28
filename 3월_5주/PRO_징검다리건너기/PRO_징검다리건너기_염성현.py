def solution(stones, k):
    left = 1
    right = 400000000
    while left <= right:
        temp = stones.copy()
        # mid : 건널 수 있는 니니즈의 수
        mid = (left + right) // 2
        cnt = 0
        # 연속으로 건널 수 있는지 체크
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            # k 내에서 건널 수 없다면 break
            if cnt >= k:
                break
        print(mid, left, right, cnt)
        # k 내에서 건널 수 없다는 것은 곧 더 적은 수가 건너야 한다는 것
        # mid 보다 작은 왼쪽 범주 검색
        if cnt >= k:
            right = mid - 1
        # k 내에서 건널 수 있다는 것은 곧 더 많은 수가 건널 수 있다는 것
        # mid 보다 큰 오른쪽 범주 검색
        else:
            left = mid + 1
        
    return left