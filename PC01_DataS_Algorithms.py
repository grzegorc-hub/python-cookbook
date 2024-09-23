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

# "double-ended queue"
# optimized for adding and removing elements from both ends
# Fast O(1) append and pop operations from both ends (append, appendleft, pop, popleft
from collections import deque

def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history) #fixed-sized queue. When new items are added and the queue is full, the oldest item is automatically removed 
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

#         1
#       /   \
#     3       6
#    / \     / \
#   5   9   8   7
# heap[0] is always the smallest item
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

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(type(heap)) # list


# 1.5 PRIORITY QUEUE
#--------------------

import heapq

class PrioQueue:
    def __init__(self):
        self._q = []
        self._i = 0

    def push(self, item, prio):
        heapq.heappush(self._q, (-prio, self._i, item)) # prio & index added so that it can compare items
        self._i += 1

    def pop(self):
        return heapq.heappop(self._q)


q = PrioQueue()
q.push('aaa', 1)
q.push('bbb', 1)
q.push('ccc', 4)
q.push('ddd', 0)
print(q._q)

r = q.pop()
print(r)


# 1.6 DEFAULT DICT
# ---------------------
# You want to make a dictionary that maps keys to more than one value (a so-called “multidict”).

from collections import defaultdict

d = {
    'a': [1, 2, 3],
    'b': [7, 6]
}

e = defaultdict(list) # feature of defaultdict is that it automatically initializes the first value so you can simply focus on adding items
e['a'].append(1)
e['a'].append(2)
e['a'].append(3)
e['b'].append(7)
e['b'].append(6)

print(d)
print(e)

# 1.7 ORDERED DICT
# --------------------

from collections import OrderedDict
import json

d = OrderedDict()
d['aaa'] = 2
d['zzz'] = 4
d['ccc'] = 1
d['bbb'] = 7

print(d)
for key in d:
    print(key, d[key])

r = json.dumps(d)
print(r)
