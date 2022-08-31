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
