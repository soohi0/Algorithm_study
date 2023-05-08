import sys
input = sys.stdin.readline

def solution(n: int, n_list: list) -> int:
    n_list.sort()
    left, right = 0, n-1
    min_left, min_right = left, right

    min_val = float('inf')
    while left < right:
        val = n_list[left] + n_list[right]
        if abs(val) < min_val:
            min_val = abs(val)
            min_left, min_right = left, right
        
        if val < 0:
            left += 1
        else:
            right -= 1

    return n_list[min_left], n_list[min_right]


if __name__ == "__main__":
    N = int(input())
    N_list = list(map(int, input().split()))
    print(*solution(N, N_list))