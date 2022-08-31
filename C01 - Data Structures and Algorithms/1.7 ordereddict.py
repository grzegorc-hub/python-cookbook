from collections import OrderedDict
import json

d = OrderedDict()
d['aaa'] = 2
d['zzz'] = 4
d['ccc'] = 1
d['bbb'] = 7

print(d)

r = json.dumps(d)
print(r)
