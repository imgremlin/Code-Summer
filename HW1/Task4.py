print('Enter the number:')
a = int(input())

if (a//100000+(a//10000)%10+(a//1000)%10)==((a//100)%10+(a//10)%10+a%10):
    print('Lucky')
else:
    print('Usual')
