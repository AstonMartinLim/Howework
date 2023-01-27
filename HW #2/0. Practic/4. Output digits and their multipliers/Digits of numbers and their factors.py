# Ввести число, вивести його розряди та їх множники.

num = int(input('Type an integer between 1 and 10 000: '))

x=num//1000
y=(num//100)%10
z=(num//10)%10
o=(num//1)%10

if num > 1000:
    print (x,'* 1000\n', y,'* 100\n', z, '* 10\n', o, '* 1')
if (num < 1000) and (num >= 100):
    print (y, '* 100\n', z, '* 10\n', o, '* 1\n')
if (num < 100) and (num >= 10):
    print (z, '* 10\n', o, '* 1\n')
if (num < 10) and (num > 0):
    print (o, '* 1\n')
