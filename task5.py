
rev = int(input('Enter your revenue - '))
cost = int(input('Enter summ of your costs - '))
emp = int(input('Enter number of employees - '))

set1 = (((rev / cost) * 100) - 100)//1
set2 = rev - cost

if rev > cost:
    print('You are have a profit')
    print('Your rent is', set1 , '%')
    prf_em = set2 // emp
    print('Profit is ' , prf_em, '$' , 'on each staff member')
else:
    print('You are have a loss')







