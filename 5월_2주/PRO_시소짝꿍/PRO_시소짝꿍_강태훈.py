from collections import defaultdict
cases = {i/j for i in (2,3,4) for j in (2,3,4)}
def solution(weights):
    answer = 0
    info = defaultdict(int)
    for w in weights:
        answer += sum([info[w*i] for i in cases])
        info[w] += 1
    return answer