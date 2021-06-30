
enter = int(input('Enter the time in seconds - '))

hours = enter // 360
if hours < 1:
    hours = 0
else:
    hours = hours

min1 = enter - hours * 360
min = min1// 60
if min < 1:
    min = 00
else:
    min = min

sec1 = enter % 360
sec = sec1 - 60

print (hours,':', min,':', sec)
