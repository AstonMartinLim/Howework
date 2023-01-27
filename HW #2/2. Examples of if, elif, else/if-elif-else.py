# Прогр. перевіряє чи знаходиться введене число у діапазоні 0-10, 11-100,
# 101-1000, 1001 - 10 000, більше ніж 10 000
#

num = int (input('Type an integer: '))

if num <= 10:
    print("Your`s number beetwen 0 and 10")
elif ((num > 10) and (num <= 100)):
    print("Your`s number beetwen 10 and 100")
elif ((num > 100) and (num <= 1000)):
    print("Your`s number beetwen 101 and 1 000")
elif ((num > 1000) and (num <= 10000)):
    print("Your`s number beetwen 1001 and 10 000")
else:
    print ("Your`s number more then 10 000")
