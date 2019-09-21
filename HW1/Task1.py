print('How much time do you want to sleep(minutes):')
x = int(input())
print('When do you go to bed(hours):')
h = int(input())
print('When do you go to bed(minutes):')
m = int(input())

tm = m+x
h1 = str((tm//60 + h)%24)
m1 = str(tm%60)
print('Alarm will ring at ' + h1 + ':' + m1)
