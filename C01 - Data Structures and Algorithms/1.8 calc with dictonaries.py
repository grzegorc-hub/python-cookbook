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
print(max(prices_and_names))  # ValueError: max() arg is an empty sequence
