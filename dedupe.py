def dedupe(items, key=None):
  seen = set()
  for item in items:
    val = item if key is None else key(item)
    if val not in seen:
      yield item
      seen.add(val)

a = [1, 2, 1, 10, 5, 5, 1, 3]
b = [ {'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

print(list(dedupe(a)))
print(list(dedupe(b, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(b, key=lambda d: (d['x']))))