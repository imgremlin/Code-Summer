print('How much do you have to sleep(min):')
a = int(input())
print('How much do you have to sleep(max):')
b = int(input())
print('How much do you sleep:')
h = int(input())

if h<a:
    print('You sleep less than you need')
elif h>b:
    print('You sleep more than you need')
else:
    print('You sleep enough')