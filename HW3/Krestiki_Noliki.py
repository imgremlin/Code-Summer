import random
import os

print('Vvedite dve tsifry: pervaya - koordinata po x, vtoraya koordinata po y')
a = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]


def funk():
    for i in range(3):
        for j in range(3):
            print(a[i][j], end=' ')
        print()
    print()


def your_turn():
    while True:
        x = int(input('Vvedite x: '))
        while True:
            if x >= 1 and x <= 3:
                break
            else:
                x = int(input('Vvedite x: '))
        y = int(input('Vvedite y: '))
        while True:
            if y >= 1 and y <= 3:
                break
            else:
                y = int(input('Vvedite y: '))
        if a[y  - 1][x - 1] == 'X' or a[y - 1][x - 1] == 'O':
            print('Error! Input another value')
        else:
            a[y - 1][x - 1] = 'X'
            break         
    funk()
    check()
    

def rand_turn():
    print('Computer s turn')
    while True:
        rand_x = random.randint(1,3)
        rand_y = random.randint(1,3)
        if a[rand_y - 1][rand_x - 1] == 'X' or a[rand_y - 1][rand_x - 1] == 'O':
            print('')
        else:
            a[rand_y - 1][rand_x - 1] = 'O'
            break
    funk()
    check()


def check():
    global num_check
    for i in range(0, 2):
        if a[i][0] == a[i][1] == a[i][2] == 'X':
            print('you win')
            que()
        elif a[i][0] == a[i][1] == a[i][2] == 'O':
            print('you lost')
            que()
    for j in range(0, 2):
        if a[0][j] == a[1][j] == a[2][j] == 'X':
            print('you win')
            que()
        elif a[0][j] == a[1][j] == a[2][j] == 'O':
            print('you lost')
            que()

    if a[0][0] == a[1][1] == a[2][2] == 'X' or a[2][0] == a[1][1] == a[0][2] == 'X':
        print('you win')
        que()
    elif a[0][0] == a[1][1] == a[2][2] == 'O' or a[2][0] == a[1][1] == a[0][2] == 'O':
        print('you lose')
        que()


def draw():
    global num_check
    dr = 0
    for i in range(0, 3):
        for j in range(0,3):
            if a[i][j] == '#':
                dr = 0
            else:
                dr += 1
    if dr > 8:
         num_check = 1
         print('draw')
         que()

def main():
    global a
    a = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
    funk()
    while num_check == 0:
                your_turn()
                if num_check == 1:
                    break
                draw()
                if num_check == 1:
                    break
                rand_turn()
                if num_check == 1:
                    break
                draw()
                if num_check == 1:
                    break


def que():
    global num_check
    num_check = 0
    ask = input('Hotite nachat igru?(yes/no): ')
    while num_check == 0:
        if ask == 'yes':
            num_check = 0
            os.system('cls')
            main()
        elif ask == 'no':
            num_check = 1
            return num_check
            print('See u next time')
        else:
                ask = input('Hotite nachat igru?(yes/no): ')

que()    
