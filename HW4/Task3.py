import random
a = [random.randint(0, 10) for i in range(10)]
print(a)
s = 0

for l in range(10):
    s += a[l]
print(s)