# Задача прикрасити fizz-buzz.

# РЕЗЮМЕ:
# 1) Использовал функцию enumerate() для приясвоения индекса каждому числу

fizz, buzz, fb = map(int, input('Type three integer separated by comma: ').split(','))

# создаю список, куда будут записыватся результаты сработки цикла
list_result = []

for i in range (1, fb+1, 1):
    if (not i%fizz) and (not i%buzz):
        list_result.append('FB')
    elif (i == fizz) or (not i%fizz):
        list_result.append('F')
    elif (i == buzz) or (not i%buzz):
        list_result.append('B')
    else:
        list_result.append(i)

print('Result without function enumerate: ', list_result, '\n')

print('Result with function enumerate\n')
# проиндексирую list_result через цикл, для красивого вывода результата
for num, index in enumerate(list_result):
    print('Index:', str(num), 'is', index) 

