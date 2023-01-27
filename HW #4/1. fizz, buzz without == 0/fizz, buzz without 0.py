# Задача fizz-buzz:

# РЕЗЮМЕ:
# 1) Убрал из кода не питонический код: х == 0

# ввод 3-х чисел с клавиатуры
fizz, buzz, fb = map(int, input('Type three integer separated by comma: ').split(','))

# цикл для сравнения fizz, buzz и fb с цифрами введенными с клавиатуры
for i in range (1, fb+1, 1):
    if (not i%fizz) and (not i%buzz):
        print ('FB', end=' ')
    elif (i == fizz) or (not i%fizz):
        print ('F', end=' ')
    elif (i == buzz) or (not i%buzz):
        print ('B', end=' ')
    else:
        print(i, end=' ')
