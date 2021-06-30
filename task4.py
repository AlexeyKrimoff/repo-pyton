
num = int(input('Enter integer number - '))
max = num%10
num = num//10
while num > 0:
    if num%10 > max:
        max = num%10
    num = num//10
print('maximum number - ', max)