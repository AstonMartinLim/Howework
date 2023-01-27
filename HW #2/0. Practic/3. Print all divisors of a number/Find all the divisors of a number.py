# Ввести число, вивести усі його дільники.

num = int(input('Type an integer: '))

num1 = 1

# Варіант 1
while num1 <= num:
    if num%num1==0:
        print(num1, end=' ')
    num1 +=1

# Варіант 2 (списаний з Інтернет)       
while num1 <= num//2:
    if num%num1==0:
        print(num1, end=' ')
    num1 +=1
print(num)

# Варіант 3
for i in range (1, num+1, 1):
    if num%i == 0:
        print (i, end=' ')
