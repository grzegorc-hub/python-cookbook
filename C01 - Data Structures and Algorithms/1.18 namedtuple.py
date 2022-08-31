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
