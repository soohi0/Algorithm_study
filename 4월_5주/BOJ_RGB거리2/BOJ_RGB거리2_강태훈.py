import sys
input = sys.stdin.readline

def main():
    n = int(input())
    fees = [list(map(int, input().split())) for _ in range(n)]

    ans = float("inf")
    # 첫 집의 색을 Fix하고 생각해봄
    for first_house in range(3):
        dp = [[float("inf")]*3]
        
        # 첫 집만 갱신해둔 상태에서
        dp[-1][first_house] = fees[0][first_house]
        
        for fees_index in range(1, n):
            # i번째를 고를 경우 i+1, i-1 만 생각하면 됨
            dp.append([fees[fees_index][i] + min([dp[fees_index-1][(i+1)%3],dp[fees_index-1][(i-1)%3]]) for i in range(3)])
        # 정답 갱신하되, 첫 집과 끝 집은 달라야함
        ans = min(ans, *[dp[-1][last_house] for last_house in range(3) if last_house != first_house])
    print(ans)


if __name__=="__main__":
    main()