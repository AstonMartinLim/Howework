# Кожен пише суму списку за допомогою for та while

# for
numbers = [3, 7, 9, 2, 8, 4]
sum_of_numbers = 0

for elem in numbers:
    sum_of_numbers += elem
print(sum_of_numbers) # 33


# while
numbers_1 = [3, 7, 9, 2, 8, 4, 6, 1, 5]
sum_of_numbers_1 = 0
index = 0

while index < len(numbers_1):
    sum_of_numbers_1 += numbers_1[index]
    index += 1
print(sum_of_numbers_1) # 45

# ПРИМЕЧАНИЕ: 
# Если в условии цикла записать len(numbers_1)-1, то НЕ БУДЕТ суммироваться
# последний элемент списка. В таком случае нужно поменять знак сравнения
# в условии. Запись должна быть следующей:
# while index <= len(numbers_1)-1:
# При такой записи цикл дойдет до последнего элемента
