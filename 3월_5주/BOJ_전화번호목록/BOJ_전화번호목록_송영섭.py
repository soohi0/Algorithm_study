import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    nums = [str(input()).rstrip() for _ in range(n)]
    nums.sort(key=lambda x: len(x))
    num_set = set()
    num_set.add(nums[0])
    check = 0
    for idx in range(1, n):
        if check == 1:
            break
        
        for length in range(1, len(nums[idx])):
            tmp = nums[idx][:length]
            if tmp in num_set:
                check = 1
                break

            num_set.add(nums[idx])

    print("YES") if check == 0 else print("NO")