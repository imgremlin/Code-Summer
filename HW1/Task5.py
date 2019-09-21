print('Enter the distance between houses (m):')
distance = int(input())
print('Enter the number of houses:')
number = int(input())
print('Enter the price of cable ($/m):')
price = int(input())

total_number = 0
for i in range(1, number):
    total_number += i

total_price = distance*price*total_number
print(total_price)
