# Задача прикрасити fizz-buzz.

# РЕЗЮМЕ:
# 1) использовал list comprehension вместо цикла for (строки 29-30) для вывода
# результата 

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

# list comprehension
[print('Index:', str(num), 'is', index)
for num, index in enumerate(list_result)]

##for num, index in enumerate(list_result):
##    print('Index:', str(num), 'is', index) 
