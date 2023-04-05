def solution(fees,records):
    cars = {}
    for r in records:
        time, number, status = r.split()
        cars[number] = cars.get(number,[]) + [time]
    prev = 0
    times = []
    for k, v in cars.items():
        total_time = 0
        for curv in v:
            if prev == 0:
                prev = curv
            else:
                prev_h, prev_m = map(int,prev.split(':'))
                curv_h, curv_m = map(int,curv.split(':'))
                t_diff = (curv_h-prev_h) * 60 + (curv_m-prev_m)
                total_time += t_diff if t_diff > 0 else 0
                prev = 0
        if prev != 0:
            prev_h, prev_m = map(int,prev.split(':'))
            curv_h, curv_m = map(int,"23:59".split(':'))
            t_diff = (curv_h-prev_h) * 60 + (curv_m-prev_m)
            total_time += t_diff if t_diff > 0 else 0
            prev = 0
        times.append((k,total_time))
    times.sort()
    answer = []
    for car_no, time in times:
        add_time = max(0,(time - fees[0])/fees[2] if not (time-fees[0])%fees[2] else (time - fees[0])//fees[2]+1)
        fee = fees[1]+ int(add_time)*fees[3]
        answer.append(fee)
    return answer