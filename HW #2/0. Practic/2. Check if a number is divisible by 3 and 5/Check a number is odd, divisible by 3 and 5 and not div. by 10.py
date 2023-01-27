# Check whether a number is odd, divisible by three and five
# at the same time, but not divisible by 10.

num = int(input('Type an integer: '))

if num%2 and not num%3 and not num%5 and num%10:
    print(num)
    
