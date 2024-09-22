# UNPACKING
# ------------------------

a, b, c = (1, 2, [3, 4])
print(a, b, c)

a, _, _, b, c = 'Hello'
print(a, b, c)

*a, b = [1, 2, 3, 4]
print(a, b)

*_, b, c = 'Hello'
print(b, c)

# KEEP LAST N ELEMENTS
#-------------------------

from collections import deque

def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)

if __name__ == '__main__':
    with open('file1.txt') as f:
        for line, prev_lines in search(f, 'python', 3):
            print(prev_lines)
            print(line)
            print('-'*15)

# FINDING N LARGEST OR SMALLEST ITEMS
#-------------------------

import heapq

N = [34, 32, 324, 234, 24, 546, 456, 456, 435, 43, 43, 345, 435, 6, 643, 4455]
L = heapq.nlargest(3, N)
S = heapq.nsmallest(3, N)
print(L)
print(S)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheapest = heapq.nsmallest(2, portfolio, lambda s: s['price'])  # best performance
print(cheapest)

expensive = sorted(portfolio, key=lambda s: s['price'], reverse=True)[:2]  # ok if N is the same size of collection
print(expensive)

i = max(portfolio, key=lambda s: s['price'])
print(i)

# PRIORITY QUEUE
#--------------------

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
