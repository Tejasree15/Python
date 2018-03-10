#prime or not
num=int(input('Enter a number: '))
for i in range(1,num):
    if num%i==0:
        print ('The number {} is NOT a prime number'.format(num))
        break
    else:
        print ('Number {} is a Prime number'.format(num))
