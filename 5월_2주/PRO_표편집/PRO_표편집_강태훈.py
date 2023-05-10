# 풀이1. Just simulation with bisect : 효율성 일부 통과 못함
from bisect import insort_left, bisect_left
def solution(n, k, cmd):
    cell = [i for i in range(n)]
    cursor = k
    history = []
    for query in cmd:
        if query == "C":
            history.append(cursor)
            index = bisect_left(cell, cursor)
            del cell[index]
            if not cell:
                continue
            if index == len(cell):
                cursor = cell[-1]
            else:
                cursor = cell[index]
        elif query == "Z":
            recovery = history.pop()
            insort_left(cell, recovery)
        else:
            direction, value = query.split()
            index = bisect_left(cell, cursor)
            if direction == "D":
                cursor = cell[min(index+int(value), len(cell)-1)]
            else:
                cursor = cell[max(index-int(value), 0)]
    answer = ["X"]*n
    for index in cell:
        answer[index] = "O"
    return "".join(answer)

# 풀이2. dictionary 활용한 doubly linked list 
class Cell:
    def __init__(self, size, cursor):
        self.cell = {i:[i-1,i+1] for i in range(size)}
        self.cell[0][0] = self.cell[size-1][1] = None
        self.cursor = cursor
        self.state = ["O"]*size
        self.history = []
        
    def delete(self):
        self.state[self.cursor] = "X"
        pnode, nnode = self.cell[self.cursor]
        self.history.append([self.cursor, *self.cell[self.cursor]])
        self.cursor = self.cell[self.cursor][(0 if nnode==None else 1)]
        if pnode == None:
            self.cell[nnode][0] = None
        elif nnode == None:
            self.cell[pnode][1] = None
        else:
            self.cell[pnode][1] = nnode
            self.cell[nnode][0] = pnode
            
    def undo(self):
        rec, pnode, nnode = self.history.pop()
        self.state[rec] = "O"
        if pnode == None:
            self.cell[nnode][0] = rec
        elif nnode == None:
            self.cell[pnode][1] = rec
        else:
            self.cell[nnode][0] = self.cell[pnode][1] = rec
        
    def move_cursor(self, direction):
        self.cursor = self.cell[self.cursor][direction]

def solution(n, k, cmd):
    cell = Cell(n, k)
    for query in cmd:
        if query=="Z":
            cell.undo()
        elif query=="C":
            cell.delete()
        else:
            t, val = query.split()
            direction = (1 if t=="D" else 0)
            for _ in range(int(val)):
                cell.move_cursor(direction)
    return "".join(cell.state)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))