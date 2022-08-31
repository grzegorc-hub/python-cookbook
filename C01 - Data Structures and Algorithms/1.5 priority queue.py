import heapq


class PrioQueue:
    def __init__(self):
        self._q = []
        self._i = 0

    def push(self, item, prio):
        heapq.heappush(self._q, (-prio, self._i, item))
        self._i += 1

    def pop(self):
        return heapq.heappop(self._q)


q = PrioQueue()
q.push('aaa', 1)
q.push('bbb', 1)
q.push('ccc', 4)
q.push('ddd', 0)

r = q.pop()
print(r)
