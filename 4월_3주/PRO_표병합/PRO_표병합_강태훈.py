parent = [i for i in range(2500)]
value = ["EMPTY" for _ in range(2500)]

def find(x):
    if x != parent[x]:
        ploc = parent[x]
        parent[x] = find(ploc)
    return parent[x]

def union(x1, x2):
    x1, x2 = find(x1), find(x2)
    if x1 == x2:
        return
    parent[x2] = x1
    val = value[x1] if value[x1]!="EMPTY" else value[x2]
    update_1(x1, val)

def update_1(x, val):
    head = find(x)
    for i in range(2500):
        if find(i) == head:
            value[i] = val

def update_2(v1, v2):
    for i in range(2500):
        loc = find(i)
        if value[loc] == v1:
            value[loc] = v2

def unmerge(x):
    head = find(x)
    val = value[head]
    for i in range(2500):
        if find(i) == head:
            parent[i] = i
            value[i] = "EMPTY" if i != x else value[i]

getloc = lambda x,y : 50*(int(x)-1) + (int(y)-1)

def solution(commands):
    answer = []
    for command in commands:
        cmd = command.split()
        cmd_len = len(cmd)
        if cmd[0] == "UPDATE":
            if cmd_len == 3:
                update_2(*cmd[1:])
            elif cmd_len == 4:
                r, c, v = cmd[1:]
                update_1(getloc(r,c), v)

        elif cmd[0] == "MERGE":
            r1, c1, r2, c2 = cmd[1:]
            loc1, loc2 = getloc(r1,c1), getloc(r2,c2)
            union(loc1, loc2)

        elif cmd[0] == "UNMERGE":
            loc = getloc(*cmd[1:])
            unmerge(loc)

        elif cmd[0] == "PRINT":
            loc = getloc(*cmd[1:])
            answer.append(value[find(loc)])

    return answer