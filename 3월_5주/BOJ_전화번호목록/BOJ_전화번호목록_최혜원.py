import sys
input = lambda : sys.stdin.readline().strip()

t_ = int(input())
answers = []
for t in range(t_):
    n_ = int(input())
    strs = [input() for _ in range(n_)]
    strs = sorted(strs)
    max_str = max(strs, key = len)
    checker = [[string for string in strs]]
    i = 0
    set_no = False
    while i < max_str and set_no == False:
        new_checker = []
        for check in checker:
            bf_s = '-'
            bf_strs= []
            for c in range(len(check)):
                try:
                    if bf_s == '-':
                        bf_s = check[c][0]
                        bf_strs.append(check[c][1:])
                    elif bf_s == check[c][0]:
                        bf_strs.append(check[c][1:])
                    else:
                        new_checker.append(bf_strs)
                        bf_strs = []
                        bf_s = check[c][0]
                        bf_strs.append(check[c][1:])
                except:
                    if check[c] == '' and len(check) > 1:
                        answers.append('NO')
                        set_no = True
                        break
            if set_no == True:
                break
            new_checker.append(bf_strs)
        checker = [n_check for n_check in new_checker]
        print(checker)
        i += 1
    if set_no == False:
        answers.append("YES")
print(*answers)