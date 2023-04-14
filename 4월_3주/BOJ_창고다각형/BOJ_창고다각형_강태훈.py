import sys
input = sys.stdin.readline

def make_stack(pipes):
    stack = []
    for x, y in pipes:
        if not stack or stack[-1][1] <= y:
            stack.append([x,y])
        else:
            maxh = 0
            for i in range(len(stack)):
                maxh = max(maxh, stack[i][1])
                stack[i][1] = maxh
            stack.append([x,maxh])
    return stack

def calc_area(stack, px):
    area = 0
    while stack:
        x, y = stack.pop()
        area += abs(px-x)*y
        px = x
    return area

def solve(n, stuff):
    stuff.sort()
    max_idx, answer = 0, 0
    for i in range(n):
        if stuff[i][1] > answer:
            max_idx, answer = i, stuff[i][1]
    l, r = map(make_stack, (stuff[:max_idx+1], stuff[::-1][:n-max_idx]))
    
    px, _ = stuff[max_idx]
    answer += (calc_area(l,px) + calc_area(r, px))
    return answer

if __name__ == "__main__":
    n = int(input())
    stuff = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, stuff))
