from math import ceil

total_fee = lambda fees, t : fees[1] + ceil(max(0, t - fees[0]) / fees[2]) * fees[3]
time_zfill = lambda timelist : timelist+[[23,59]] if len(timelist)%2 else timelist
time_diff = lambda t1, t2 : 60*(t1[0]-t2[0]) + t1[1]-t2[1]

def solution(fees, records):
    user_inform = {}
    answer = []
    for record in records:
        time, car, ty = record.split()
        user_inform[car] = user_inform.get(car, []) + [list(map(int,time.split(":")))]
    for carnum, timelist in sorted(user_inform.items()):
        timelist = time_zfill(timelist)
        use_time = sum(time_diff(t1,t2) for t2, t1 in zip(timelist[::2], timelist[1::2]))
        answer.append(total_fee(fees, use_time))
    return answer
