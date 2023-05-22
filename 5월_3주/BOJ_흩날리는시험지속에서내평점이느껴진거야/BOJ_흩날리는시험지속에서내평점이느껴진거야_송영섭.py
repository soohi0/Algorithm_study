import sys
input = sys.stdin.readline


def solution(n, k, s_list):

    left, right = 0, 20 * 10 ** 5 + 1
    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        sum_val = 0
        for score in s_list:
            if sum_val + score >= mid:
                sum_val = 0
                cnt += 1
            else:
                sum_val += score
        
        if cnt >= k:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


N, K = map(int, input().split())
score_list = list(map(int, input().split()))

print(solution(N, K, score_list))