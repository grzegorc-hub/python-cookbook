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
