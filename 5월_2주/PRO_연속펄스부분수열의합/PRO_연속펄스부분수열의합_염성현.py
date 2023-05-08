def sliding(graph):
    dp = [0]*len(graph)
    dp[0] = graph[0]
    for i in range(1,len(graph)):
        dp[i] = max(graph[i]+dp[i-1],graph[i])
    return max(dp)

def solution(sequence):
    answer = 0
    p_pulse = ([1,-1]*len(sequence))[:len(sequence)]
    m_pulse = ([-1,1]*len(sequence))[:len(sequence)]
    p_sum = []
    m_sum = []
    for s,p,m in zip(sequence, p_pulse, m_pulse):
        p_sum.append(s*p)
        m_sum.append(s*m)
    answer = max(sliding(p_sum),sliding(m_sum))
    return answer