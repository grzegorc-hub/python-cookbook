######   0123456789012345678901234567890123456789012345678901234567890'
record = '....................100         .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)

SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

print(PRICE.start, PRICE.stop, PRICE.step)
