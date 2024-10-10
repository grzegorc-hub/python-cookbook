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


# 1.8 CALC WITH DICTONARIES
# --------------------------
# In order to perform useful calculations on the dictionary contents, it is often useful to
# invert the keys and values of the dictionary using zip().

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# zip creates iterator that can be only consumed once
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
#print(max(prices_and_names))  # ValueError: max() arg is an empty sequence


# 1.9 FINDING COMMONALITIES IN 2 DICTs
# -------------------------------------

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print( a.keys() & b.keys() )
print( a.keys() - b.keys() )
print( a.items() & b.items() )

c = { k: a[k] for k in a.keys() - {'z'} }
print(c)


# 1.10 REMOVING DUPLICATES WHILE KEEPING ORDER
# ---------------------------------------------

def del_duplicates(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(del_duplicates(a)))

b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(del_duplicates(b, key=lambda d: d['x'])))

c = [1, 2, 3, 7, 4, 5, 1, 2, 3, 10]
print(set(c))  # doesn't preserve order


# NAMING A SLICE
# --------------------------

######   0123456789012345678901234567890123456789012345678901234567890'
record = '....................100         .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)

SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

print(PRICE.start, PRICE.stop, PRICE.step)


# MOST FREQUENT ITEMS IN SEQ
# --------------------------------

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
words_count = Counter(words)
print(words_count.most_common(3))


# 1.13 SORTING LIST OF DICTS BY COMMON KEY
# ---------------------------------------------

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
rows_by_lname = sorted(rows, key=itemgetter('lname'))
print(rows_by_lname)

rows_by_lname2 = sorted(rows, key=lambda r: r['lname'])
print(rows_by_lname2)


# 1.14 SORTING OBJECTS WITHOUT NATIVE CMP
# ---------------------------------------------

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User({self.user_id})'


users = [User(1), User(5), User(3)]
print(users)

users2 = sorted(users, key=lambda u: u.user_id)
print(users2)

from operator import attrgetter
users3 = sorted(users, key=attrgetter('user_id'))
print(users3)


# 1.15 GROUPING RECORDS TOGETHER BASED ON A FIELD
# ------------------------------------------------

"""
The groupby() function works by scanning a sequence and finding sequential “runs”
of identical values (or values returned by the given key function). On each iteration, it
returns the value along with an iterator that produces all of the items in a group with
the same value.
"""

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(i)


# 1.16 FILTERING SEQUENCE ELEMENTS
# --------------------------------

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

pos = (n for n in mylist if n > 0)  # if the result is large, then better to use generator
print(pos)
for x in pos:
    print(x)


values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

f = list(filter(is_int, values))  # for more advanced filtering criteria, use separate function and filter()
print(f)


# 1.17 EXTRACTING SUBSET OF DICT
# -------------------------------

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {k:v for k,v in prices.items() if v > 200}
print(p1)


# 1.18 NAMED TUPLES
# ------------------

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('bob@example.com', '2019-01-01')

print(sub)
print(sub.addr)
a, b = sub
print(b)


# ordinary tuple
def compute_cost1(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# 1.19 TRANSFORMING AND REDUCING DATA AT THE SAME TIME
# -----------------------------------------------------

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

import os

files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('there is python')
else:
    print('no python')

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20}]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)


# 1.20 COMBINING MULTIPLE MAPPINGS INTO A SINGLE MAPPING
# ------------------------------------------------------
# You have multiple dictionaries or mappings that you want to logically combine into a
# single mapping to perform certain operations, such as looking up values or checking
# for the existence of keys.

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
