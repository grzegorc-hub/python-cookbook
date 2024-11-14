# SPLITING
# ------------------------

# split() - for simple cases
line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re

r = re.split(r'[\s,;]\s*', line)
print(r)

# MATCHING TEXT AT START AND END
# ------------------------

url = 'http://www.python.org'
r = url.startswith('http:')
print(r)
r = url.endswith('.com')
print(r)

import os

filenames = os.listdir('.')
r = [name for name in filenames if name.startswith(('2_1', '2_2', '2_100'))]
print(r)

print('test')
