import sys
input = sys.stdin.readline

def sol(n, k, nums):
    nums.sort()
    min_val = float('inf')

    left, right = 0, n-1
    cnt = 0
    while left < right:
        val = nums[left] + nums[right]

        distance = abs(k - val)
        if distance < min_val:
            min_val = distance
            cnt = 1
        
        elif distance == min_val:
            cnt += 1
        
        if val <= k:
            left += 1
        else:
            right -= 1
        
    return cnt


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, K = map(int, input().split())
        nums = list(map(int, input().split()))
        print(sol(n, K, nums))