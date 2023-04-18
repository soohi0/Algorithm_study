# https://suri78.tistory.com/15
import sys 
input = lambda : sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    K = int(input())
    Klist = list(map(int, input().split()))
    dp = [[0]*K for _ in range(K)]
    for i in range(K-1):
        # 연속된 두 값을 묶어주기
        dp[i][i+1] = Klist[i] + Klist[i+1]
        # i+2부터는 이전 dp + 현재 인덱스의 값
        for j in range(i+2,K):
            dp[i][j] = dp[i][j-1] + Klist[j]
    # 마지막 합쳐줄 때 어느 비용을 사용할 것인가
    # => 마지막 합의 비용이 아닌 그 이전의 비용
    # (page[0] + page[1]) + page[2]
    # (40 + 30) + (70 + 30) # 첫 번째 합의 비용 40+30 = 70, 이후 두 번째 합의 비용 70+30 = 100
    # page[0] + (page[1] + page[2])
    # (30 + 30) + (60 + 40) # 첫 번째 합의 비용 30+30 = 60, 이후 두 번째 합의 비용 60+40 = 100
    for d in range(2,K):
        for i in range(K-d):
            j = i+d 
            # i~k까지 더한 비용의 최솟값 + K+1~j까지 더한 비용의 최솟값
            minimum = [dp[i][K] + dp[K+1][j] for K in range(i,j)]
            dp[i][j] += min(minimum)
    print(dp[0][K-1])