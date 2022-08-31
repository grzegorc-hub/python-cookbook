a, b, c = (1, 2, [3, 4])
print(a, b, c)

a, _, _, b, c = 'Hello'
print(a, b, c)

*a, b = [1, 2, 3, 4]
print(a, b)

*_, b, c = 'Hello'
print(b, c)
