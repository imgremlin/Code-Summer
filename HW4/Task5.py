import random

a = [[random.randint(0, 16) for i in range(4)] for j in range(4)]
print(a)
for k in range(4):
    for l in range(4):
        if a[k][l] % 2 == 0:
            a[k][l] = -1

print(a)