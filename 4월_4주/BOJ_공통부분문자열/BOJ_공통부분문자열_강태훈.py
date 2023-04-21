import sys
input = lambda : sys.stdin.readline().rstrip()

def main(s1, s2):
    l1, l2, answer = len(s1), len(s2), 0
    dp = [0]*l2
    for i1 in range(l1):
        dp_sub = [0]*l2
        for i2 in range(l2):
            dp_sub[i2] = (min(i2,1)*dp[i2-1] + 1)*(s1[i1]==s2[i2])
        answer = max(answer, max(dp_sub))
        dp = dp_sub
    print(answer)

if __name__ == "__main__":
    s2, s1 = sorted([input() for _ in range(2)], key=len)
    main(s1, s2)

# LCS, Longest Common Substring