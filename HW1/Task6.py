a = int(input())
a1 = str(a)
last_n = a%10
last_11 = a%100
if 14>=last_11>=11 or 9>=last_n>=5 or last_n==0:
    print(a1 + ' программистов')
elif last_n==1:
    print(a1 + ' программист')
elif 4>=last_n>=2:
    print(a1 + ' программиста')
