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
