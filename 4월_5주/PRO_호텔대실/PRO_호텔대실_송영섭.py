def convert_time(time: str) -> int:
    return int(time[:2]) * 60 + int(time[3:])

def solution(book_time: list) -> int:
    book_time.sort()
    room_list = [0] * 1001
    max_pos = -1
    for book in book_time:
        start, end = book
        start, end = convert_time(start), convert_time(end) + 10 # 청소시간 더함
        
        for pos in range(1, 1001):
            if pos > max_pos:
                max_pos = pos

            if room_list[pos] <= start:
                room_list[pos] = end
                break
    
    return max_pos