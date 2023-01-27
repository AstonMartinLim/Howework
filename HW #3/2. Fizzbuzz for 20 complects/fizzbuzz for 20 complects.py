# Задача:
# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл.
# Читайте із файлу перший рядок з трьома числами, беріть із нього числа,
# рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком
# і так до кінця файла.

# ввод 3-х чисел с клавиатуры
fizz, buzz, fb = map(int, input('Type three integer separated by comma: ').split(','))

# открывается текстовый файл
r = open('numbers.txt', 'r')

# переменная-счетчик, чтобы цикл сработал 20 раз
MAX_counter = 20

while MAX_counter != 0:
    MAX_counter -= 1
    # считывание по 1-й строке
    b = r.readline()
    # т.к. ф-я read считывает данные в формате str, их нужно преобразовать
    # в int и для удобства итерации передать в список
    list_of_str = b.split(',')
    list_of_int = list(map(int, list_of_str))
    # цикл для сравнения fizz, buzz и fb с цифрами в текстовом файле  
    for i in list_of_int:
        if (i%fizz == 0) and (i%buzz == 0):
            print ('FB', end=' ')
        elif (i == fizz) or (i%fizz == 0):
            print ('F', end=' ')
        elif (i == buzz) or (i%buzz == 0):
            print ('B', end=' ')
        else:
            print(i, end=' ')
# закрытие текстового файла по результатам работы цикла
r.close()

