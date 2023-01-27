# Написати 2 функції. Перша функція прийматиме рядок та приводитиме його
# до нижнього регістру. Друга функція прийматиме рядок та приводитиме його
# до верхнього регістру.

# Головна програма має застосовувати обидві функції до списку рядків
# за допомогою map, для кожного з рядків, та друкувати результат.

my_str1 = '''Python — высокоуровневый язык программирования общего назначения
            с динамической строгой типизацией и автоматическим управлением
            памятью, ориентированный на повышение производительности
            разработчика, читаемости кода и его качества, а также на
            обеспечение переносимости написанных на нём программ.'''

my_str = my_str1.split() # получаю список строк для дальнейшей обработки

# возведение списка строк в верхний регистр
def hight_reg (my_str):
    return my_str.upper()


# возведение списка строк в нижний регистр
def low_reg (my_str):
    return my_str.lower()


str_hight = list(map(hight_reg, my_str))
print(' '.join(str_hight)) # склеивание списка для красивого отображения               
    
str_low = list(map(low_reg, my_str))
print(' '.join(str_low)) # склеивание списка для красивого отображения
