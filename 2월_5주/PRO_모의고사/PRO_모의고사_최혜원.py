def solution(answers):
    result = []
    supo1 = [1,2,3,4,5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct_cnts = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == supo1[idx%len(supo1)]:
            correct_cnts[0] += 1
        if answer == supo2[idx%len(supo2)]:
            correct_cnts[1] += 1
        if answer == supo3[idx%len(supo3)]:
            correct_cnts[2] += 1
    max_ = max(correct_cnts)
    for idx in range(3):
        if correct_cnts[idx] == max_:
            result.append(idx+1)


    return result