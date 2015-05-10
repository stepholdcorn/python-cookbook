from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')

print(a + b)
print((a + b) == Decimal('6.3'))