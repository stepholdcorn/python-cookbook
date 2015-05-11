from datetime import datetime

text = '2015-05-11'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)

z = datetime.now()
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)