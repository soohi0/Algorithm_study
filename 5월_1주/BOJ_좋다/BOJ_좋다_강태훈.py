import sys
input = sys.stdin.readline

from bisect import bisect_right

def solve(n, nums):
    answer = 0
    for i in range(n):
        local = nums[:i]+nums[i+1:]
        s = 0
        e = min(bisect_right(local, nums[i]-local[s]), n-2)
        while s < e:
            found_value = local[s]+local[e]
            if found_value==nums[i]:
                answer+=1
                break
            elif found_value < nums[i]:
                s += 1
            else:
                e -= 1
    return answer

if __name__ == "__main__":
    n = int(input())
    nums = sorted(map(int, input().split()))
    print(solve(n, nums))
