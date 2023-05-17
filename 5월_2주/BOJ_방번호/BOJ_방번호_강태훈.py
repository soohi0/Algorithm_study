import sys
input = sys.stdin.readline

def solve(n, p, m):
    if m==0:
        print(0)
    else:
        # 정답 배열 메모이제이션
        dp = [-float("inf")]*(m+1)
        # 큰 번호부터 순회
        for i, price in reversed([[i,j] for i,j in enumerate(p)]):
            # 살 수 있는 방들에 대하여
            for j in range(price, m+1):
                # 사지 않는 경우, 사는 경우, 처음 사는 경우 중 가장 큰 값으로 갱신
                dp[j] = max(dp[j], dp[j-price]*10+i, i)
        print(dp[m])
    return

if __name__ == "__main__":
    solve(
        n=int(input()),
        p=list(map(int, input().split())), 
        m=int(input())
    )