import sys
input = sys.stdin.readline

def make_prime(num: int) -> list:
    num_list = [1] * (num+1)
    prime_list = [] 
    for i in range(2, num+1):
        if num_list[i]:
            prime_list.append(i)
            for j in range(2*i, num+1, i):
                num_list[j] = 0
    
    return prime_list

def solution(num):
    prime_list = make_prime(num)
    n = len(prime_list)
    if n == 0:
        return 0
    left, right = 0, 0
    sum_val = prime_list[0]
    cnt = 0
    while left <= right:
        if sum_val == num:
            sum_val -= prime_list[left]
            left += 1
            cnt += 1
        elif sum_val < num:
            if right + 1 < n:
                right += 1
                sum_val += prime_list[right]
            else:
                break
        else:
            sum_val -= prime_list[left]
            left += 1
    
    return cnt

N = int(input())
print(solution(N))