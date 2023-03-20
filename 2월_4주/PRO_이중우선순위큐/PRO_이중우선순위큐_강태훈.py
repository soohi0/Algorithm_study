import heapq


class double_priority_queue:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.datalen = 0

    def initialize(self):
        if self.datalen == 0:
            self.maxheap = []
            self.minheap = []

    def push(self, item):
        heapq.heappush(self.maxheap, -item)
        heapq.heappush(self.minheap, item)
        self.datalen += 1
        self.initialize()

    def popmax(self):
        max_item = None
        if self.datalen > 0:
            max_item = heapq.heappop(self.maxheap)
            self.datalen -= 1
            self.initialize()
            return -max_item

    def popmin(self):
        min_item = None
        if self.datalen > 0:
            min_item = heapq.heappop(self.minheap)
            self.datalen -= 1
            self.initialize()
            return min_item


def solution(operations):
    answer = []
    myheap = double_priority_queue()
    for op in operations:
        cmd, val = op.split()
        val = int(val)
        if cmd == "I":
            myheap.push(val)
        if cmd == "D":
            if val == 1:
                myheap.popmax()
            else:
                myheap.popmin()
    if myheap.datalen == 0:
        return [0, 0]
    elif myheap.datalen == 1:
        val = myheap.popmin()
        return [val, val]
    return [myheap.popmax(), myheap.popmin()]