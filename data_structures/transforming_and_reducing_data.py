import os

files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
  print('There be Python!')
else:
  print('No Python here')

nums = [1, 2, 3, 4, 5]
s = sum(x ** 2 for x in nums)
print(s)

stock = ('ACME', 5, 123.45)
t = ','.join(str(x) for x in stock)
print(t)