import random
print('Vas privetstvuet klassicheskaya igra "kamen, nojnitsi, bumaga"')
print('Pravila igry prosty: vy xodite odnim iz zadanyx obektov(tolko kamen, nojnitsi, bumaga, ), potom bot delaet xod')
print('Pust pobedit silnejshij!')
print()

def funk():
    print('Vash xod:', end=' ')
    your_turn = input()
    a = 0
    base = str()
    while a==0:
        if your_turn == 'kamen' or your_turn == 'nojnitsi' or your_turn == 'bumaga':
            a = 1
        else:
            print('Nu budte zhe lyudmi! Normalno poxodite:', end=' ')
            your_turn = input()

    base = ['kamen', 'nojnitsi', 'bumaga']
    random.shuffle(base)
    random_number = random.choice(base)
    print('Hod sopernika:', end=' ')
    print(random_number)

    if your_turn == 'kamen':
        if random_number == 'kamen':
            print('draw')
        elif random_number == 'nojnitsi':
            print('ez win')
        else:
            print('sry lose')

    elif your_turn == 'nojnitsi':
        if random_number == 'kamen':
            print('sry lose')
        elif random_number == 'nojnitsi':
            print('draw')
        else:
            print('ez win')

    elif your_turn == 'bumaga':
        if random_number == 'kamen':
            print('ez win')
        elif random_number == 'nojnitsi':
            print('sry lose')
        else:
            print('draw')
    print()

b = 0
print(funk())

while b==0:
    print('Eshe odnu katku?(yes/no)')
    print('Your answer:', end=' ')
    your_answer = input()
    print()
    if your_answer == 'yes':
        print(funk())
    elif your_answer == 'no':
        print('Bye')
        b = 1