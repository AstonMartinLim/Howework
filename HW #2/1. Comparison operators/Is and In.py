# Оператор is перевіряє, чи є обидва операнди одним і тим самим об'єктом
# у пам'яті, тоді як просте порівняння на рівність == перевіряє тільки
# на відповідність вмісту двох операндів, але не перевіряє, чи є вони тим
# самим об'єктом

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2) # True
print(l1 is l2) # False
print(l1[0] is l2[0]) # True
print(l1[0] == l2[0]) # True
print(l1 is not l2) # True
print('\n\n')

# Оператор in перевіряє, чи включає операнд справа в той операнд, що зліва
print(3 in l1) # True
print(4 in l1) # False
print(5 not in l1) # True
# print(3 in l1[2]) TypeError: argument of type 'int' is not iterable
print(3 == l1[2]) # True
print(6 == sum(l1))# True
print(sum(l1) != sum(l2)) # False
