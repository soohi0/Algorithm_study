import sys
input = sys.stdin.readline

def solution(nums, n, k):
    nums.sort()
    mindist = float("inf")
    answer = 0
    s, e = 0, n-1
    while s<e:
        sumval = nums[s] + nums[e]
        dist = abs(sumval-k)
        if sumval > k:
            e -= 1
        else:
            s += 1
        if dist < mindist:
            mindist = dist
            answer = 0
        elif dist^mindist:
            continue
        answer += 1
    return answer

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n, k = map(int, input().split())
        print(solution(list(map(int, input().split())), n, k))
