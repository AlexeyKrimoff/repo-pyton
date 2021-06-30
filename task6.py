
a = int(input('Enter your today distance -km-  '))
b = int(input('Enter your target distance -km-  '))

count = 0
while a < b:
    a = a * 1.1
    count += 1
    if a > b:
        break
print('You achive your goal, after ' , count , 'days')