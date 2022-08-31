from collections import defaultdict

d = {
    'a': [1, 2, 3],
    'b': [7, 6]
}

e = defaultdict(list)
e['a'].append(1)
e['a'].append(2)
e['a'].append(3)
e['b'].append(7)
e['b'].append(6)

print(d)
print(e)