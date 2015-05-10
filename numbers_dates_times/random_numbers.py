import random

values = [1, 2, 3, 4, 5, 6]
shuffled = random.shuffle(values)

print(random.choice(values))
print(random.sample(values, 2))
print(shuffled)
print(random.randint(1, 4))
print(random.random())