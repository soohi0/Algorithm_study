from collections import deque
def get_1dist(pre_word, words, len_word):
    dist1s = []
    for word in words:
        cnt = 0
        for idx in range(len_word):
            if pre_word[idx] != word[idx]:
                cnt += 1
        if cnt == 1:
            dist1s.append(word)
    return dist1s
def solution(begin, target, words):
    answer = 0
    
    if target in words:
        words_q = deque([[begin, 0]])
        len_word = len(begin)
        while words_q:
            pre_word, turn = words_q.popleft()
            if pre_word == target:
                return turn
            dist1s = get_1dist(pre_word, words, len_word)
            # print(dist1s)
            if len(dist1s) != 0:
                for dist1 in dist1s:
                    words_q.append([dist1, turn+1])
    else:
        return answer