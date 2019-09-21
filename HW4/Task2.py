import random

x = random.randint(0, 10)
for i in range(3):
    a = int(input())
    if a == x:
        print('ugadal')
        break
    elif a > x:
        print('nado menshe')
    elif a < x:
        print('nado bolshe')