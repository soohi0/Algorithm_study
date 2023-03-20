def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr, r-1):
                yield [arr[i]] + next
    
import itertools
def solution(numbers):
    number = [int(s) for s in numbers]
    answer = 0
    
    num_set = set()
    # print(number)
    for i in range(1, len(number)+1):
        for nums in itertools.permutations(number, i):
            num_str = ''
            for num in nums:
                num_str += str(num)
            num_set.add(int(num_str))
    
        
#     #eratostenes's
    max_number = 5599999
    sosus = [False, False] + [True] * (max_number-1) #idx = 1 -> num1
    
    for i in range(2, len(sosus)):
        for j in range(2 * i, max_number, i):
            if sosus[j] == True:
                    sosus[j] = False
    answer = 0
    for num in num_set:
        if sosus[num] == True:
            answer += 1
    
    
    
    return answer