from itertools import accumulate

def time_to_minute(time):
    h,m = time.split(':')
    return int(h)*60 + int(m)

def solution(book_time):
    graph = [0]*(60*24+10)
    for book_start, book_end in book_time:
        start_t = time_to_minute(book_start)
        end_t = time_to_minute(book_end)
        graph[start_t]+= 1
        graph[end_t+10]-=1
    return max(accumulate(graph))