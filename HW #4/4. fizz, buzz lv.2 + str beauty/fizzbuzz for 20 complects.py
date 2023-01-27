# Задача прикрасити fizz-buzz.

# РЕЗЮМЕ:
# 1) вместо цикла while использовал цикл for, это уменьшило код на 2 строчки
# 2) для вывода кода на монитор использовал разные методы форматирования str

# ввод 3-х чисел с клавиатуры
fizz, buzz, fb = map(int, input('Type three integer separated by comma: ').split(','))

# Использование метода format()
s = "You typed: fizz = {}, buzz = {}, fb = {}"
print('\n', s.format(fizz, buzz, fb), '\n')

# открывается текстовый файл
r = open('numbers.txt', 'r')

for i in range(20):
    # считывание по 1-й строке
    b = r.readline()
    # т.к. ф-я read считывает данные в формате str, их нужно преобразовать
    # в int и для удобства итерации передать в список
    list_of_str = b.split(',')
    list_of_int = list(map(int, list_of_str))
    # цикл для сравнения fizz, buzz и fb с цифрами в текстовом файле  
    for i in list_of_int:
        if (not i%fizz) and (not i%buzz):
            print ('%s %s %s' % ('Number:', i, 'divisible by Fizz and Buzz'))
        elif (i == fizz) or (not i%fizz):
            print (f'Number: {i} divisible by Fizz')
        elif (i == buzz) or (not i%buzz):
            print (f'Number: {i} divisible by Buzz')
        else:
            print('%s %s %s' % ('Number:', i, 'is not divisible by Fizz and Buzz'))
# закрытие текстового файла по результатам работы цикла
r.close()
