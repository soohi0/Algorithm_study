import sys
input = sys.stdin.readline

n,k = int(input()),int(input())

def compare(i,j):
    if i==0: return 1
    elif i==1: return j
    elif j/i==2: return 2
    elif j/i<2: return 0
    else: return -1

dp = [[compare(i,j) for i in range(k+1)] for j in range(n+1)]

def solve(n,k):
    if dp[n][k] == -1:
        dp[n][k] = (solve(n-1,k) + solve(n-2,k-1)) % 1_000_000_003
    return dp[n][k]

print(solve(n,k))

"""
1. 추가되는 색을 선택한 경우 -> k에 1 빼준다.
    양옆의 색을 고르지 않아야 함. -> n에 2 빼준다.
        -> 2인 이유? : 해당 3칸을 선택된 1칸으로 생각하면 편함
2. 추가되는 색을 선택하지 않은 경우 -> k는 그대로.
    양 옆의 색은 무관하다 -> n에 1 빼준다.
"""