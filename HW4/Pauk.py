import random

n = int(input('Vvedite razmer setki: '))

a = [['#' for i in range(n)] for j in range(n)]

def funk():
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()

rand_px = random.randint(0, n-1)
rand_py = random.randint(0, n-1)
a[rand_py][rand_px] = 'P'

while True:
        rand_mx = random.randint(0, n - 1)
        rand_my = random.randint(0, n - 1)
        if a[rand_my][rand_mx] == 'P':
            lamsad = 0
        else:
            a[rand_my][rand_mx] = 'M'
            break

if rand_mx > rand_px and rand_my > rand_py: 
    for i in range(rand_px + 1, rand_mx):
        a[rand_py][i] = 'H'
    for j in range(rand_py, rand_my):
        a[j][rand_mx] = 'H'
    funk()

elif rand_mx < rand_px and rand_my > rand_py: 
    for i in range(rand_mx, rand_px):
        a[rand_py][i] = 'H'
    for j in range(rand_py, rand_my):
        a[j][rand_mx] = 'H'
    funk()

elif rand_mx < rand_px and rand_my < rand_py: 
    for i in range(rand_mx + 1, rand_px):
        a[rand_my][i] = 'H'
    for j in range(rand_my, rand_py):
        a[j][rand_px] = 'H'
    funk()

elif rand_mx > rand_px and rand_my < rand_py: 
    for i in range(rand_px, rand_mx):
        a[rand_my][i] = 'H'
    for j in range(rand_my, rand_py):
        a[j][rand_px] = 'H'
    funk()

elif rand_mx == rand_px and rand_my < rand_py: 
    for j in range(rand_my + 1, rand_py):
        a[j][rand_px] = 'H'
    funk()

elif rand_mx == rand_px and rand_my > rand_py: 
    for j in range(rand_py + 1, rand_my):
        a[j][rand_px] = 'H'
    funk()

elif rand_mx > rand_px and rand_my == rand_py: 
    for i in range(rand_px + 1, rand_mx):
        a[rand_my][i] = 'H'
    funk()

elif rand_mx < rand_px and rand_my == rand_py: 
    for i in range(rand_mx + 1, rand_px):
        a[rand_my][i] = 'H'
    funk()
