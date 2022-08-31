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
