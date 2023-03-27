import sys
input = sys.stdin.readline

from collections import defaultdict

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def get_near(n, loc):
    for i in range(4):
        nx, ny = loc[0]+dx[i], loc[1]+dy[i]
        if 0<=nx<n and 0<=ny<n:
            yield nx, ny

def solve(n, park):
    setted, prefer_dict = {}, {}
    graph = {(i,j):-1 for i in range(n) for j in range(n)}
    visited = {(i,j):4 for i in range(n) for j in range(n)}
    for i in range(n):
        visited[(0,i)] -= 1
        visited[(i,0)] -= 1
        visited[(n-1,i)] -= 1
        visited[(i,n-1)] -= 1

    def insert(student_info, location):
        student_idx, prefer_list = student_info[0], student_info[1:]
        setted[student_idx] = location
        prefer_dict[student_idx] = set(prefer_list)
        graph[location] = student_idx
        for near_coordinate in get_near(n, location):
            visited[near_coordinate] -= 1
        
    for student in park:
        student_idx, prefer_list = student[0], set(student[1:])
        possibility = defaultdict(int)
        for prefer in (prefer_list & set(setted.keys())):
            for nloc in get_near(n, setted[prefer]):
                possibility[nloc] += 1
        for location, _ in sorted(possibility.items(), key=lambda x:(-x[1],x[0])):
            if graph[location] == -1:
                insert(student, location)
                break
        else:
            for location, _ in sorted(visited.items(), key=lambda x:(-x[1],x[0])):
                if graph[location] == -1:
                    insert(student, location)
                    break
    answer = 0
    for student_idx, loc in setted.items():
        cnt = -1 + sum([(graph[nloc] in prefer_dict[student_idx]) for nloc in get_near(n, loc)])
        answer += int(10**cnt)
    return answer

if __name__ == "__main__":
    n = int(input())
    print(solve(n, [list(map(int, input().split())) for _ in range(n**2)]))
    