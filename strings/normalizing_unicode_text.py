import unicodedata

s1 = 'Jalape\u00f1o'
s2 = 'Jalapen\u0303o'

print(s1 == s2)

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)

print(t1 == t2)