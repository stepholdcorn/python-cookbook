from operator import itemgetter
from itertools import groupby

rows = [
  {'address': '5412 N Clark', 'date': '07/01/2012'},
  {'address': '5421 N Granville', 'date': '07/04/2012'},
  {'address': '2412 W Addison', 'date': '07/04/2012'},
  {'address': '4412 N Broadway', 'date': '07/01/2012'},
  {'address': '5112 E 58th', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
  print(date)
  for i in items:
    print('', i)