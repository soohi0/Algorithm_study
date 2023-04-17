import math
from collections import defaultdict
def fee_cal(till, fees):
    fee = 0
    if till >= fees[0]:
        fee += fees[1]
        till -= fees[0]
        fee +=math.ceil(till / fees[2]) * fees[3]
    else:
        fee = fees[1]
    return fee
def time_check(in_time, out_time):
    result = 0
    i_hour, i_minute = map(int, in_time.split(':'))
    o_hour, o_minute = map(int, out_time.split(':'))
    # i_hour, i_minute, o_hour, o_minute = int(i_hour), int(i_minute), int(o_hour), int(o_minute) 
    result += (o_hour - i_hour) * 60
    if o_minute - i_minute >= 0:
        result += (o_minute - i_minute)
    else:
        result -= 60
        result += (60+(o_minute - i_minute))
    return result
    
def solution(fees, records):
    answer = []
    fee_checker = defaultdict(list)
    for record in records:
        time, number, check = record.split(' ')
        if number not in fee_checker and check == 'IN':
            print(time, number, check)
            fee_checker[number] = [time, check, 0]
        elif number in fee_checker and check == 'IN': 
            fee_checker[number][0] = time
            fee_checker[number][1] = check
        elif check == 'OUT':
            #시간계산
            fee_checker[number][2] += time_check(fee_checker[number][0], time)
            fee_checker[number][1] = check
            fee_checker[number][0] = time
        # print(fee_checker)
    keys = sorted(fee_checker)
    # print(fee_checker)
    for key in keys:
        time, check, till = fee_checker[key]
        if check == 'IN':
            till += time_check(time, '23:59')
        fee = fee_cal(till, fees)
        answer.append(fee)
        
    return answer